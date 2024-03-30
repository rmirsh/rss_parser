import json
import os
from pathlib import Path

from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    """
   Interface for logging to file.

   :param filename: Path to file.
   """
    def __init__(self, filename: Path) -> None:
        self._filename = filename

    def read(self):
        """Read logs from file."""
        with open(self._filename) as file:
            return file.read()

    @abstractmethod
    def log_to_file(self, message: str) -> None:
        pass


class JsonLogger(AbstractLogger):
    """
    Logging to json file without duplicates.
    """

    def log_to_file(self, json_data: list[dict[str, str]]) -> None:
        """Logging to json file."""
        with open(f"{self._filename}", "w") as json_file:
            uniques = self._find_uniques(json_data)
            json.dump(uniques, json_file, indent=4, ensure_ascii=True)

    def read_json(self):
        """Read logs from file."""
        with open(f"{self._filename}") as json_file:
            return json.load(json_file)

    def _find_uniques(self, new_json_data: list[dict[str, str]]) -> list[dict[str, str]]:
        """Find only unique values."""
        if os.path.getsize(self._filename) == 0:
            return new_json_data
        else:
            with open(f"{self._filename}", "r") as json_file:
                old_json_data = json.load(json_file)
                new_json_set = set(tuple(d.items()) for d in new_json_data)
                old_json_set = set(tuple(d.items()) for d in old_json_data)

            difference = new_json_set - old_json_set
            uniques = [dict(item) for item in difference]
            extended = old_json_data.extend(uniques)

            return extended


class TextLogger(AbstractLogger):
    """
    Logging to plain text file.
    """

    def log_to_file(self, message: str) -> None:
        """Logging message to file."""
        with open(self._filename, "a") as file:
            file.write(f"\n{message}\n")
