"""
ITECC04 Data Structures & Algorithms
Laboratory 1: checks for the BankAccount class

Run this after every step:   python test_bank_account.py

Checks you have not written yet report "not written yet" instead of crashing,
so you can run this from the very start and watch the list turn green.
Checks 5, 6, and 7 are supposed to be refused. A class that accepts them has
not protected its own rule.
"""

from bank_account import BankAccount

passed = 0
total = 7


def report(number, status, description, detail):
    """Print one result line, aligned in four columns."""
    print(f"{number}. {status:<16}{description:<40}{detail}")


def check(number, description, expected, produce):
    """Run one check and print a single line for it."""
    global passed
    try:
        actual = produce()
    except NotImplementedError as missing:
        report(number, "not written yet", description, str(missing))
        return
    except Exception as error:
        report(number, "ERROR", description, f"{type(error).__name__}: {error}")
        return
    if str(actual) == str(expected):
        passed += 1
        report(number, "pass", description, f"got {actual}")
    else:
        report(number, "FAIL", description, f"expected {expected}, got {actual}")


def refuses(action):
    """Return 'refused' if the class rejects the action, 'accepted' if not."""
    def run():
        try:
            action()
        except ValueError:
            return "refused"
        except NotImplementedError:
            raise
        return "accepted"
    return run


def after_deposit():
    account = BankAccount("Juan", 1000)
    account.deposit(500)
    return account.get_balance()


def after_withdraw():
    account = BankAccount("Juan", 1000)
    account.withdraw(250)
    return account.get_balance()


check(1, "a new account keeps its opening balance", 1000,
      lambda: BankAccount("Juan", 1000).get_balance())
check(2, "depositing 500 into 1000 gives 1500", 1500, after_deposit)
check(3, "withdrawing 250 from 1000 gives 750", 750, after_withdraw)
check(4, "the account prints owner and balance", "Juan: 1500.00",
      lambda: BankAccount("Juan", 1500))
check(5, "overdrawing is refused", "refused",
      refuses(lambda: BankAccount("Juan", 1000).withdraw(5000)))
check(6, "a negative deposit is refused", "refused",
      refuses(lambda: BankAccount("Juan", 1000).deposit(-100)))
check(7, "a negative opening balance is refused", "refused",
      refuses(lambda: BankAccount("Juan", -50)))

print(f"\n{passed} of {total} checks passing.")
print("The balance never went below zero, and no test reached into _balance "
      "directly. That is encapsulation doing its job.")
