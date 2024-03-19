class Phone:
    # Define a method to produce a generic phone ring sound
    def phone_ring(self, ringtone="Ring Ring Ring"):
        print(ringtone)
    
    # Define a method to indicate a call connection
    def call(self):
        print("Call Has Been Connected")
    
    # Define a method to indicate a message has been sent
    def message(self):
        print("Message Has Been Sent")

# Create an instance of Phone
phone = Phone()

# Call the phone_ring method with different parameters
# The phone_ring method behaves differently based on the number of parameters passed
# This demonstrates method overloading-like behavior
phone.phone_ring()               # Outputs: "Ring Ring Ring" (default ringtone)
phone.phone_ring("Tu Tu Tu")     # Outputs: "Tu Tu Tu"
phone.phone_ring("iPhone Ring")  # Outputs: "iPhone Ring"
