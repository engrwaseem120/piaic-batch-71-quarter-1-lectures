from animals import Dog, Cat, Parrot, Sparrow
from vehicles import Car, Bike

dog = Dog()
cat = Cat()
parrot = Parrot()
sparrow = Sparrow()

print(dog.speak())
print(cat.speak())
print(parrot.speak())
print(sparrow.speak())

car = Car("Toyota Corolla")
bike = Bike("Harley Davidson")

print(car.display())
print(bike.display())