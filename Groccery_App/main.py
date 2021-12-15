import unittest 
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
while True:
 
    print("1. Add Shopping List: ")
    print("2. View All Shopping List: ")
    print("3. Add Item to a Shopping List: ")
    print("4. Select List to Remove: ")
    print("5. Select a list item to remove: ")
    print("q: Quit: ")
    
    choice = input("Enter a selection: ")
    
    
    if choice == "1":
       title = input("Enter name of shopping list: ")
       address = input("Enter shopping list address: ")
       shopping_list = ShoppingList(title, address)
       shopping_lists.append(shopping_list)


    elif choice == "2": 
       for index in range(len(shopping_lists)):
         shopping_list = shopping_lists[index]
         print(f"{index + 1} - {shopping_list.title}")
         for item in shopping_list.items: 
          print(item.name)

    elif choice == "3": 
       for index in range(len(shopping_lists)):
         shopping_list = shopping_lists[index]
         print(f"{index + 1} - {shopping_list.title}")
       shopping_list_index = int(input("Enter shopping list number to add items to: "))
       shopping_list = shopping_lists[shopping_list_index - 1]
       item_name = input("Enter item name: ")
       item_price = float(input("Enter item price: ")) 
       grocery_item = Item(item_name, item_price)
       shopping_list.add_item(grocery_item)


    elif choice == "4":
       for index in range(len(shopping_lists)):
         shopping_list = shopping_lists[index]
         print(f"{index + 1} - {shopping_list.title}")
         for item in shopping_list.items: 
           print(item.name)
       shopping_list = ShoppingList(title, address) 
       del_choice = int(input("Enter Number of shopping list to remove: "))
       del shopping_lists[del_choice - 1] 


    elif choice == "5":
         for index in range(len(shopping_lists)):
          shopping_list = shopping_lists[index]
         print(f"{index + 1} - {shopping_list.title}")
         for item in shopping_list.items: 
          print(item.name)
         shopping_list_index = int(input("Enter shopping list number to remove items from: "))
         shopping_list = shopping_lists[shopping_list_index - 1]
         item_name = input("Enter item to remove: ")
         grocery_item = Item(item_name, item_price)
         shopping_list.remove_item(item)


    elif choice == "q":
      break    
unittest.main()