#Current Date Time With Expected Format
import datetime

current_datetime=datetime.datetime.now()

formated_datetime=current_datetime.strftime("%d/%m/%Y  %H:%M:%S")
print(f"Current Date and Time : {formated_datetime}")