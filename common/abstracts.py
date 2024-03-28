from abc import ABC, abstractmethod


class AbstractGetter(ABC):
    @abstractmethod
    def _get_response(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class AbstractLogger(ABC):
    @abstractmethod
    def log_to_file(self, message: str):
        pass
