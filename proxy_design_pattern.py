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