from datetime import datetime, date, timedelta

def display_current_time():
    current_time = datetime.now().replace(microsecond=0)
    print(f"Current date and time: {current_time}")

def calculate_future_date(number):
    tday = date.today()
    tdelta = timedelta(days=number)
    future_date = tday + tdelta
    print(f"Future date: {future_date}")

display_current_time()
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)