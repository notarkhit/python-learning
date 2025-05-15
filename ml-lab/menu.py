class menuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantitiy = int(quantity)

    def getQty(self):
        print(f"STOCK: {self.quantitiy}")

    def order(self):
        
        self.getQty()

        if self.quantitiy == 0:
            print(f"{self.name} is out of stock!!")
            return

        print(f"How much of {self.name} would you like to order: ")
        orderQty = int(input())
        totalprice = 0

        if orderQty <= self.quantitiy:
            self.quantitiy = self.quantitiy - orderQty
            totalprice = self.price * orderQty
        else:
            print(f"{orderQty} items not in stock")

        return totalprice

    def restock(self):
        self.getQty()
        newStock = int(input("How many units to restock?? : "))
        self.quantitiy = self.quantitiy+newStock

item = menuItem('burger',20,40)
item.order()
item.order()
item.restock()
item.order()
item.restock()
item.order()
item.restock()
