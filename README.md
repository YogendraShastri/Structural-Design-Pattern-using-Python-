# Structural Design Patterns using Python
Let's explore structural design patterns, understand which patterns fall under this category, and look at Python code examples for each one.

## What is Structural Design Patterns ?
Structural Design Patterns provide solutions for organizing classes and objects in software design to create larger, functional and reliable structures. These patterns simplify object relationships, making the codebase more efficient, adaptable, and easier to maintain. In Simple word Creational Design Pattern more focuses on object creation while Structural Design Pattern focuses on **"How Classes & Objects are structured together, and how we can structure them so that it became more efficient, reliable and easy to maintain."**

By applying structural patterns, developers can better handle complex hierarchies, promote code reuse, and build scalable system architectures.

## Types of Structural Design Patterns : 
* Decorator Pattern
* Adapter Pattern
* Proxy Pattern
* Facade Pattern
* Bridge Pattern
* Composite Pattern
* Flyweight Pattern

### Decorator Pattern :
The Decorator Design Pattern is a type of structural pattern that allows you to add new behaviors to individual objects—either at runtime or compile time—without changing the behavior of other objects of the same class.

Put simply, it lets you “wrap” objects with additional functionality while keeping their original structure untouched. This approach is especially useful when you need to extend an object's features in a flexible, scalable, and reusable way.

**Structure** :
![image](https://github.com/user-attachments/assets/c5ed5b58-9d24-4a21-89b6-2bc1a1295668)

**Example** : 
```python
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

Output : 
Starting basic Car
Stoping the basic Car
Cost of basic car: $20000

Starting the SunRoof Car
Shuting the SunRoof Car
Cost of car with sunroof: $23000

Starting the Bulletproof Car
Shuting theBulletproof Car
```

*How It Works*:
- When you create a SunroofCar instance, you pass a Car object (e.g., BasicCar) to its constructor via CarDecorator’s initialization.
- The self._car attribute in SunroofCar stores this BasicCar instance.
- The cost() method in SunroofCar first calls self._car.cost(), which invokes the cost() method of the wrapped BasicCar object (returning $20,000).
- Then, it adds $3000 to the result, giving the total cost.

### Adapter Pattern :
The Adapter Design Pattern is a structural pattern that acts like a bridge between two incompatible interfaces.It translates one interface into another so that classes can work together without changing their existing code.

for example,Imagine you're traveling to a country where the power sockets are different. You use a plug adapter to connect your charger (which doesn’t fit natively) to the local socket.

**Structure** :
![image](https://github.com/user-attachments/assets/aa622e9c-406b-43ad-bc8b-d6af59fc6cae)

**Code** :
```python
# Target interface
class IndianSwitchBoard:
    def provide_power_230v(self):
        pass

# Adaptee class (different interface)
class USPhoneCharger:
    def charge_110v(self):
        return "Charging phone with 110V power"

# Adapter class
class IndianPortAdapter(IndianSwitchBoard):
    def __init__(self, us_phone_charger):
        self.us_phone_charger = us_phone_charger

    def provide_power_230v(self):
        # Simulate converting 230V to 110V for the US charger
        print("Adapting 230V Indian power to 110V for US charger...")
        return self.us_phone_charger.charge_110v()

# Usage
if __name__ == "__main__":
    # Create a USPhoneCharger instance
    us_charger = USPhoneCharger()

    # Create an adapter to make USPhoneCharger compatible with IndianSwitchBoard
    adapter = IndianPortAdapter(us_charger)

    # Use the adapter with the Indian switchboard
    print(f"Power status: {adapter.provide_power_230v()}")

Output:
```

Adapting 230V Indian power to 110V for US charger...
Power status: Charging phone with 110V power

**How it works** :
- Adapter wraps the USPhoneCharger to make it compatible with IndianSwitchBoard.
- Adapter translates the provide_power_230v() call into charge_110v().
- Original charger stays unchanged, while the adapter handles the conversion.

### Proxy Pattern :
We all know what a proxy means in real life — like back in school or college when we gave proxy attendance for a friend. If the teacher called out their name and they weren’t present, we’d reply ‘Yes Ma’am’ on their behalf.

Similarly, in software, the Proxy Design Pattern involves using a substitute object to act on behalf of the real one — especially when creating the actual object is resource-intensive (like loading a large database or performing a heavy computation).

The proxy controls access and can add extra logic like caching, logging, or access control — without directly invoking the real object every time

**Structure**
![image](https://github.com/user-attachments/assets/97048867-a71c-4c44-81b5-a2c5e5b4186c)


**Code**: 
```python
from abc import ABC, abstractmethod
import logging
import time

# Interface
class ClassInterface(ABC):
    @abstractmethod
    def operations(self):
        pass


# Real Subject
class RealClass(ClassInterface):
    def operations(self):
        print("RealClass: Performing complex IO operation")
        # Simulate a time-consuming operation
        time.sleep(1)

# Proxy
class ProxyClass(ClassInterface):
    def __init__(self):
        # Lazy initialization: RealClass is created only when needed
        self._real_class = None

    def _get_real_class(self):
        # Initialize RealClass lazily
        if self._real_class is None:
            logging.info("ProxyClass: Initializing RealClass")
            self._real_class = RealClass()
        return self._real_class

    def operations(self):
        # Add logging before the operation
        logging.info("ProxyClass: Logging before operation")

        # Delegate to RealClass
        self._get_real_class().operations()

        # Add logging after the operation
        logging.info("ProxyClass: Logging after operation")

    def logging(self):
        # Additional method to demonstrate proxy-specific behavior
        logging.info("ProxyClass: Performing additional logging tasks")


# Client code
if __name__ == "__main__":
    # Create proxy instance
    proxy = ProxyClass()

    # Perform operations via proxy
    print("Client: Executing operations through ProxyClass")
    proxy.operations()

    # Call additional proxy-specific method
    proxy.logging()

Output : 

Client: Executing operations through ProxyClass
RealClass: Performing complex IO operation
```

**How it works**: 
- Client side we create the object of proxy class but client do not know.
- By Lazy initialization we create object of main class from proxy.
- Proxy Class interact with Main class rather than client class.

### Facade Pattern : 
The Facade Design Pattern is a structural design pattern that provides a simplified, unified interface to a complex subsystem.It hides the complexity of the system by encapsulating it behind a single entry point. This pattern is commonly used to improve usability and reduce dependencies between clients and the underlying subsystems.

In simple terms, the Facade Design Pattern is like a refactoring technique that simplifies a complex system and makes it easier to use.Think of it like going to a restaurant: as a customer (client), you don’t need to worry about how your food is ordered, prepared, or served. You just talk to the waiter. In this analogy:

You are the client.
The waiter is the facade — the simplified interface.
The restaurant kitchen, which has different departments like order processing, cooking, and serving, represents the complex subsystem.
The Facade Pattern helps hide these complex parts and gives you a smooth, clean way to interact with everything.

**Structure**
![image](https://github.com/user-attachments/assets/06ab9881-f880-4ae1-9629-c4a16f3f5a60)

**Code** : 
```python
# Facade Design Pattern
# Subsystem 1
class PlaceOrder:
    def place_order(self, order):
        print(f"Customer Placed the Order for : {order}")

# Subsystem 2
class PrepareFood:
    def prepare_food(self, order):
        print(f"{order} is being prepared")

# Subsystem 3
class ServeOrder:
    def serve_order(self, order):
        print(f"{order} Prepared, Order Served")

# Facade:
class Waiter:
    def __init__(self):
        self.po = PlaceOrder()
        self.pf = PrepareFood()
        self.so = ServeOrder()

    def waiter_takeorder(self, order):
        self.po.place_order(order)
        self.pf.prepare_food(order)
        self.so.serve_order(order)


if __name__ == "__main__":
    cust1 = Waiter()
    cust1.waiter_takeorder("Pasta")

Output : 

Customer Placed the Order for : Pasta
Pasta is being prepared
Pasta Prepared, Order Served
```

**How it Works**:
- There are three subsystems (subsystem1, subsystem2, subsystem3).
- Waiter class creates the objects for each sub system class.
- By Creating the object of the waiter class we can access all three subsystem classes as Waiter class act as facade.

### Bridge Pattern :
The **Bridge Design Pattern** is a structural pattern that decouples an abstraction from its implementation so that the two can vary independently.

It’s useful when you want to separate an object's interface from its implementation, allowing them to evolve separately without affecting each other. in simple words The bridge pattern allows the Abstraction and the Implementation to be developed independently and the client code can access only the Abstraction part without being concerned about the Implementation part, for Example : 

You have different remotes (like basic remote, smart remote), and they can control different devices (like TV, Radio, Projector).
Instead of creating separate classes for every combination (e.g., SmartTVRemote, BasicRadioRemote, etc.), the Bridge Pattern helps you separate Remotes (Abstraction) from Devices (Implementation).

**Structure**:
![image](https://github.com/user-attachments/assets/db98bb95-4e62-4c02-895b-25f70ff546de)

**Code** : 
```python
# """ 
#                       [ implementation ]                                    [ Abstraction ]
#
#                             Device                                               Remote
#                 { PowerOn, PowerOff, set_channel}  --------------  { toggle_power, change_chennel}
#                        /             \                                      /               \ 
#                       /               \                                    /                 \ 
#                  TV(Device)           Radio(Device)                SmartRemote(Remote)     BasicRemote(Remote)
# """

from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    def change_channel(self, channel):
        pass

class TV(Device):

    def power_on(self):
        print("TV is Powering ON")

    def power_off(self):
        print("TV is powering OFF")

    def change_channel(self, channel):
        print(f"TV is set to channel : {channel}")

class Radio(Device):

    def power_on(self):
        print("Radio is powering on")
    
    def power_off(self):
        print("Radtio is powering off")

    def change_channel(self, channel):
        print(f"Radio channel set to {channel}")

#abstraction
class Remote(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def toggle_power(self, power):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

class SmartRemote(Remote):

    def toggle_power(self, power):
        if power == "ON":
            return f"Smart Remote : {self.device.power_on()}"
        else:
            return f"Smart Remote : {self.device.power_off()}"
    
    def set_channel(self, channel):
        return f"SmartRemote : {self.device.change_channel(channel)}"
    
    def subscription(self):
        print("Use Hotstar, Sony liv  or Netflix")
    
class BasicRemote(Remote):

    def toggle_power(self, power):
        if power == "On":
            return f"Basic Remote : {self.device.power_on()}"
        else:
            return f"Basic Remote : {self.device.power_off()}"
    
    def set_channel(self, channel):
        return f"Basic Remote : {self.device.change_channel(channel)}"


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    tv_remote = SmartRemote(tv)
    radio_remote = BasicRemote(radio)
    
    tv_remote.toggle_power("ON")
    tv_remote.set_channel(23)
    tv_remote.subscription()
    tv_remote.toggle_power("OFF")

    print("\n")
    radio_remote.toggle_power("ON")
    radio_remote.set_channel(94.6)
    radio_remote.toggle_power("OFF")

```
**Output**
```python
TV is Powering ON
TV is set to channel : 23
Use Hotstar, Sony liv  or Netflix
TV is powering OFF


Radtio is powering off
Radio channel set to 94.6
Radtio is powering off
```

**How it Works**:
- The pattern defines an abstraction (e.g., Remote) that contains a reference to an implementation interface (e.g., Device)
- The Remote (abstraction) and Device (implementation) hierarchies are independent, allowing new remotes or devices to be added without modifying the other hierarchy.

### Composite Pattern:
The **Composite Design Pattern** is a structural pattern that allows you to compose objects into tree-like structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly, enabling recursive processing of complex structures.

In simple word Composite means made up of variours elements,  there are two major components one is part (leaf)  and another is whole, if in an orgnization there is a L7 manager who manages 2 L6 managers and 5 L5 Employees than, all the Employees are considered as Part or Leaf, but Managers will be considered as Whole, as each L6 Manager, Manages the team of 2 L4 Employees. Lets see Diagram :

**Key Components :** 
* Client
* Component (Interface)
* Leaf or Part
* Composite or Whole

**Structure**:
![image](https://github.com/user-attachments/assets/97968ac6-7d57-46ac-bb35-d59a397b81ec)

The core idea behind the Composite Design Pattern revolves around the ability to treat individual objects and composites uniformly, especially with operations like:
**Add(component)** – Add a part (leaf or composite) to a composite.
**Remove(component)** – Remove a part from a composite.
**Operation()** – Perform an operation (e.g., display, calculate) on both individual objects and groups.

**Code** : 
```python
from abc import ABC, abstractmethod

# Interface
class Employee(ABC):

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def emp_details(self):
        pass


# Leaf - Developer
class Developer(Employee):
    def __init__(self, name):
        self.name = name

    def do_work(self):
        print(f"{self.name} is doing Development Task")

    def emp_details(self):
        print(f"Name: {self.name}, Position: Developer")


# Leaf - Tester
class Tester(Employee):
    def __init__(self, name):
        self.name = name

    def do_work(self):
        print(f"{self.name} is doing Testing Task")

    def emp_details(self):
        print(f"Name: {self.name}, Position: Tester")


# Composite - Manager
class Manager(Employee):
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_employee(self, emp: Employee):
        self.team.append(emp)

    def remove_employee(self, emp: Employee):
        self.team.remove(emp)

    def do_work(self):
        print(f"{self.name} is managing the team:")
        for emp in self.team:
            emp.do_work()

    def emp_details(self):
        print(f"Name: {self.name}, Position: Manager, Team Members:")
        for emp in self.team:
            emp.emp_details()


# Client
if __name__ == "__main__":
    dev1 = Developer("Raj")
    dev2 = Developer("Shyam")
    tester1 = Tester("Devesh")

    manager = Manager("Yogi")
    manager.add_employee(dev1)
    manager.add_employee(dev2)
    manager.add_employee(tester1)

    manager.emp_details()
    print("\n--- Work in progress ---\n")
    manager.do_work()
```

**Output**
```python
Name: Yogi, Position: Manager, Team Members:
Name: Raj, Position: Developer
Name: Shyam, Position: Developer
Name: Devesh, Position: Tester

--- Work in progress ---

Yogi is managing the team:
Raj is doing Development Task
Shyam is doing Development Task
Devesh is doing Testing Task

Process finished with exit code 0
```
**How it Works**:
* Manager acts as a composite and holds a team of Employee objects.
* Developer and Tester are leaves.
* The client code can treat both individuals and groups uniformly using the Employee interface.






