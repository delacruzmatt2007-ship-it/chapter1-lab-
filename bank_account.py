"""
ITECC04 Data Structures & Algorithms
Laboratory 1, Task B: the BankAccount class

The simpler of the two tasks. Same rules as Task A: the data stays private,
the operations are public, and the class refuses anything that would break
its own rule.

The rule this class protects: the balance may never go below zero.

Fill in one step at a time and run the tests after each one:

    python test_bank_account.py

Step 1  __init__       store the owner and the opening balance, privately
Step 2  get_balance    return the balance
Step 3  deposit        add to the balance, refusing zero or negative amounts
Step 4  withdraw       subtract, refusing anything that would overdraw
Step 5  __str__        return text such as 'Juan: 1500.00'
"""


class BankAccount:
    """An account that will not let itself go negative."""

    def __init__(self, owner, balance=0):
        # Step 1
        # - raise ValueError if balance is negative
        # - store the owner in self._owner
        # - store the balance in self._balance
        raise NotImplementedError("Step 1: store the owner and the opening balance")

    def get_balance(self):
        # Step 2
        # Return the stored balance. Callers use this instead of reaching
        # into self._balance themselves.
        raise NotImplementedError("Step 2: return the balance")

    def deposit(self, amount):
        # Step 3
        # - raise ValueError if amount is zero or negative
        # - otherwise add it to the balance
        raise NotImplementedError("Step 3: add to the balance, after checking the amount")

    def withdraw(self, amount):
        # Step 4
        # - raise ValueError if amount is zero or negative
        # - raise ValueError if amount is larger than the balance
        # - otherwise subtract it from the balance
        raise NotImplementedError("Step 4: subtract, but never below zero")

    def __str__(self):
        # Step 5
        # Return the owner, a colon, and the balance to two decimal places,
        # for example: Juan: 1500.00
        raise NotImplementedError("Step 5: return 'owner: balance'")


if __name__ == "__main__":
    print("BankAccount starter. Run: python test_bank_account.py")
