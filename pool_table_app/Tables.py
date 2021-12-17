from datetime import datetime
time = datetime.now()



class Tables:
  def __int__(self, table_number):
   self.table_number = table_number
   self.occupied = False
   self.start_time = ""
   self.end_time = ""
   self.time_played = ""
   self.current_time = ""

  def checkout(self):
      if self.occupied == True:
          print("")
          input(f"Table {self.table_number} is currently in use. Please pick a different table. Press ENTER")
      else:
              self.occupied = True
              self.start_time = datetime.now()
              self.end_time = datetime.now()
              self.time_played = self.end_time - self.start_time     

  def checkin(self):
      if self.occupied == False:
          print("")
          input("This table is currently available. Please choose another table. Press ENTER")
          return False
      else:
          self.occupied = False
          self.end_time = datetime.now()
          self.time_played = self.end_time - self.start_time
          return True

