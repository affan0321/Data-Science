import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'

    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            if Path(self.database).exists():
                with open(self.database) as fs:
                    self.data = json.load(fs)
            else:
                self.data = []
        except Exception as err:
            self.data = []

    def update_data(self):
        with open(self.database, 'w') as fs:
            json.dump(self.data, fs, indent=4)

    def generate_account_number(self):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchr = random.choices("!@#$%^&*", k=1)
        acc_id = alpha + num + spchr
        random.shuffle(acc_id)
        return "".join(acc_id)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Invalid age or PIN"
        new_account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account_number(),
            "balance": 0
        }
        self.data.append(new_account)
        self.update_data()
        return True, new_account

    def find_user(self, acc_no, pin):
        return next((acc for acc in self.data if acc["accountNo"] == acc_no and acc["pin"] == pin), None)

    def deposit_money(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if user and 0 < amount <= 10000:
            user["balance"] += amount
            self.update_data()
            return True, user
        return False, None

    def withdraw_money(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)
        if user and user["balance"] >= amount:
            user["balance"] -= amount
            self.update_data()
            return True, user
        return False, None

    def show_details(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        return user

    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = self.find_user(acc_no, pin)
        if not user:
            return False
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            user["pin"] = new_pin
        self.update_data()
        return True

    def delete_account(self, acc_no, pin):
        user = self.find_user(acc_no, pin)
        if user:
            self.data.remove(user)
            self.update_data()
            return True
        return False
