# Component interface
class Car:
    
    def start(self):
        pass

    def stop(self):
        pass

    def cost(self):
        pass

# Concrete Component
class BasicCar(Car):
    def start(self):
        print("Starting basic Car")
    
    def stop(self):
        print("Stoping the basic Car")

    def cost(self):
        return 20000

# Decorator base class
class CarDecorator(Car):
    def __init__(self, car: Car):
        self._car = car

    def start(self):
        self._car.start()

    def stop(self):
        self._car.stop()
        
    def cost(self):
        return self._car.cost()

# Concrete Decorators
class SunroofCar(CarDecorator):

    def start(self):
        print("Starting the SunRoof Car")

    def stop(self):
        print("Shuting the SunRoof Car")

    def cost(self):
        return self._car.cost() + 3000

class BulletproofCar(CarDecorator):
    def start(self):
        print("Starting the Bulletproof Car")

    def stop(self):
        print("Shuting theBulletproof Car")

    def cost(self):
        return self._car.cost() + 15000

# Usage
if __name__ == "__main__":
    # Create a basic car
    basic_car = BasicCar()
    basic_car.start()
    basic_car.stop()
    print(f"Cost of basic car: ${basic_car.cost()}\n")

    # Add sunroof to the basic car
    sunroof_car = SunroofCar(basic_car)
    sunroof_car.start()
    sunroof_car.stop()
    print(f"Cost of car with sunroof: ${sunroof_car.cost()}\n")

    # Add bulletproof to the car with sunroof
    bulletproof_sunroof_car = BulletproofCar(sunroof_car)
    bulletproof_sunroof_car.start()
    bulletproof_sunroof_car.stop()
    print(f"Cost of car with sunroof and bulletproof: ${bulletproof_sunroof_car.cost()}\n")