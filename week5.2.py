class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs 🐕")


class Bird(Animal):
    def move(self):
        print("The bird flies in the sky 🦅")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water 🐟")

class Vehicle:
    def move(self):
        pass  


class Car(Vehicle):
    def move(self):
        print("The car drives on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky ✈️")


dog = Dog()
dog.move() 
bird = Bird()
bird.move()  
fish = Fish()
fish.move()  
car = Car()
car.move() 
plane = Plane()
plane.move() 
