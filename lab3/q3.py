class Inventory:
    def __init__(self):
        self.items={}
    def add_items(self,id,name,stock,price):
        self.items[id]=[name,stock,price]
    def update_items(self,id,stock,price):
        if stock is not None:
            self.items[id][1]=stock
        if price is not None:
            self.items[id][2]=price
    def check_item_details(self,id):
        if id in self.items:
            print(self.items[id])
        else:
            print("Unavailable")
my_inventory=Inventory()
my_inventory.add_items(1,"pencil",12,522)
my_inventory.add_items(2,"pen",31,555)

my_inventory.check_item_details(2)
