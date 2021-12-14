shopping_lists = [] 

class GroceryItem: 
  def __init__(self, name, price, quantity): 
    self.name = name 
    self.price = price
    self.quantity = quantity

class ShoppingList: 
  def __init__(self, name, address): 
    self.name = name 
    self.address = address 
    self.grocery_items = [] 
  
  def add_grocery_item(self, item):
    self.grocery_items.append(item)
    

def display_all_shopping_lists(): 
    for index in range(0, len(shopping_lists)):
      shopping_list = shopping_lists[index]
      print(f"{index + 1}. {shopping_list.name}")

while True:
  print("1. Add a Shopping Location: ")
  print("2. add item to an existing shopping list: ")
  print("3. display shopping lists: ")
  print("q to quit")

  choice = input("Enter choice: ")

  if choice == "1": 
   name = input("Enter Shopping Location: ")
   address = input("Enter Shop Address: ")
   print("\n")
   shopping_list = ShoppingList(name, address)
   shopping_lists.append(shopping_list)
   print("\n")
  elif choice == "2": 
    print("===============")
    print("Current Shopping Lists")
    print("===============")
    display_all_shopping_lists()
    print("Select List to add to: ")
    grocery_item = input("Enter item name: ")
    grocery_price = input("Enter price of item: ")
    grocery_quantity = input("Enter quantity of item: ")
    print("\n")
    item = GroceryItem(grocery_item, grocery_price, grocery_quantity)
    shopping_lists.append(item)
  elif choice == "3":
     print("===========================")
     print("Current Shopping Lists")
     print("===========================")
     display_all_shopping_lists() 
     print("\n")
  elif choice == "q":
    break     
     
  
     
   
