class Bank:
    Bank_name = "Meezan Bank" # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.Bank_name = name
        return name

print("Bank name",Bank.Bank_name)
a=Bank.change_bank_name("Habib Bank")
print(a)