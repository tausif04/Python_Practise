# Handling Time Zones

import pytz
import datetime
# Set a timezone
timezone = pytz.timezone("America/New_York")
ny_time = datetime.datetime.now(timezone)
print("New York Time:", ny_time)
# Convert to another timezone
london_timezone = pytz.timezone("Europe/London")
london_time = ny_time.astimezone(london_timezone)
print("London Time:", london_time)