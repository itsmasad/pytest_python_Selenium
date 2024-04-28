# In Python, the self keyword is used within class methods to refer to the instance of the class itself.
# It acts similarly to the this keyword in other programming languages like Java or C++. The self keyword
# is the first parameter of instance methods in Python, though it is not a reserved keyword and
# can technically be named anything (though self is the convention).

# Here's how self is used:

# Defining Methods:When defining methods within a class, the first parameter of each method should be self.
# This parameter refers to the instance of the class itself and allows the method to access and modify attributes of the instance.


# Define a class named MyClass
class MyClass:
    # Define the constructor method (__init__) which initializes the instance with a value x
    def __init__(self, x):
        # Assign the value of x to the instance attribute self.x
        self.x = x

    # Define a method named print_value which prints the value of self.x
    def print_value(self):
        print(self.x)

# Create an instance of MyClass with the value 5 and assign it to the variable obj
obj = MyClass(5)

# Call the print_value method of the obj instance which prints the value of self.x
obj.print_value()  # Output: 5

