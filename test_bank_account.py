from bank_account import BankAccount

import unittest


class TestBankAccount(unittest.TestCase):

    def test_f_strings(self):
        name = "Alice"
        age = 30
        formatted_string = f"My name is {name} and {age}"
        print(formatted_string)

        a = 5
        b = 10
        formatted_string = f"The sum of {a} and {b} is {a + b}."

        person = {"name": "Bob", "age": 25}
        formatted_string = f"Person's name is {person['name']} and age is {person['age']}"

        pi = 3.141592653589793
        formatted_string = f"Value of pi: {pi:.2f}"

        from datetime import datetime
        current_date = datetime.now()
        formatted_string = f"Current date and time: {current_date:%Y-%m-%d %H:%M:%S}"

        a = 3
        b = 4
        formatted_string = f"The result is {a + {b * 2} }."

        path = r"C:\Users\Username\Documents"
        formatted_string = f"Path: {path}"

        value = 42
        formatted_string = f"{{value}}"

        formatted_string = f"Hello, {name}"

        empty_string = f"{name}"

    def test_deposit_positive_amount(self):
        name = "Alice"
        age = 30
        formatted_string = f"My name is {name}"
        print(formatted_string)

        account = BankAccount("John", False)
        initial_balance = account.balance()
        amount = 100
        account.deposit(amount)
        new_balance = account.balance()
        self.assertEqual(new_balance,
                         initial_balance + amount - account._calc_commission_rate(account._hasCommissionDiscount))

    def test_dictionary_contains_keys(self):
        account = BankAccount("John Doe", False)
        result = account.info()
        assert "key" in result
        assert "account" in result
        assert "name" in result
        assert "current_balance" in result

    def test_returns_dictionary_with_account_information(self):
        account = BankAccount("John Doe", False)
        result = account.info()
        assert isinstance(result, dict)

    def test_account_name_is_empty_string(self):
        account = BankAccount("", False)
        result = account.info()
        assert result["name"] == ""

    def test_account_balance_is_negative(self):
        account = BankAccount("John Doe", False)
        account._balance = -100
        result = account.info()
        assert result["current_balance"] == -100