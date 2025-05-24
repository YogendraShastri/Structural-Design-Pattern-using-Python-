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
