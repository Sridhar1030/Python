class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Meow"


def make_sound(animal):
    return animal.sound()


def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(f"{dog.name}: {make_sound(dog)}")
    print(f"{cat.name}: {make_sound(cat)}")


if __name__ == "__main__":
    main()
