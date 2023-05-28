from datetime import datetime, timedelta

def date_difference(from_date, to_date, difference):
    date_format = "%y-%m-%d"
    from_datetime = datetime.strptime(from_date, date_format)
    to_datetime = datetime.strptime(to_date, date_format)
    delta = abs(from_datetime - to_datetime)
    return delta.days < difference
print(date_difference('21-05-01', '21-05-10', 10))  # True
print(date_difference('21-05-01', '21-05-15', 10))  # False
