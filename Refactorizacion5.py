class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BitcoinPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")


payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BitcoinPayment()
]


for payment in payments:
    payment.process_payment(100)