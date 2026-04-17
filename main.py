from atm import ATM

def main():
    atm = ATM()

    while True:
        print("\n===== ATM SYSTEM =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            atm.create_account()

        elif choice == "2":
            user = atm.login()
            if user:
                atm.menu(user)

        elif choice == "3":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()