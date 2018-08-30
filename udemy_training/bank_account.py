class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):

        return f"\nAccount holder: {self.owner}\nBalance: {self.balance}\n"

    def deposit(self, amount):

        self.balance += amount

    def withdrawal(self, amount):

        if(amount > self.balance):
            print("\n\tNot enough money\n\tCurrent balance: {}\n"
                  .format(self.balance))
        else:
            self.balance -= amount


def another_operation():

    again = input(
        "Another operation? [ y / any key to exit ]: ").upper().strip()

    return again == "Y"


def main():

    client = Account('Bruno', 200)

    print("=" * 18)
    print("\tBank v1")
    print("=" * 18)
    print(str(client))

    while True:

        print("\nWhat do you want to do?")
        print("[ 1 ] > Deposit \n[ 2 ] > Withdrawals\n[ any ] exit")
        option = int(input("\n> ").strip())

        if option == 1:
            client.deposit(int(input("Deposit amount: ")))
        elif option == 2:
            client.withdrawal(int(input("Withdrawal amount: ")))

        if not another_operation():
            break

    print("\n\tEND")
    print("=" * 18)
    print(str(client))
    print("=" * 18)


if __name__ == '__main__':
    main()
