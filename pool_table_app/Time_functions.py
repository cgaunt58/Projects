 
class Time_function():
    def __int__ (self):
        self.clock = ""
  
    def timer_function(self, end, start):
        delta_time = end - start
        delta_sec = delta_time.total_seconds()
        hours = round(delta_sec / (60 * 60))
        rem_minutes = delta_sec % 60 * 60
        minutes = round(rem_minutes / 60)

    
    def start_clock_format(self, time):
        hour = time.hour
        minute= time.minute
        if minute < 10:
            minute = f"0{minute}"
            self.clock = "AM"
        if hour > 12 :
            hour -= 12
            self.clock = "PM"
        clock = f"{hours}:{minutes} {self.clock}"
        return clock

    def time_date_format(self, date):
        date_time = f"{date.month} - {date.day} {self.start_clock_format(date)}"                 

    def date_only(self, date):
        date_display = f"{date.month} - {date.day} - {date.year}"
        return date_display    