from __future__ import annotations

from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Subscriber(Observer):
    def update(self, subject: Subject) -> None:
        if subject.isThereAnyPhone == 1:
            print("Tem iphone disponivel")
        else:
            print("Vou continuar esperando")


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Subject) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Publisher(Subject):
    isThereAnyPhone: int = 0

    subscribers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        print("Quero meu iphone vou me inscrever aqui...")
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        print("Cansei de esperar vou comprar o androide mesmo...")
        self.subscribers.remove(observer)

    def notify(self) -> None:
        print("Notificando evento")
        for subscriber in self.subscribers:
            subscriber.update(self)

    def verify_iphones(self) -> None:
        self.isThereAnyPhone = randrange(0, 2)
        self.notify()


if __name__ == "__main__":
    # The client code.

    events = Publisher()

    Subscriber = Subscriber()
    events.subscribe(Subscriber)

    events.verify_iphones()

    events.unsubscribe(Subscriber)

    events.verify_iphones()

