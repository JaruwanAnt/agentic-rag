from pathlib import Path

STOP_WORDS = {
    "what", "is", "the", "a", "an", "on", "of", "to",
    "for", "when", "should", "do", "does", "are",
    "can", "be"
}


def retrieve(query: str, top_k: int = 3, min_score: int = 2) -> list[str]:
    text = Path("knowledge_base.txt").read_text(encoding="utf-8")

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    keywords = [
        word.lower()
        for word in query.split()
        if word.lower() not in STOP_WORDS
    ]

    scored = []

    for paragraph in paragraphs:
        score = sum(
            1
            for keyword in keywords
            if keyword in paragraph.lower()
        )

        if score >= min_score:
            scored.append((score, paragraph))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [paragraph for _, paragraph in scored[:top_k]]