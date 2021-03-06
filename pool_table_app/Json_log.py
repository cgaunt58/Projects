import json
from Tables import Tables
from Time_functions import Time_function
time_function = Time_function()



class Json_Log():
    def __init__(self, date):
        self.date = date
        self.entry_list = []
        self.recovery_list = []

    

    def create_entry(self, table, start, end, total_time):
        f_start = time_function.date_format(start)
        f_end = time_function.date_format(end)
        f_total_time = time_function.timer_format(end, start)
        entry = {
            "Table Number": table, "Start Time": f_start,
            "End Time": f_end, "Total Time Played": f_total_time, 
        }
        self.entry_list.append(entry)
        return self.entry_list

    

    def create_recovery_entry(self, table, start, end):
        rec_entry = {"Table Number": table,
                     "Start Time": str(start), "End Time": str(end)}
        self.recovery_list.append(rec_entry)
        return self.recovery_list

 

    def log_entry(self, entry):
        with open(f'{self.date}.json', 'w') as file_object:
            json.dump(entry, file_object, indent=2)


    def rec_entry(self, entry):
        with open(f'{self.date}-rec.json', 'w') as file_object:
            json.dump(entry, file_object, indent=2)

    

    def recovery(self, date):
        with open(f'{self.date}-rec.json') as file_object:
            recovery_list = json.load(file_object)
        return recovery_list