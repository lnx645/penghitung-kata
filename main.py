#!/usr/bin/env python3
"""Analisis teks CLI: kata, kalimat, karakter, paragraf, kata teratas."""
import argparse
import re
import sys
from collections import Counter

STOPWORDS = {"dan", "yang", "di", "ke", "dari"}


def analyze(text: str) -> dict:
    words = re.findall(r"\b[\w']+\b", text.lower())
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    paragraphs = [p for p in text.split("\n") if p.strip()]
    freq = Counter(w for w in words if w not in STOPWORDS)
    return {
        "kata": len(words),
        "kalimat": len(sentences),
        "karakter": len(text),
        "paragraf": len(paragraphs),
        "teratas": freq.most_common(10),
    }


def print_report(r: dict) -> None:
    print(f"Jumlah kata      : {r['kata']}")
    print(f"Jumlah kalimat   : {r['kalimat']}")
    print(f"Jumlah karakter  : {r['karakter']}")
    print(f"Jumlah paragraf  : {r['paragraf']}")
    print("\n10 kata teratas (tanpa kata umum):")
    for i, (w, c) in enumerate(r["teratas"], 1):
        print(f"  {i:>2}. {w} ({c}x)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analisis statistik teks")
    parser.add_argument("file", nargs="?", help="Path file teks (opsional; default baca dari stdin)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    else:
        if sys.stdin.isatty():
            print("Tempel teks lalu tekan Ctrl+D:")
        text = sys.stdin.read()

    if not text.strip():
        print("Error: tidak ada teks untuk dianalisis.", file=sys.stderr)
        sys.exit(1)

    print_report(analyze(text))


if __name__ == "__main__":
    main()
