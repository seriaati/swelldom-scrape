import json
import pathlib

from .schema import Article

FILE_PATH = pathlib.Path("articles.json")


def load_articles() -> list[Article]:
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, encoding="utf-8") as f:
        return [Article(**article) for article in json.load(f)]


def get_article(articles: list[Article], article_id: int) -> Article | None:
    return next((post for post in articles if post.id == article_id), None)


def save_articles(to_save: list[Article], current_articles: list[Article]) -> list[Article]:
    to_save = [post for post in to_save if get_article(current_articles, post.id) is None]
    current_articles.extend(to_save)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([post.model_dump() for post in current_articles], f, ensure_ascii=False, indent=2)

    return to_save
