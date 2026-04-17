import json
from account import Account

class ATM:

    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                for pin, value in data.items():
                    self.accounts[pin] = Account(
                        value["name"],
                        pin,
                        value["balance"]
                    )
        except:
            pass

    def save_data(self):
        data = {}
        for pin, acc in self.accounts.items():
            data[pin] = {
                "name": acc.name,
                "balance": acc.balance
            }

        with open("data.json", "w") as f:
            json.dump(data, f)

    def create_account(self):
        name = input("Enter Name: ")
        pin = input("Create PIN: ")
        balance = float(input("Enter Balance: "))

        self.accounts[pin] = Account(name, pin, balance)
        self.save_data()

        print("Account Created")

    def login(self):
        pin = input("Enter PIN: ")

        if pin in self.accounts:
            return self.accounts[pin]
        else:
            print("Invalid PIN")
            return None

    def menu(self, acc):

        while True:
            print("\n1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Balance:", acc.check_balance())

            elif choice == "2":
                amt = float(input("Enter amount: "))
                print(acc.deposit(amt))
                self.save_data()

            elif choice == "3":
                amt = float(input("Enter amount: "))
                print(acc.withdraw(amt))
                self.save_data()

            elif choice == "4":
                break