import feedparser

from app.domain.models import Source, SourceType
from app.sources.rss import fetch_articles


def test_fetch_articles(monkeypatch) -> None:
    rss_content = """
    <rss version="2.0">
        <channel>
            <title>Example News</title>
            <item>
                <title>AI makes another breakthrough</title>
                <link>https://example.com/article</link>
                <description>An example AI article.</description>
                <pubDate>Sat, 27 Sep 2026 10:00:00 GMT</pubDate>
            </item>
        </channel>
    </rss>
    """

    parsed_feed = feedparser.parse(rss_content)

    monkeypatch.setattr(
        "app.sources.rss.feedparser.parse",
        lambda _url: parsed_feed,
    )

    source = Source(
        name="Example News",
        url="https://example.com/rss",
        type=SourceType.RSS,
    )

    articles = fetch_articles(source)

    assert len(articles) == 1
    assert articles[0].title == "AI makes another breakthrough"
    assert str(articles[0].url) == "https://example.com/article"
    assert articles[0].source.name == "Example News"
