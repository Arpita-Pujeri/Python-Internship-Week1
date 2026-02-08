# Parent class
class Payment:
    def pay(self):
        print("Payment is being processed")


# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")


# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")


# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")


# Creating objects and calling pay() method
payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()

payment.pay()
gpay.pay()
phonepe.pay()
card.pay()
