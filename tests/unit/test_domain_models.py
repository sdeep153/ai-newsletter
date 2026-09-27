from datetime import date, datetime

from app.domain.models import Article, Newsletter, Source, SourceType


def test_article_creation() -> None:
    source = Source(
        name="Example News",
        url="https://example.com",
        type=SourceType.RSS,
    )

    article = Article(
        title="AI makes another breakthrough",
        url="https://example.com/article",
        summary="An example AI article.",
        published_at=datetime(2026, 9, 27, 10, 0),
        source=source,
    )

    assert article.title == "AI makes another breakthrough"
    assert article.source.name == "Example News"


def test_newsletter_creation() -> None:
    newsletter = Newsletter(
        issue_date=date(2026, 9, 27),
        title="AI Daily",
        articles=[],
    )

    assert newsletter.title == "AI Daily"
    assert newsletter.articles == []
