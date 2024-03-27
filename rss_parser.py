import json
from json import JSONDecodeError
from pathlib import Path
import time

from bs4 import BeautifulSoup as bs4
from bs4 import ResultSet
from pprint import pprint
import httpx

from abstracts import AbstractGetter, AbstractLogger
from exceptions import EmptyResponseError, HTTPError

from config import settings


class NewsGetter(AbstractGetter):

    def __init__(self, url: str, time_sleep: int) -> None:
        self.url = url
        self.time_sleep = time_sleep

    def _get_response(self) -> httpx.Response | None:
        for attempt in range(4):
            try:
                response = httpx.get(self.url)
                response.raise_for_status()

                return response

            except httpx.HTTPStatusError as error:
                print(f"Request error: {error}")
                print(f"\nRequesting again...\nAttempt no. {attempt + 1}\n")

            time.sleep(1)

        raise HTTPError(f"Couldn't get response from {self.url}")

    def _get_data(self) -> ResultSet | None:
        response = self._get_response()
        if response is None:
            raise EmptyResponseError("Response is empty")

        soup = bs4(response.text, 'xml')
        items = soup.find_all('item')

        return items

    def convert_xml_to_json(self) -> list[dict[str, str]] | None:
        items_json = []
        items = self._get_data()

        for item in items:
            title = item.find('title')
            pub_date = item.find('pubDate')
            category = item.find('category')

            article_data = {
                "title": title.text,
                "category": category.text,
                "date": pub_date.text,
            }

            items_json.append(article_data)

        return items_json


class JsonLogger(AbstractLogger):

    def __init__(self, json_file: Path) -> None:
        self._json_file = json_file

    def log_to_file(self, json_data: list[dict[str, str]]) -> None:
        with open(f"{self._json_file}", "a") as json_file:
            for data in json_data:
                if not self._find_duplicate(data, 'title'):
                    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    def _find_duplicate(self, item: dict, field: str) -> bool:
        try:
            with open(f"{self._json_file}", "r") as json_file:
                data = json.load(json_file)

                for chunk in data:
                    if chunk['title'] == item[field]:
                        return True
                return False
        except JSONDecodeError as error:
            print(f"Error: {error}")


class Logger(AbstractLogger):

    def __int__(self, file: Path) -> None:
        self._file = file

    def log_to_file(self, message: str) -> None:
        with open(self._file, 'a') as file:
            file.write(message + '\n')


if __name__ == '__main__':
    getter = NewsGetter(settings.RSS_URL, settings.TIME_SLEEP)
    json_logger = JsonLogger(settings.JSON_FILE)
    articles = getter.convert_xml_to_json()
    json_logger.log_to_file(articles)
    # pprint(getter.convert_xml_to_json())
