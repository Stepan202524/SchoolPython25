
class BankAcc:
    def __init__(self, own, bal=0):
        self._own = own
        self._bal = bal

    def get_bal(self):
        return self._bal

    def deposit(self, amount):
        if amount > 0:
            self._bal += amount
            print(f'Popolnenie na : {amount}')
        else:
            print(f'Nel`zya vnesti otricatelnuyu summu')

    def withdr(self, amount):
        if 0 < amount <= self._bal:
            self._bal -= amount
            print(f'Snyato : {amount}')
        else:
            print(f'!Nedostatochno sredst na chetu!')

client1 = BankAcc('Petr')
client1.deposit(500)
client1.withdr(400)
print('Ostatok: ', client1.get_bal())