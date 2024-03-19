# Encapsulation in Python is primarily achieved by using private and protected attributes and methods.
# However, Python doesn't enforce strict encapsulation like some other languages (e.g., Java),
# but it does provide conventions and mechanisms to achieve it. Here's an example demonstrating encapsulation:

# Define a class called BankAccount to represent a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        # Private attributes
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute
    
    # Public method to deposit money into the account
    def deposit(self, amount):
        self.__balance = self.__balance + amount  # Explicit addition instead of +=
        print(f"Deposit of ${amount} successful. New balance: ${self.__balance}")
    
    # Public method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance = self.__balance - amount  # Explicit subtraction instead of -=
            print(f"Withdrawal of ${amount} successful. New balance: ${self.__balance}")
    
    # Public method to get account balance
    def get_balance(self):
        return self.__balance

# Create an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Perform operations using public methods
account.deposit(500)   # Outputs: "Deposit of $500 successful. New balance: $1500"
account.withdraw(200)  # Outputs: "Withdrawal of $200 successful. New balance: $1300"
print(account.get_balance())  # Outputs: 1300