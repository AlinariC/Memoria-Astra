#!/usr/bin/env python3
"""Cross-trilogy review audit for continuity, prose seams, and package shape."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
REPORT = ROOT / "production" / "full-trilogy-review.md"


@dataclass(frozen=True)
class BookSpec:
    number: int
    title: str
    folder: str
    chapters: int


BOOKS = (
    BookSpec(1, "The Ash Beneath the Crown", "book-01-the-ash-beneath-the-crown", 36),
    BookSpec(2, "The Moon Below the World", "book-02-the-moon-below-the-world", 31),
    BookSpec(3, "The Dragon That Dreamed Death", "book-03-the-dragon-that-dreamed-death", 41),
)


BANNED_OR_SCAFFOLD = (
    "The chapter's truth settled slowly",
    "Trouble came wearing the local weather",
    "did not reveal itself all at once",
    "When the attack came",
    "purpose was clear enough",
    "remained before them",
    "under it all",
    "Book One is",
    "Book Two is",
    "Book Three is",
    "shape of Book",
    "Final Fantasy",
    "World of Warcraft",
    "Lord of the Rings",
    "hobbit",
    "hobbits",
)


CANON_TERMS = (
    "Mara",
    "Joryn",
    "Caldus",
    "Saelith",
    "Ilyr",
    "Tavi",
    "Kesh",
    "Brakka",
    "Arveth",
    "Vorrakai",
    "Veyrasha",
    "Othrava",
    "Sava",
    "Maelin",
    "Kell Ashgate",
    "Harrowmere",
    "Lumenorath",
    "Khar Veyl",
    "Orrowen",
    "Brassroot",
    "Gloamfen",
    "Seven Arches",
    "Third Arch",
    "Pale Bough",
    "Umbral Seat",
    "Crownreach",
    "cinder",
    "cinders",
    "cinder-singer",
    "cinder-singing",
)


STYLEWATCH = (
    "answerable",
    "witness",
    "useful",
    "personhood",
    "mercy",
    "command",
    "crown",
    "chair",
    "road",
    "soup",
    "onions",
    "Good.",
)


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


def word_count(text: str) -> int:
    return len(words(text))


def chapters(text: str) -> list[tuple[int, str, str]]:
    matches = list(re.finditer(r"(?m)^## Chapter (\d+): (.+)$", text))
    back = re.search(r"(?m)^## (?:Back Matter|Glossary)\b", text)
    limit = back.start() if back else len(text)
    result: list[tuple[int, str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        if start >= limit:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else limit
        result.append((int(match.group(1)), match.group(2).strip(), text[start:end].strip()))
    return result


def sentence_list(text: str) -> list[str]:
    raw = re.split(r"(?<=[.!?])\s+", text)
    cleaned = []
    for sentence in raw:
        s = re.sub(r"\s+", " ", sentence.strip())
        if len(s.split()) >= 12 and not s.startswith("**"):
            cleaned.append(s)
    return cleaned


def paragraph_list(text: str) -> list[str]:
    paras = []
    for paragraph in re.split(r"\n\s*\n", text):
        p = re.sub(r"\s+", " ", paragraph.strip())
        if len(p.split()) >= 25 and not p.startswith("**"):
            paras.append(p)
    return paras


def ngrams(token_list: list[str], n: int) -> Counter[str]:
    lowered = [t.lower() for t in token_list]
    stop = {
        "the",
        "and",
        "that",
        "with",
        "from",
        "into",
        "they",
        "their",
        "there",
        "this",
        "was",
        "were",
        "had",
        "not",
        "for",
        "but",
        "you",
        "her",
        "him",
        "she",
        "his",
        "all",
    }
    counts: Counter[str] = Counter()
    for i in range(len(lowered) - n + 1):
        chunk = lowered[i : i + n]
        if sum(1 for w in chunk if w in stop) > n - 2:
            continue
        counts[" ".join(chunk)] += 1
    return counts


def first_sentence(chapter_text: str) -> str:
    body = re.sub(r"(?m)^## Chapter \d+: .+$", "", chapter_text, count=1).strip()
    body = re.sub(r"(?m)^# Part .+$", "", body).strip()
    sentences = sentence_list(body)
    return sentences[0] if sentences else ""


def last_sentence(chapter_text: str) -> str:
    body = re.sub(r"(?m)^## Chapter \d+: .+$", "", chapter_text, count=1).strip()
    sentences = sentence_list(body)
    return sentences[-1] if sentences else ""


def main() -> None:
    lines = [
        "# Full Trilogy Review Audit",
        "",
        "This report is a mechanical companion to the five-role reader review. It flags structural risks, repeated seams, term consistency, and high-frequency motifs before the next prose pass.",
        "",
    ]

    all_sentences: dict[str, list[str]] = defaultdict(list)
    all_paragraphs: dict[str, list[str]] = defaultdict(list)
    all_tokens: list[str] = []
    issues: list[str] = []
    concise_watch: list[str] = []

    lines.extend(["## Package Shape", "", "| Book | Chapters | Words | Back Matter | Part Headings | Longest Chapter | Shortest Chapter |", "| --- | ---: | ---: | ---: | ---: | --- | --- |"])
    book_texts: dict[str, str] = {}
    for spec in BOOKS:
        book_dir = OUTPUT / spec.folder
        text = (book_dir / "manuscript.md").read_text(encoding="utf-8")
        book_texts[spec.title] = text
        chaps = chapters(text)
        chap_counts = [(no, title, word_count(body)) for no, title, body in chaps]
        longest = max(chap_counts, key=lambda item: item[2])
        shortest = min(chap_counts, key=lambda item: item[2])
        back_count = len(re.findall(r"(?m)^## (?:Back Matter|Glossary)\b", text))
        part_count = len(re.findall(r"(?m)^# Part ", text))
        lines.append(
            f"| {spec.title} | {len(chaps)} | {word_count(text):,} | {back_count} | {part_count} | Ch. {longest[0]} {longest[2]:,}w | Ch. {shortest[0]} {shortest[2]:,}w |"
        )
        if len(chaps) != spec.chapters:
            issues.append(f"{spec.title}: expected {spec.chapters} chapters, found {len(chaps)}")
        if back_count != 1:
            issues.append(f"{spec.title}: expected one Back Matter section, found {back_count}")
        if shortest[2] < 1400:
            issues.append(f"{spec.title}: Chapter {shortest[0]} is short for epic pacing at {shortest[2]:,} words")
        if longest[2] > 7000:
            issues.append(f"{spec.title}: Chapter {longest[0]} is long enough to review for pacing at {longest[2]:,} words")
        for no, title, count in chap_counts:
            if count < 1800:
                concise_watch.append(f"{spec.title}: Ch. {no} `{title}` at {count:,} words")

        for no, title, body in chaps:
            label = f"{spec.title} Ch. {no}: {title}"
            for sentence in sentence_list(body):
                all_sentences[sentence].append(label)
            for paragraph in paragraph_list(body):
                all_paragraphs[paragraph].append(label)
            all_tokens.extend(words(body))

    lines.extend(["", "## Banned/Scaffold/IP Phrase Scan", ""])
    any_banned = False
    for phrase in BANNED_OR_SCAFFOLD:
        hits = []
        for title, text in book_texts.items():
            if re.search(re.escape(phrase), text, re.IGNORECASE):
                hits.append(title)
        if hits:
            any_banned = True
            lines.append(f"- `{phrase}` found in: {', '.join(hits)}")
            issues.append(f"Phrase cleanup needed: {phrase}")
    if not any_banned:
        lines.append("- No banned scaffold/comparison/IP phrases found in manuscripts.")

    exact_sentence_repeats = [(s, locs) for s, locs in all_sentences.items() if len(locs) > 1]
    exact_paragraph_repeats = [(p, locs) for p, locs in all_paragraphs.items() if len(locs) > 1]
    lines.extend(["", "## Exact Repetition", ""])
    if exact_paragraph_repeats:
        lines.append("### Paragraphs")
        for paragraph, locs in exact_paragraph_repeats[:20]:
            sample = paragraph[:180] + ("..." if len(paragraph) > 180 else "")
            lines.append(f"- {len(locs)}x in {', '.join(locs[:4])}: {sample}")
            issues.append("Exact repeated paragraph detected")
    else:
        lines.append("- No exact repeated long paragraphs found.")
    if exact_sentence_repeats:
        lines.append("")
        lines.append("### Sentences")
        for sentence, locs in exact_sentence_repeats[:30]:
            sample = sentence[:180] + ("..." if len(sentence) > 180 else "")
            lines.append(f"- {len(locs)}x in {', '.join(locs[:5])}: {sample}")
    else:
        lines.append("- No exact repeated long sentences found.")

    lines.extend(["", "## High-Frequency 5-Word Phrases", ""])
    gram_counts = ngrams(all_tokens, 5)
    common = [(gram, count) for gram, count in gram_counts.most_common(40) if count >= 4]
    if common:
        for gram, count in common[:25]:
            lines.append(f"- {count}x `{gram}`")
    else:
        lines.append("- No 5-word phrase repeats above threshold.")

    lines.extend(["", "## Canon Term Counts", "", "| Term | Book 1 | Book 2 | Book 3 |", "| --- | ---: | ---: | ---: |"])
    for term in CANON_TERMS:
        row = [term]
        for spec in BOOKS:
            text = book_texts[spec.title]
            pattern = r"\b" + re.escape(term) + r"\b"
            row.append(str(len(re.findall(pattern, text))))
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

    variant_checks = {
        "cinder singer": "Use hyphenated `cinder-singer` unless context intentionally separates words.",
        "cinder singing": "Use hyphenated `cinder-singing` unless context intentionally separates words.",
        "Cinder Singer": "Lowercase unless used as a formal title.",
        "dark elf": "Use `dark-elf` adjectivally when parallel to `light-elf`.",
        "light elf": "Use `light-elf` adjectivally when parallel to `dark-elf`.",
        "Seven arches": "Use `Seven Arches` for the formal place name.",
        "third arch": "Use `Third Arch` for the formal bridge.",
    }
    lines.extend(["", "## Term Variant Watchlist", ""])
    variant_found = False
    for variant, guidance in variant_checks.items():
        found = []
        for spec in BOOKS:
            text = book_texts[spec.title]
            count = len(re.findall(r"\b" + re.escape(variant) + r"\b", text))
            if count:
                found.append(f"{spec.title}: {count}")
        if found:
            variant_found = True
            lines.append(f"- `{variant}` -> {guidance} Hits: {', '.join(found)}")
    if not variant_found:
        lines.append("- No obvious canon-term variants found.")

    lines.extend(["", "## Motif Frequency Watch", "", "| Motif | Count |", "| --- | ---: |"])
    combined = "\n".join(book_texts.values())
    for motif in STYLEWATCH:
        count = len(re.findall(re.escape(motif), combined, re.IGNORECASE if motif != "Good." else 0))
        lines.append(f"| {motif} | {count} |")

    lines.extend(["", "## Concise Chapter Watchlist", ""])
    if concise_watch:
        lines.extend(f"- {item}" for item in concise_watch)
    else:
        lines.append("- No chapters under the 1,800-word watch threshold.")

    lines.extend(["", "## Chapter Opening/Closing Samples To Spot-Check", ""])
    for spec in BOOKS:
        lines.append(f"### {spec.title}")
        chaps = chapters(book_texts[spec.title])
        for no, title, body in chaps[:2] + chaps[-2:]:
            opener = first_sentence(body)
            closer = last_sentence(body)
            lines.append(f"- Ch. {no} `{title}` opens: {opener[:160]}")
            lines.append(f"  closes: {closer[:160]}")

    lines.extend(["", "## Audit Issues", ""])
    if issues:
        deduped = list(dict.fromkeys(issues))
        for issue in deduped:
            lines.append(f"- {issue}")
    else:
        lines.append("- No mechanical blockers found for publishing handoff.")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()
