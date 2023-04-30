class Wallet:
    # First thing to run when making new class
    # Outline required user-provided input values here
    # Parameters with default assigned become optional
    def __init__(self, initial_amount=0):
        # Save user-provided initial_amount as an attribute
        # Self refers to whatever object working with
        self.balance = initial_amount

    # Spend cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return "not enough money"
        else: 
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"new balance of: {self.balance}"

    # __repr__ method
    # Cahnges how the 'object' looks when it is printed out
    # The resence of the self keyword alls one to access or 
    # modify class attributes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"


if __name__ == '__main__':
    wallet1 = Wallet(50)
    print(wallet1)
    print(wallet1.balance)



