class Checkbook:
    def __init__(self):
        """
        Function description: Initializes the Checkbook instance
        with an initial balance of 0.0.

        Parameters: None

        Returns: None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description: Adds the specified amount
        to the current balance and prints deposit details.

        Parameters: amount (float):
        The amount to deposit into the checkbook.

        Returns: None

        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description: Substracts the specified amount
        from the current balance if sufficient funds are available.
        If not, it notifies the user of insufficient funds.

        Parameters: amount (float):
        The amount to withdraw from the checkbook.

        Returns: None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description: Prints the current balance of the checkbook.

        Parameters: None

        Returns: None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function description: Runs the main loop of the checkbook application,
    allowing the user to perform actions like
    deposit, withdraw, check balance or exit the program.

    Parameters: None

    Returns: None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
