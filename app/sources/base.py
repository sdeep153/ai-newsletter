from abc import ABC, abstractmethod

from app.domain.models import Article, Source


class SourceReader(ABC):
    @abstractmethod
    def fetch_articles(self, source: Source) -> list[Article]:
        """Fetch articles from a source."""
