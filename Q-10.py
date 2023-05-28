from datetime import datetime, timedelta

def get_previous_date(date, n):
    # Convert the date string to a datetime object
    current_date = datetime.strptime(date, '%y-%m-%d')

    # Calculate the timedelta for n days
    delta = timedelta(days=n)

    # Subtract the timedelta from the current date
    previous_date = current_date - delta

    # Format the previous date as a string in the 'yy-mm-dd' format
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str
date = '16-12-10'
n = 11
previous_date = get_previous_date(date, n)
print(previous_date)  # Output: 16-11-29
