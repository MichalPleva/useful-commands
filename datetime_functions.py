import datetime

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

# Generate dates in range
for month in range(1, 13):
    print(last_day_of_month(datetime.date(2019, month, 1)))
