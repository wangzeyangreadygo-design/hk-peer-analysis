#!/usr/bin/env python3
"""
Extract structured financial/strategic data from an HK bank PDF report.

Usage:
  python extract_pdf.py <bank_key> <pdf_path> [--out FILE]

Example:
  python extract_pdf.py hsbc_hk /path/to/HSBC-interim-2025.pdf --out hsbc.json

Output: JSON with schema:
  {
    "bank": str,
    "period": str,
    "sections": {
      "strategic_direction": [...text chunks...],
      "retail": [...],
      "corporate": [...],
      "treasury": [...],
      "digital": [...]
    },
    "raw_pages": int
  }

The extraction uses pypdf for text and section-heading heuristics. It does NOT
fabricate numbers — if a KPI is not found, the slot is left null and flagged
for manual review.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pypdf
except ImportError:
    sys.exit("pypdf not installed. Run: pip install pypdf")


SECTION_PATTERNS = {
    "strategic_direction": [
        r"strategic\s+(priorit|direction|focus)", r"chief\s+executive", r"chairman",
        r"战略", r"董事长报告", r"行政总裁", r"业务回顾"
    ],
    "retail": [
        r"wealth.*personal|retail\s+banking|personal\s+banking",
        r"零售|个人银行|财富管理"
    ],
    "corporate": [
        r"commercial\s+banking|corporate.*institutional|wholesale|transaction\s+banking",
        r"企业银行|公司银行|工商金融|商业银行"
    ],
    "treasury": [
        r"treasury|global\s+markets|financial\s+markets|custody|asset\s+management",
        r"金融市场|财资|投资银行|资产托管|资产管理"
    ],
    "digital": [
        r"digital\s+transformation|technology|innovation|AI|artificial\s+intelligence",
        r"数字化|金融科技|人工智能|数码"
    ],
}


def extract_pdf_text(pdf_path: Path) -> list[str]:
    """Return a list of page texts."""
    reader = pypdf.PdfReader(str(pdf_path))
    return [page.extract_text() or "" for page in reader.pages]


def section_of(line: str) -> str | None:
    """Return section name if line matches any section pattern."""
    low = line.lower()
    for sec, patterns in SECTION_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, low, re.IGNORECASE):
                return sec
    return None


def chunk_by_sections(pages: list[str]) -> dict[str, list[str]]:
    """Bucket page content by detected section. Pages often overlap topics."""
    buckets: dict[str, list[str]] = {k: [] for k in SECTION_PATTERNS}
    for i, page in enumerate(pages):
        hit_sections = set()
        for line in page.split("\n"):
            sec = section_of(line)
            if sec:
                hit_sections.add(sec)
        # attribute page text to each section it mentions
        for sec in hit_sections:
            buckets[sec].append(f"[p.{i+1}]\n{page.strip()[:3000]}")
    return buckets


def extract_kpis(pages: list[str]) -> dict:
    """Best-effort KPI extraction. Returns null for unfound — NEVER fabricates."""
    full = "\n".join(pages)
    kpis = {}
    # Net new customers (万, 千 or '00,000s)
    m = re.search(r"(新增|net new)[^\n]{0,30}(\d+(?:\.\d+)?)\s*(万名|万|千|thousand|million)", full, re.IGNORECASE)
    kpis["net_new_customers"] = m.group(0) if m else None
    # AUM
    m = re.search(r"(AUM|资产管理规模|客户资产)[^\n]{0,50}(US\$|HK\$|\$|港元|美元|人民币)?\s*([\d,.]+)\s*(trillion|billion|million|万亿|亿|百万)", full, re.IGNORECASE)
    kpis["aum"] = m.group(0) if m else None
    # Net trading income
    m = re.search(r"(net trading|净交易)[^\n]{0,80}", full, re.IGNORECASE)
    kpis["net_trading_income"] = m.group(0) if m else None
    # Custody
    m = re.search(r"(custody|托管)[^\n]{0,80}", full, re.IGNORECASE)
    kpis["custody"] = m.group(0) if m else None
    return kpis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bank_key", help="Bank ID e.g. hsbc_hk, scb_hk, bochk, hang_seng")
    ap.add_argument("pdf_path", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--period", default=None, help="e.g. 2025H1 or 2024FY")
    args = ap.parse_args()

    if not args.pdf_path.exists():
        sys.exit(f"File not found: {args.pdf_path}")

    pages = extract_pdf_text(args.pdf_path)
    sections = chunk_by_sections(pages)
    kpis = extract_kpis(pages)

    out = {
        "bank": args.bank_key,
        "period": args.period,
        "source_file": args.pdf_path.name,
        "raw_pages": len(pages),
        "sections": sections,
        "kpis_best_effort": kpis,
        "note": "KPIs are best-effort regex matches. Verify against source PDF before use. Null values mean no match was found — DO NOT fabricate."
    }

    if args.out:
        args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"Wrote {args.out}")
    else:
        json.dump(out, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
