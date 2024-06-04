import asyncio

from dotenv import load_dotenv
from loguru import logger

from src.database import load_articles, save_articles
from src.scraper import WEBSITE_URL, fetch_content, get_articles
from src.utils import line_notify


async def main() -> None:
    logger.info("Start scraping")

    load_dotenv()

    content = await fetch_content(WEBSITE_URL)
    articles = get_articles(content)

    current_articles = load_articles()
    logger.info(f"{len(current_articles)} posts in database")

    saved_posts = save_articles(articles, current_articles)
    logger.info(f"Saved {len(saved_posts)} posts")

    for post in saved_posts:
        await line_notify(f"\n{post.title}\n{post.url}")

    logger.info("Scraping finished")


if __name__ == "__main__":
    asyncio.run(main())
