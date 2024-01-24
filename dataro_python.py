import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
a = "test"
logger.info(f"this is an info message {a}")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=float)
args = parser.parse_args()


# Create a Python class representing a simplified ATM that dispenses Australian notes and coins.

# The first time the program runs, it should hold $1000 and have enough of each type of note and coin to service a number
# of different withdrawals. We will call this the 'balance'.
# When the program finishes, it should save the balance to a JSON file.
# When the program runs again, the class should load the most recent balance from a JSON file.
# The code should be called from the command line like so:

# python ATM.py
# There are three optional arguments:

# --amount, -a: The amount to withdraw as a decimal number
# --balance, -b: Print the current balance to the screen
# --refill, -r: Refill the ATM to hold the original setting of notes and coins.

# A user must supply one argument per invocation (never multiple at once).
# When the user is using the --amount argument, the ATM should return (to the screen) the smallest number of notes and/or coins to service the request and deduct these from its balance.

# I.e.

# % python ATM.py -a 150
# Withdrawing: 1x $100 Note, 1x $50 Note

# There are many scenarios where a user can input some amount argument that the ATM cannot service. Identify and handle at least 2 cases.
# Dataro [Python Test]: Rayhan + Dave (CTO)

from collections import OrderedDict
import sys
import json

import json

with open("atm.json") as f:
    data = json.load(f)


class ATM:
    def __init__(self, amount=1000, currency={}):
        self.amount = amount
        self.currency = currency
        sorted(self.currency, key=self.currency.get, reverse=True)
        self.amount_refiller = self.amount
        self.currency_refiller = self.currency

    def withdraw(self, withdraw_amount):
        # returns amounts of currency needed to fullfill the request
        # Withdraws amount with relevant currency, in smallest mount
        # looping through from biggest currency, to smallest currency
        withdraw_currency = []
        # Not sure if needs a keys(); will come ack to this
        for currency in self.currency.keys():
            currency = int(currency)
            if int(currency) <= withdraw_amount:
                withdraw_currency.append(currency)
                withdraw_amount -= int(currency)
                self.currency[currency] -= 1
        # output_message = f" Withdrawing: 1x ${} Note, 1x $50 Note"
        output_notes = {
            f"{withdraw_currency.count(curr)} x ${curr} Note"
            for curr in withdraw_currency
        }
        output_message = f" Withdrawing: {' '.join(output_notes)}"
        return output_message

    def balance_inquiry(self):
        return self.amount

    def refill(self):
        self.amount = self.amount_refiller
        self.currency = self.currency_refiller


print(data)
A = ATM(data["amount"], data["currency"])
transaction = A.withdraw(args.a)
# print(transaction)
balance = A.balance_inquiry()
print(balance)
A.refill
print(A.balance_inquiry())
