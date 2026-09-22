"""
Скрипт для сбора текстов из Википедии через API.
"""
import requests

def fetch_wiki_article(title: str) -> str:
    """Получает текст статьи из Википедии."""
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
    }
    response = requests.get(url, params=params)
    data = response.json()
    pages = data["query"]["pages"]
    for page_id, page_data in pages.items():
        return page_data.get("extract", "")
    return ""

if __name__ == "__main__":
    articles = [
        "Искусственная нейронная сеть",
        "Свёрточная нейронная сеть",
        "Рекуррентная нейронная сеть",
    ]
    for title in articles:
        text = fetch_wiki_article(title)
        print(f"=== {title} ===")
        print(text[:500])
