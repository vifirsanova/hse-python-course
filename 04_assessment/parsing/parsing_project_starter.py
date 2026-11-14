"""
Стартовый шаблон проектного ДЗ по веб-парсингу и анализу данных.
Заполните блоки TODO под выбранный вами открытый веб-источник.
"""

import os
import time
from urllib.parse import urljoin

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


class CatalogScraper:
    """Каркас парсера каталога с пагинацией и подсчётом ошибок."""

    def __init__(self, base_url: str, max_pages: int = 3, delay_sec: float = 1.0):
        self.base_url = base_url
        self.max_pages = max_pages
        self.delay_sec = delay_sec
        self.error_count = 0

    def fetch_page(self, url: str) -> str | None:
        """Скачать HTML одной страницы или вернуть None при ошибке сети."""
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code == 404:
                return None
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding
            return resp.text
        except requests.RequestException as exc:
            self.error_count += 1
            print(f"[WARN] Ошибка запроса {url}: {exc}")
            return None

    def parse_card(self, card_tag) -> dict:
        """Преобразовать один HTML-элемент карточки в словарь признаков."""
        # TODO: адаптируйте селекторы под ваш сайт
        title_tag = card_tag.select_one("h3 a")
        price_tag = card_tag.select_one("p.price_color")
        if title_tag is None or price_tag is None:
            raise ValueError("Отсутствует обязательное поле карточки")

        raw_price = price_tag.get_text(strip=True).lstrip("£$€Â ")
        return {
            "title": (title_tag.get("title") or title_tag.get_text(strip=True)).strip(),
            "price": float(raw_price),
            "url": urljoin(self.base_url, title_tag.get("href", "")),
        }

    def run(self) -> pd.DataFrame:
        """Обойти страницы каталога и вернуть собранный DataFrame."""
        items: list[dict] = []
        for page in range(1, self.max_pages + 1):
            page_url = self.base_url.format(page=page)
            html = self.fetch_page(page_url)
            if html is None:
                break

            soup = BeautifulSoup(html, "html.parser")
            # TODO: укажите тег и класс карточки вашего источника
            cards = soup.find_all("article", class_="product_pod")
            for card in cards:
                try:
                    items.append(self.parse_card(card))
                except ValueError:
                    self.error_count += 1

            if page < self.max_pages:
                time.sleep(self.delay_sec)

        return pd.DataFrame(items)

    def __str__(self) -> str:
        return f"CatalogScraper(max_pages={self.max_pages}, errors={self.error_count})"


def save_basic_plots(df: pd.DataFrame, plots_dir: str = "plots") -> None:
    """Пример сохранения базовой гистограммы цен в папку plots/."""
    if df.empty or "price" not in df.columns:
        return
    os.makedirs(plots_dir, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(data=df, x="price", bins=15, ax=ax)
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig(os.path.join(plots_dir, "plot_1_dist.png"), dpi=120)
    plt.close(fig)


# ============================================================
# Локальный офлайн самотест разбора карточки (без сети)
# ============================================================

if __name__ == "__main__":
    sample_card_html = """
    <article class="product_pod">
      <h3><a href="book_1/index.html" title="Data Science Handbook">Data Science...</a></h3>
      <p class="price_color">£39.90</p>
    </article>
    """
    scraper = CatalogScraper("https://books.toscrape.com/catalogue/page-{page}.html")
    soup_test = BeautifulSoup(sample_card_html, "html.parser")
    parsed = scraper.parse_card(soup_test.find("article"))

    assert parsed["title"] == "Data Science Handbook"
    assert parsed["price"] == 39.90
    assert parsed["url"].endswith("book_1/index.html")
    print("Самотест стартового шаблона успешно пройден:", scraper)
