from abc import ABC, abstractmethod


class Runnable(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError()

