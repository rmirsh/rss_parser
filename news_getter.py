import time

import httpx
from bs4 import BeautifulSoup as bs4
from bs4 import ResultSet

from abstracts import AbstractGetter
from exceptions import EmptyResponseError, HTTPError


class NewsGetter(AbstractGetter):
    """
    Class that retrieve RSS news in XML and convert them into python dict.

    :param url: URL to request RSS news.
    """

    def __init__(self, url: str) -> None:
        self.url = url

    def _get_response(self) -> httpx.Response | None:
        """Make request to retrieve XML"""
        for attempt in range(4):
            try:
                response = httpx.get(self.url)
                response.raise_for_status()

                return response

            except httpx.HTTPStatusError as error:
                print(f"Request error: {error}")
                print(
                    f"\nRequesting again...\nAttempt no. {attempt}\n"
                    if attempt > 0
                    else ""
                )

            time.sleep(3)

        raise HTTPError(f"Couldn't get response from {self.url}")

    def get_data(self) -> ResultSet:
        """Extract data that we want from response."""
        response = self._get_response()
        if response is None:
            raise EmptyResponseError("Response is empty")

        soup = bs4(response.text, "xml")
        items = soup.find_all("item")

        return items

    @staticmethod
    def convert_xml_to_dict(xml_data: ResultSet) -> list[dict[str, str]]:
        """Converting XML to python dict."""
        items_json = []

        for item in xml_data:
            title = item.find("title")
            pub_date = item.find("pubDate")
            category = item.find("category")

            article_data = {
                "title": title.text,
                "category": category.text,
                "date": pub_date.text,
            }

            items_json.append(article_data)

        return items_json
