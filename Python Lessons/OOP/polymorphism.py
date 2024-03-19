# Define a base class called Phone
class Phone:
    # Define a method to produce a generic phone ring sound
    def phone_ring(self):
        print("Ring Ring Ring")
    
    # Define a method to indicate a call connection
    def call(self):
        print("Call Has Been Connected")
    
    # Define a method to indicate a message has been sent
    def message(self):
        print("Message Has Been Sent")

# Define a subclass Samsung which inherits from Phone
class Samsung(Phone):
    # Override the phone_ring method to produce a Samsung-specific ring sound
    def phone_ring(self):
        print("Tu Tu Tu")

# Define another subclass IPhone which also inherits from Phone
class IPhone(Phone):
    # Override the phone_ring method to produce an iPhone-specific ring sound
    def phone_ring(self):
        print("iPhone Ring")

# Create instances of generic phone
generic_phone = Phone()
# Create instances of Samsung and iPhone
samsung_phone = Samsung()  # Creating an instance of Samsung phone
iphone_phone = IPhone()     # Creating an instance of iPhone phone

# Call the phone_ring method for both instances
# The phone_ring method behaves differently for each object
# This is polymorphism - the same method name is used, but behaves differently depending on the object
generic_phone.phone_ring()  # Outputs: "Ring Ring Ring"
samsung_phone.phone_ring()  # Outputs: "Tu Tu Tu"
iphone_phone.phone_ring()   # Outputs: "iPhone Ring"
