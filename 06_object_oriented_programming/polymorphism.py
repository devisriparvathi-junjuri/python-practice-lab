"""Polymorphism lets callers use a shared behavior."""

class Dog:
    def speak(self) -> str:
        return "woof"

class Cat:
    def speak(self) -> str:
        return "meow"


def sounds(animals: list[Dog | Cat]) -> list[str]:
    return [animal.speak() for animal in animals]

print(sounds([Dog(), Cat()]))
