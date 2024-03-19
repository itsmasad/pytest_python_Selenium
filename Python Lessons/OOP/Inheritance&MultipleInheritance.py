# Define a base class called Animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Some generic sound")

# Define a subclass Dog which inherits from Animal
class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

# Define another subclass Cat which also inherits from Animal
class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")

# Define a subclass Duck which inherits from both Dog and Cat
# This demonstrates multiple inheritance
class Duck(Dog, Cat):
    def sound(self):
        print("Quack! Quack!")

# Create instances of Dog, Cat, and Duck
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Daffy")

# Call the sound method on instances of Dog, Cat, and Duck
# The sound method behaves differently for each object based on their respective implementations
dog.sound()  # Outputs: "Woof! Woof!"
cat.sound()  # Outputs: "Meow! Meow!"
duck.sound()  # Outputs: "Quack! Quack!"

# Accessing the 'name' attribute inherited from the Animal class
print(duck.name,dog.name,cat.name)  # Outputs: "Daffy"
