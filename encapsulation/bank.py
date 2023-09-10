class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__initial_balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__initial_balance
    
    def deposit(self, deposit_amount):
        # It should accept an amount as input and add it to the account balance.
        self.__initial_balance += deposit_amount
    
    
    def withdraw(self, withdraw_amount):
        """_summary_
        If there are not enough funds it should raise a ValueError exception with the message "Insufficient funds".
        Otherwise, it should deduct the amount from the balance.
        """        
        if self.__initial_balance < withdraw_amount:
            raise ValueError("Insufficient funds")
        self.__initial_balance -= withdraw_amount
             

# don't touch below this line


def test(account_number, initial_balance, deposit_amount, withdraw_amount):
    account = BankAccount(account_number, initial_balance)
    print(f"Account number: {account.get_account_number()}")
    print(f"Initial balance: {account.get_balance():.2f}")
    account.deposit(deposit_amount)
    print(
        f"After depositing ${deposit_amount:.2f}, balance: ${account.get_balance():.2f}"
    )
    try:
        account.withdraw(withdraw_amount)
        print(
            f"After withdrawing ${withdraw_amount:.2f}, balance: ${account.get_balance():.2f}"
        )
    except ValueError as e:
        print(
            f"Failed to withdraw ${withdraw_amount:.2f}, balance: ${account.get_balance():.2f}"
        )
        print(f"Error: {e}")
    print("=====================================")


def main():
    test("1234567890", 100.0, 50.0, 75.0)
    test("0987654321", 500.0, 100.0, 200.0)
    test("1234567890", 100.0, 50.0, 200.0)


main()
