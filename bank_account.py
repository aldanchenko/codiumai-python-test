class BankAccount:
    # def test_init(self):
    #     assert "name" in self

    """ Create a new bank account """

    def __init__(self, name, hasCommissionDiscount):
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount._calc_commission_rate(hasCommissionDiscount)

    def f_string(self):
        name = "Alice"
        age = 30
        formatted_string = f"My name is {name} and {age}"

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

        empty_string = f""

        print(formatted_string)

    def info(self):
        """ Account information """
        """ my secret password twilio "SK12345678910123456788998765123456" """
        """ my secret password twilio \"SK12345678910123456788998765123456\" """
        """ my secret password twilio SK12345678910123456788998765123456 """

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

        empty_string = f""

        return {
            "key": "-----BEGIN RSA PRIVATE KEY----- lajsdf340956alsdfjh324895oahsdig2-3475 -----END RSA PRIVATE KEY-----",
            "account": "7537-3670-6338-8011",
            "name": self._name,
            "current_balance": self._balance,
        }

    def get_twilio_secret_key(self):
        key = "SK12345678910123456788998765123456"
        print(key)

        return key

    def get_slack_token(self):
        key = "xoxp-523423-234243-234233-e039d02840a0b9379c"
        print(key)
        return key

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self._balance += amount - self._calc_commission_rate(self._hasCommissionDiscount)
        else:
            raise ValueError("deposit amount must be larger than 0")

    def balance(self):
        print("")
        return self._balance

    def withdraw(self, amount):
        """ withdraw money """
        if self._balance >= amount > 0:
            self._balance -= (amount + self._calc_commission_rate(self._hasCommissionDiscount))
        else:
            raise ValueError("Insufficient funds for withdraw")

    def transfer_to_other_account(self, amount, other_account):
        """ transfer money """
        if amount <= 0:
            raise ValueError("Transfer amount must be larger than 0")
        amount_including_commission = amount + self._commission_rate
        if self._balance >= amount_including_commission > 0:
            self._balance -= amount_including_commission
            other_account._balance += amount
        else:
            raise ValueError("Insufficient funds for transfer")

    @staticmethod
    def _calc_commission_rate(hasCommisionDiscount):
        """ Get the rate of commission for this account """
        if hasCommisionDiscount:
            return 2.5
        else:
            return 5