from Time_functions import Time_function
from Tables import Tables
from datetime import datetime
from time import time
from Json_log import Json_Log
day = datetime.now()




class Table_manager():
    def __init__(self, day):
        self.day = day
        self.date = time_function.date_only(day)
       

    def print_lines(self):
        print("")
        print("-----------------------------------")
        print("")
    

    def show_menu(self):
  
        print("")
        print(f"-------------------------")
        print(f" \t   {self.date}\n")
        print("CHECKOUT TABLE: Press 1: ")
        print("CLOSE TABLE: Press 2: ")
        print("VIEW ALL TABLES: Press 3: ")
        print("DATA RECOVERY: Press 4: ")
        print("To QUIT, Press 'q': ")
        self.print_lines()

  
    def show_tables(self):
        current_time = datetime.now()
        print("")
        print("------------------------\n")
        print("         TABLE LIST")
        self.print_lines()
        for table in tables:
            if table.occupied == True:
                status = "Occupied"
            else:
                status = "Available"
            if table.start_time != "":
                clock = time_function.clock_format(table.start_time,)
                elapsed_time = time_function.timer_format(
                    current_time, table.start_time)
                print(
                    f"Table-{table.number} - {status} -  Start: {clock} - Play time: {elapsed_time}")
            else:
                print(
                    f"Table-{table.number} - {status}")
        self.print_lines()
    

    def choose_table(self, user_input):
        while True:
            try:
                if user_input == "1":
                    choice = int(input("Enter table a table to use: ")) - 1

                else:
                    choice = int(input("Enter table number to quit: ")) - 1

                table = tables[choice]
                return table
               
            except ValueError:
                print("\n")
                print(
                    "Please enter a different table number:")
                print("\n")
            except:
                print(
                    "\n Press Enter to continue: ")

   
    def repopulate_data(self, json_data):
        recovery_time = datetime.now()
        for i in range(len(json_data)):
            temp_table = json_data[i]
            temp_table_no = int(temp_table["Table Number"])
            print(temp_table_no)
            for table in tables:
                if table.number == temp_table_no:
                    table.occupied = True
                    table.start_time = datetime.strptime(
                        temp_table["Start Time"], "%Y-%m-%d %H:%M:%S.%f")
                    table.end_time = recovery_time

   
    def chooser(self, user_input):
        if user_input == "1":
            print("")
            confirmation = input(
                "Checkout Table?\nEnter y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables()
                table = self.choose_table(user_input)
                table.checkout()
                recovery_list = activity_log.create_recovery_entry(
                    table.number, table.start_time, table.end_time)
                activity_log.rec_entry(recovery_list)
                self.show_tables()
                print(
                    f"Table {table.number} has been checked out at: {time_function.clock_format(table.start_time)}")
            else:
                print("")
                print(" You did not enter a correct response.  Please try again. ")

        elif user_input == "2":
            print("")
            confirmation = input(
                "Close out Table?\nEnter y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                self.show_tables()
              
                all_available = True
                for table in tables:
                    if table.occupied == True:
                        all_available = False
                if all_available == True:
                    print("")
                    input(
                        " All Tables are available. Choose another menu option. \nPress RETURN to continue: ")
                   
                else:
                    table = self.choose_table(user_input)
                    status = table.checkin()
                    if status == True:
                        entry = activity_log.create_entry(
                            table.number, table.start_time, table.end_time, table.time_played)
                        activity_log.log_entry(entry)
                        table.start_time = ""
                        self.show_tables()
                        print(
                            f"Table {table.number} has been closed out at: {time_function.clock_format(table.end_time)}")

            else:
                print("")
                print("You did not enter a correct response.  Please try again.")

        elif user_input == "3":
            self.show_tables()

        elif user_input == "4":
            print("")
            confirmation = input(
                "Recover table activity?\nEnter  y/n: ").lower()
            if confirmation == "n":
                print("")
            elif confirmation == "y":
                recovery_list = activity_log.recovery(self.date)
                self.repopulate_data(recovery_list)
                self.show_tables()
            else:
                print("")
                print("You did not enter a correct response.  Please try again.")




time_function = Time_function()
manager = TableManager(day)
activity_log = Json_Log(manager.date)


tables = []
for i in range(1, 13):
    table = Tables(i)
    tables.append(table)



user_input = ""
while user_input != "q":
    manager.show_menu()
    user_input = input("Please enter a choice from the menu: ")
    manager.chooser(user_input)