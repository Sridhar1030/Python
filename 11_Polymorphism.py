class Animal:
    def __init__(self, name):
        # Constructor to initialize the name of the animal
        self.name = name

    def sound(self):
        # This method is designed to be overridden by subclasses to produce the sound of the animal
        pass


class Dog(Animal):
    def __init__(self, name):
        # Constructor to initialize the name of the dog using the constructor of the Animal class
        super().__init__(name)

    def sound(self):
        # Override the sound method to produce the sound of a dog
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        # Constructor to initialize the name of the cat using the constructor of the Animal class
        super().__init__(name)

    def sound(self):
        # Override the sound method to produce the sound of a cat
        return "Meow"


def make_sound(animal):
    # Function that returns the sound of the given animal
    return animal.sound()


def main():
    # Creating instances of Dog and Cat classes
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Printing the name and sound of the dog
    print(f"{dog.name}: {make_sound(dog)}")
    # Printing the name and sound of the cat
    print(f"{cat.name}: {make_sound(cat)}")


if __name__ == "__main__":
    # Calling the main function
    main()
