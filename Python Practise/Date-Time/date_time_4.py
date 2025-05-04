import datetime
# Subtracting two dates
date1 = datetime.datetime(2024, 9, 1)
date2 = datetime.datetime(2023, 9, 1)
difference = date1 - date2
print("Difference:", difference)
# Adding 10 days to a date
new_date = date1 + datetime.timedelta(days=10)
print("New Date:", new_date)