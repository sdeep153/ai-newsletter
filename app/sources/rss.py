from datetime import datetime

import feedparser

from app.domain.models import Article, Source


def fetch_articles(source: Source) -> list[Article]:
    feed = feedparser.parse(str(source.url))

    articles: list[Article] = []

    for entry in feed.entries:
        if not entry.get("title") or not entry.get("link"):
            continue

        published_at = _parse_published_at(entry)

        if published_at is None:
            continue

        articles.append(
            Article(
                title=entry.title,
                url=entry.link,
                summary=entry.get("summary", ""),
                published_at=published_at,
                source=source,
            )
        )

    return articles


def _parse_published_at(entry: dict) -> datetime | None:
    published_parsed = entry.get("published_parsed")

    if published_parsed is None:
        return None

    return datetime(*published_parsed[:6])
