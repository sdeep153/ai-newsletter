import pytest

from app.domain.models import SourceType
from app.sources.registry import SourceRegistry
from app.sources.rss import RSSReader


def test_registry_returns_rss_reader() -> None:
    registry = SourceRegistry()

    reader = registry.get_reader(SourceType.RSS)

    assert isinstance(reader, RSSReader)


def test_registry_rejects_unregistered_source() -> None:
    registry = SourceRegistry()

    with pytest.raises(ValueError, match="No reader registered"):
        registry.get_reader(SourceType.GITHUB)
