from __future__ import annotations
from abc import ABC, abstractmethod


class TransportFactory(ABC):
    """
    Abstract factory class that defines the method for creating a transport vehicle.
    """

    @abstractmethod
    def create_transport(self):
        pass

    def deliver(self) -> str:
        """
        Main business method that uses the created transport vehicle.
        """
        transport = self.create_transport()
        result = f"TransportFactory: Delivery is performed using {transport.move()}"
        return result


class CarFactory(TransportFactory):
    """
    Factory that creates cars.
    """
    def create_transport(self) -> Transport:
        return Car()


class BikeFactory(TransportFactory):
    """
    Factory that creates bicycles.
    """
    def create_transport(self) -> Transport:
        return Bike()


class Transport(ABC):
    """
    Abstract class for all types of transport.
    """

    @abstractmethod
    def move(self) -> str:
        pass


class Car(Transport):
    """
    Concrete class representing a car.
    """
    def move(self) -> str:
        return "a car (fast and comfortable)"


class Bike(Transport):
    """
    Concrete class representing a bicycle.
    """
    def move(self) -> str:
        return "a bicycle (eco-friendly and cheap)"


def client_code(factory: TransportFactory) -> None:
    """
    Client code that works with the factory through its base interface.
    """
    print(f"Client: Using the factory to obtain transport.\n"
          f"{factory.deliver()}", end="")


