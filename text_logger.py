from pathlib import Path

from abstracts import AbstractLogger


class TextLogger(AbstractLogger):
    """
    Interface for logging to plain text file.

    :param file: Path to text file.
    """

    def __init__(self, file: Path) -> None:
        self._file = file

    def log_to_file(self, message: str) -> None:
        """Logging message to file."""
        with open(self._file, "a") as file:
            file.write(f"\n{message}\n")
