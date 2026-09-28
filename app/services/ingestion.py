from app.domain.models import Article, Source
from app.sources.registry import SourceRegistry


class IngestionService:
    def __init__(self, registry: SourceRegistry) -> None:
        self._registry = registry

    def fetch_articles(self, source: Source) -> list[Article]:
        reader = self._registry.get_reader(source.type)

        return reader.fetch_articles(source)
