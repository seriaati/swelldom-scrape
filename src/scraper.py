import aiohttp
import bs4
from loguru import logger

from .schema import Article

WEBSITE_URL = "https://www.swelldom.net/"


async def fetch_content(url: str) -> str:
    logger.info(f"Fetching {url}")
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session, session.get(url) as response:
        return await response.text()


def get_articles(content: str) -> list[Article]:
    result: list[Article] = []
    soup = bs4.BeautifulSoup(content, "lxml")
    articles = soup.find_all("article", class_="excerpt")

    for article in articles:
        title = article.find("h2")
        result.append(
            Article(
                title=title.text.strip(),
                url=title.a["href"],
            )
        )

    return result
