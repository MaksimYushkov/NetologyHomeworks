from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    print(datetime.date.today())
    print(calculate_salary())
    print(get_employees())
