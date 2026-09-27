from datetime import date, datetime
from enum import StrEnum

from pydantic import BaseModel, HttpUrl


class SourceType(StrEnum):
    RSS = "rss"
    NEWS_API = "news_api"
    GITHUB = "github"


class Source(BaseModel):
    name: str
    url: HttpUrl
    type: SourceType


class Article(BaseModel):
    title: str
    url: HttpUrl
    summary: str
    published_at: datetime
    source: Source


class Newsletter(BaseModel):
    issue_date: date
    title: str
    articles: list[Article]
