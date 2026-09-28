from app.domain.models import SourceType
from app.sources.base import SourceReader
from app.sources.rss import RSSReader


class SourceRegistry:
    def __init__(self) -> None:
        self._readers: dict[SourceType, SourceReader] = {
            SourceType.RSS: RSSReader(),
        }

    def get_reader(self, source_type: SourceType) -> SourceReader:
        try:
            return self._readers[source_type]
        except KeyError as exc:
            raise ValueError(f"No reader registered for source type: {source_type}") from exc
