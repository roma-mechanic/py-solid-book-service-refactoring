from abc import ABC, abstractmethod

from app.books import Book


class PrintService(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrintService(PrintService):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def print(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrintService(PrintService):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
