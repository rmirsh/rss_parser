import time

from config import settings
from rss_parser import RSSParser
from statistics import display_statistics


def main():
    try:
        while True:
            parser = RSSParser()
            parser.parse_news()

            time.sleep(settings.TIME_SLEEP)
    except KeyboardInterrupt:
        if settings.SHOW_STATISTICS:
            display_statistics(settings.JSON_FILE)


if __name__ == "__main__":
    main()
