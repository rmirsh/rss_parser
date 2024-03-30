import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from pprint import pprint


def display_statistics(file: Path) -> None:
    """Show statistics of news."""
    try:
        with open(file, "r") as file:
            news = json.load(file)
            today_news = _find_today_news(news)
            most_frequent_category = _find_most_frequent_category(today_news)
            today_count = _count_categories(today_news)
            print(f"\nMost frequent category today: {most_frequent_category}")
            print(f"News quantity by categories today: ", end="\n")
            pprint(today_count, width=100)
    except FileNotFoundError as error:
        print(f"{error}")
        print("File with news doesn't exist.")
        print("Please, run the script again.")


def _count_categories(categories: list[dict[str, str]]) -> dict[str, int]:
    """Show count of categories."""
    categories_count = [categories[i]["category"] for i in range(len(categories))]
    return dict(Counter(categories_count))


def _find_today_news(news: list[dict[str, str]]) -> list[dict[str, str]]:
    """Find today news."""
    today = datetime.today().strftime("%a, %d %b %Y %z")
    today_news = [news[i] for i in range(len(news)) if news[i]["date"].startswith(today)]
    return today_news


def _find_most_frequent_category(news: list[dict[str, str]]) -> str:
    """Find most frequent category within news."""
    categories = [news[i]["category"] for i in range(len(news))]
    category_counter = Counter(categories)
    for category in category_counter:
        if category_counter[category] == max(category_counter.values()):
            return category
