from abc import ABC, abstractmethod
from typing import List, Callable

class Pet(ABC):
    pass

class Dog(Pet):
    def __str__(self) -> str:
        return "Dog"    
class Cat(Pet):
    def __str__(self) -> str:
        return "Cat"
     

class Person(ABC):
    @abstractmethod
    def get_pet(self) -> Pet:

        pass

    def play(self, pet: Pet = None):
        if pet is None:
            pet = self.get_pet()
        print(f"Playing with {pet}")


class DogPerson(Person):
    def __init__(self):
        self.dog = Dog()

    def get_pet(self):
        return self.dog


class CatLover(Person):
    def __init__(self):
        self.cat = Cat()

    def get_pet(self):
        return self.cat


def call(person: Person):
    person.play()

if __name__ == "__main__":
    call(DogPerson())
    call(CatLover())