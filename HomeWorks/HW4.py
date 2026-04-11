rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, odj):
        # Ман ин ҷо кодро каме тоза кардам, то хато набошад
        return Money(self.amount + odj.amount, self.currency)