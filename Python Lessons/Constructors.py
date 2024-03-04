# Constructors

# It is a special method within a class that gets automatically called when an object or instance of the class is created.
# It is used to initialize the attributes of the object.
# It is writen with __init__
# The 'self' keyword is used within the methods of a class to refer to the instance of 
# the class itself. It is a convention and not a reserved keyword, 
# but it is widely adopted and recommended for clarity.



class faculty:
    def putdata(self):
        self.id=int((input("Enter Faculty ID")))
        self.name=input("Enter Name")
        self.salary=float(input("Enter Salary"))
    def display(self):
        print(f'Faculty ID : {self.id}')
        print(f'Faculty Name :{self.name}')
        print(f'Faculty Salary : {self.salary}')

a = faculty()
a.putdata()
a.display()



class faculty:
    def __init__(self):
        self.id=int((input("Enter Faculty ID")))
        self.name=input("Enter Name")
        self.salary=float(input("Enter Salary"))
    def display(self):
        print(f'Faculty ID : {self.id}')
        print(f'Faculty Name :{self.name}')
        print(f'Faculty Salary : {self.salary}')

a = faculty()
# Here we don't need to call init, it will run automatically when an object is called or created
a.display()




class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an instance of MyClass
obj = MyClass(10, 20)

# Access the instance variables
print(obj.x)  # Output: 10
print(obj.y)  # Output: 20
