from typing import Any


class Person: 
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     print("i'm calling")

    def __init__(self, name: str) -> None:
        self.name = name
    def whoAreYou(self):
        print(f"i'm {self.name}")

person = Person("Nikitin")
person.whoAreYou()