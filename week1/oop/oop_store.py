# OOP
from copy import deepcopy


class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        self.bills = [100, 50, 20, 10, 5, 2, 1]
        self.totalmoney = 0

    def take_money(self, money_taken):
        for i in money_taken:
            self.money[i] = self.money[i] + money_taken[i]
        print(self.money)

    def total(self):
        self.totalmoney = 0
        for i in self.money:
            self.totalmoney = self.totalmoney + self.money[i]*i
        print(self.totalmoney)
        return self.totalmoney

    def can_withdraw_money(self, amount_of_money):
        canwithdraw = deepcopy(self.money)
        if self.total() < amount_of_money:
            print("false")
            return False
        else:
            self.subtracted = 0
            i = 0
            originalamount = amount_of_money
            while i < len(self.bills) and amount_of_money > 0:

                #print("hmm", self.bills[i])
                if canwithdraw[self.bills[i]] > 0 and amount_of_money >= self.bills[i]:
                    canwithdraw[self.bills[i]] -= 1
                    amount_of_money -= self.bills[i]
                    self.subtracted += self.bills[i]
                    continue
                else:
                    i += 1
                    continue
            if self.subtracted == originalamount:
                print ("true")
                return True
            else:
                print("false")
                print(amount_of_money, self.subtracted, canwithdraw)
                return False


class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        print(self.final_price - self.stock_price)
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.total = 0

    def load_new_products(self, prod, count):
        #self.products[prod.name] = (prod, count)
        self.products[prod] = count

    def list_products(self):
        for i, j in self.products.items():
            print(i.name, ":", j)

    def sell_products(self, prod):

        for i in self.products.items():
            # print(prod, self.products[i].name)
            if not isinstance(i[0], prod.__class__):
                print("item out of stock!")
                # print(i[0].__class__, prod.__class__) # debug
                return False
            elif i[1] < 1:
                print("item out of stock")
                return False
            else:
                print("item sold")
                self.products[prod] -= 1
                self.total += prod.profit()
                return True

    def total_profit(self):
        print(self.total)
        return self.total


# my_cash_desk = CashDesk()
# my_cash_desk.take_money({100: 10, 20: 2})
# my_cash_desk.take_money({100: 1, 20: 1, 10: 2})
# my_cash_desk.total()
# my_cash_desk.can_withdraw_money(100)
# my_cash_desk.can_withdraw_money(30)
# my_cash_desk.can_withdraw_money(31)
# my_cash_desk.can_withdraw_money(1020)
# my_cash_desk.total()

# halva = Product("tahan halva", 10, 18)
# halva.profit()

# hackbook = Laptop("hackbook", 1200, 1340, 1000, 4)
# print(hackbook.stock_price)
# hackbook.profit()
# print(hackbook.name)

# nexus3 = Smartphone("google nexus 3", 800, 900, 123, 456)
# nexus3.profit()

# store = Store("laptop.bg")
# store.load_new_products(nexus3, 2)
# store.list_products()
# store.sell_products(nexus3)
# store.sell_products(nexus3)
# store.sell_products(nexus3)
# store.list_products()
# store.sell_products(hackbook)
# store.total_profit()
