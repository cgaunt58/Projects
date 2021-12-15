shopping_lists = [] 

class Item: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 

class ShoppingList:
  def __init__(self, title, address):
    self.title = title
    self.address = address
    self.items = [] 

  def add_item(self, item): 
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item) 