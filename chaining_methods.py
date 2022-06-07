class User:
    def __init__(self, name):
        self.name = name
        # account balance already has a default value, so we do not have to include that as a parameter. If the default wasn't zero, we would have to include it as a parameter.
        self.account_balance = 0
    # deposit method
    def make_deposit(self, amount):
        # takes an argument that is the amount of the deposit
        self.account_balance += amount
        # the specific user's account increases by the amount of the value received
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

# line below: creating an instance of User called sarah.
sarah = User("Sarah Perez")
catherine = User("Catherine Smith")
sally = User("Sally Miller")

# Looking at the parameters in make_deposit and make_withdrawal, we are passing sarah (what sarah is equal to) in as an argument for self and passing the numeric value in parentheses as an argument for amount
sarah.make_deposit(325).make_deposit(642).make_deposit(122).make_withdrawl(236).display_user_balance()

catherine.make_deposit(27).make_deposit(42).make_withdrawl(6).make_withdrawl(17).display_user_balance()

sally.make_deposit(657).make_withdrawl(97).make_withdrawl(46).make_withdrawl(22).display_user_balance()