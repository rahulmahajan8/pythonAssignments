class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):
        amt = float(input("Enter Deposit Amount: "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter Withdraw Amount: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100


obj1 = BankAccount("Rahul", 10000)
obj2 = BankAccount("Amit", 5000)

print("Object 1")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest =", obj1.CalculateInterest())
obj1.Display()

print("\nObject 2")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest =", obj2.CalculateInterest())
obj2.Display()