from datetime import datetime, date, timedelta

def display_current_datetime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_time}")

def calculate_future_date(number):
    tday = datetime.now()
    tdelta = timedelta(days=number)
    future_date = tday + tdelta
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")

display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)