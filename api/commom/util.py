import httpx
from bs4 import BeautifulSoup


# Access page and return its content
async def get_page_content(url: str) -> str:
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    soup = BeautifulSoup(res.content, "html.parser")
    page_content = soup.get_text()

    return page_content
