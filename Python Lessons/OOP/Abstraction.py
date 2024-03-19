# Abstraction in Python involves hiding the complex implementation details and showing
# only the essential features of an object. This is typically achieved through abstract
# classes and methods, which are not meant to be instantiated directly but serve as a
# blueprint for other classes to inherit from. Here's an example demonstrating abstraction:

from abc import ABC, abstractmethod  # Import the ABC module and abstractmethod decorator

# Define an abstract class called Mouse
class Mouse(ABC):
    # Abstract method for clicking
    @abstractmethod
    def click(self):
        pass  # Placeholder statement to indicate no implementation, must be overridden in subclasses

# Define a subclass WirelessMouse which inherits from Mouse
class WirelessMouse(Mouse):
    def __init__(self, brand):
        self.brand = brand  # Initialize the brand attribute
    
    # Implementing the abstract method to perform a click for WirelessMouse
    def click(self):
        print(f"{self.brand} Wireless Mouse: Click")  # Print a message indicating a click with the brand of the mouse

# Define a subclass WiredMouse which also inherits from Mouse
class WiredMouse(Mouse):
    def __init__(self, brand):
        self.brand = brand  # Initialize the brand attribute
    
    # Implementing the abstract method to perform a click for WiredMouse
    def click(self):
        print(f"{self.brand} Wired Mouse: Click")  # Print a message indicating a click with the brand of the mouse

# Create instances of WirelessMouse and WiredMouse
wireless_mouse = WirelessMouse("Logitech")  # Instantiate a WirelessMouse object with brand "Logitech"
wired_mouse = WiredMouse("Microsoft")      # Instantiate a WiredMouse object with brand "Microsoft"

# Click with both types of mice
wireless_mouse.click()  # Outputs: "Logitech Wireless Mouse: Click"
wired_mouse.click()     # Outputs: "Microsoft Wired Mouse: Click"
