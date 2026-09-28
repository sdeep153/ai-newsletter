from datetime import datetime

from app.domain.models import Article, Source, SourceType
from app.services.ingestion import IngestionService


class FakeReader:
    def fetch_articles(self, source: Source) -> list[Article]:
        return [
            Article(
                title="Test Article",
                url="https://example.com/article",
                summary="Test summary",
                published_at=datetime(2026, 9, 28, 10, 0),
                source=source,
            )
        ]


class FakeRegistry:
    def get_reader(self, source_type: SourceType) -> FakeReader:
        return FakeReader()


def test_ingestion_service_fetches_articles() -> None:
    source = Source(
        name="Example News",
        url="https://example.com/rss",
        type=SourceType.RSS,
    )

    service = IngestionService(FakeRegistry())

    articles = service.fetch_articles(source)

    assert len(articles) == 1
    assert articles[0].title == "Test Article"
