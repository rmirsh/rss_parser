import json
import os
from pathlib import Path

from abstracts import AbstractLogger


class JsonLogger(AbstractLogger):
    """
    Interface for logging to json file without duplicates.

    :param json_file: Path to json file.
    """

    def __init__(self, json_file: Path) -> None:
        self._json_file = json_file

    def log_to_file(self, json_data: list[dict[str, str]]) -> None:
        """Logging to json file."""
        with open(f"{self._json_file}", "w") as json_file:
            uniques = self._find_uniques(json_data)
            json.dump(uniques, json_file, indent=4, ensure_ascii=True)

    def read_json(self):
        """Read logs from file."""
        with open(f"{self._json_file}") as json_file:
            return json.load(json_file)

    def _find_uniques(self, new_json_data: list[dict[str, str]]) -> list[dict[str, str]]:
        """Find only unique values."""
        if os.path.getsize(self._json_file) == 0:
            return new_json_data
        else:
            with open(f"{self._json_file}", "r") as json_file:
                old_json_data = json.load(json_file)
                new_json_set = set(tuple(d.items()) for d in new_json_data)
                old_json_set = set(tuple(d.items()) for d in old_json_data)

            difference = new_json_set - old_json_set
            uniques = [dict(item) for item in difference]
            extended = old_json_data.extend(uniques)

            return extended
