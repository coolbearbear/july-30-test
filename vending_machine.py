from dataclasses import dataclass, field
import coins
import products

#creating our own exception
class InsufficientFunds(Exception):
    pass


@dataclass
class VendingMachine:
    inserted_coins: list = field(default_factory=list)
    purchases: list = field(default_factory=list)

    def insert_coin(self, coin):
        if not isinstance(coin, coins.Coin):
            raise ValueError

        self.inserted_coins.append(coin)

    def buy_product(self, product):
        if not issubclass(product, products.Product):
            raise ValueError
        balance = self.get_balance() #calling get_balance
        if balance < product.price:
            raise InsufficientFunds

        obj = product()
        self.purchases.append(obj)
        return obj

    def get_balance(self):
        balance = 0
        for coin in self.inserted_coins: #this coin is local so its ok to use
            #balance = balance + coin.value
            balance += coin.value

        for product in self.purchases:
            balance -= product.price

        return balance
