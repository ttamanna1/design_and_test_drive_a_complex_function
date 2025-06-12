from dateutil.relativedelta import relativedelta
from datetime import datetime

def age_checker(date):
    if type(date) != str:
        raise Exception('Enter DOB in string format.')
    
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Enter DOB in string format: YYYY-MM-DD.')
    
    todays_date = datetime.today().date()
    
    age = relativedelta(todays_date, date_object).years

    if age > 16:
        return 'Access granted'
    else:
        return f"Access denied. Your age is {age}. You need to be 16."