# In Python, the self keyword is used within class methods to refer to the instance of the class itself.
# It acts similarly to the this keyword in other programming languages like Java or C++. The self keyword
# is the first parameter of instance methods in Python, though it is not a reserved keyword and
# can technically be named anything (though self is the convention).

# Here's how self is used:

# Defining Methods:When defining methods within a class, the first parameter of each method should be self.
# This parameter refers to the instance of the class itself and allows the method to access and modify attributes of the instance.


class MyClass:
    def __init__(self, x):
        self.x = x

    def print_value(self):
        print(self.x)

obj = MyClass(5)
obj.print_value()  # Output: 5
