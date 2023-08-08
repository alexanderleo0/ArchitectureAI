from typing import Any


class Person: 
    def __call__(self):
        print("i'm calling")

    def __init__(self, name: str) -> None:
        self.name = name
    def whoAreYou(self):
        print(f"i'm {self.name}")

    @staticmethod
    def checkAge(age: int) -> str:
        if age > 18:
            return "Взрослый"
        else: 
            return "Не взрослый"

# person = Person("Nikitin")
# person.whoAreYou()

print(Person.checkAge(30))
