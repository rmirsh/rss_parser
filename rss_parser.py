from datetime import datetime

from exceptions import HTTPError
from loggers import TextLogger, JsonLogger
from getters import NewsGetter

from config import settings


class RSSParser:
    """Parser of RSS news."""

    def __init__(self) -> None:
        self.json_logger = JsonLogger(settings.JSON_FILE)
        self.text_logger = TextLogger(settings.LOG_FILE)
        self.news_getter = NewsGetter(settings.RSS_URL)

    def parse_news(self) -> None:
        """Display news in console."""
        try:
            xml_news = self.news_getter.get_data()
            news = self.news_getter.convert_xml_to_dict(xml_news)
            self.json_logger.log_to_file(news)

            self._log_succees()

        except HTTPError as error:
            self._log_error(error)

    def _log_succees(self) -> None:
        """Log success message."""
        message = f"News was succesfuly written at {datetime.now()}"
        self.text_logger.log_to_file(message)

    def _log_error(self, error) -> None:
        """Log error message."""
        message = f"News wasn't written at {datetime.now()}\nDue to error:\n{error}"
        self.text_logger.log_to_file(message)
