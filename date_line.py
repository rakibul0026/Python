
import datetime

# Current datetime
print(datetime.datetime.now())

# Current UTC time
print(datetime.datetime.utcnow())

# Get today's date
print(datetime.date.today())

# Timestamp
random_date = datetime.date.fromtimestamp(12345678)
print(random_date.year)
print(random_date.month)
print(random_date.day)
