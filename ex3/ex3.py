# Moshe Shahar - 211692165
# Yehonatan Klein - 322961764

import math
from functools import reduce
from time import time
from datetime import datetime, timedelta
from hdate import HDate

# 1
linear_func = lambda x: x / 2 + 2

# 1.1
lst_linear = list(map(linear_func, range(10000 + 1)))

# 1.2
lst_sum = reduce(lambda x, y: x + y, map(linear_func, range(10000 + 1)))

# 1.3
tic = time()
sum1 = reduce(lambda x, y: x + y, map(linear_func, range(10000 + 1)))
toc = time()
time1 = (toc - tic) * 1000

tic = time()
sum2 = 0
for i in lst_linear:
    sum2 += i
toc = time()
time2 = (toc - tic) * 1000

print(f"Time using reduce: {time1}\nTime using for loop: {time2}")

# 1.4
def one_func_to_rule_them_all():
    return reduce(lambda x, y: x + y, map(lambda x: x / 2 + 2, range(10000 + 1)))


# 2
def make_odd_even_lsts(func, lst):
    return list(filter(func, lst))

lst = list(range(1, 1000 + 1))
odd_lst = make_odd_even_lsts(lambda x: x % 2 != 0, lst)
even_lst = make_odd_even_lsts(lambda x: x % 2 == 0, lst)

# 2.1
even_mul = lambda z: reduce(lambda x, y: x * y, z)
odd_lin = lambda z: reduce(lambda x, y: linear_func(x) + y, z)

# 2.2
def apply_for_odd_even_lsts(func, lst):
    return func(lst)

res1, res2 = apply_for_odd_even_lsts(even_mul, even_lst), apply_for_odd_even_lsts(odd_lin, odd_lst)

# 2.3
print(res1)
print(res2)

# 3.1
def get_dates(start_date: str, num_dates: int, skip_days: int):
    formated_start_date = datetime.strptime(start_date, '%d-%m-%Y')
    return list(map(lambda x: (formated_start_date + timedelta(days=x * skip_days)).strftime('%d-%m-%Y'), range(1, num_dates + 1)))


result = get_dates('01-10-2024', 5, 2)
print(result)

# 3.2
def get_hebrew_dates(start_date: str, num_dates: int, skip_days: int):
    formatted_start_date = datetime.strptime(start_date, '%d-%m-%Y')

    return list(map(lambda x: HDate(formatted_start_date + timedelta(days=x * skip_days)).hebrew_date, range(1, num_dates + 1)))


result = get_hebrew_dates('01-10-2024', 5, 2)
print(result)


# 4.1
def power_function(n: int):
    return lambda x: x ** n

# 4.2
def map_of_power_functions(n: int) -> map:
    return map(power_function, range(n))

# 4.3
def taylor_series(x: int, n: int):
    return reduce(lambda a, b: a + b, map(lambda f: f[1](x) / math.factorial(f[0]), enumerate(map_of_power_functions(n))))


# 5
def task_manager() -> dict:
    tasks = {}

    def add_task(name: str, status: str = "incomplete"):
        tasks[name] = status

    def complete_task(name: str):
        if name in tasks and tasks[name] != "complete":
            tasks[name] = "complete"

    def get_tasks():
        return tasks

    return {
        'add_task': add_task,
        'complete_task': complete_task,
        'get_tasks': get_tasks
    }

def test_task_manager():
    # Create a new task manager
    tasks_manager = task_manager()
    # Add tasks
    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")
    # Get the list of tasks
    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)
    assert current_tasks == {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework': 'incomplete'}
    # Mark a task as complete
    tasks_manager['complete_task']("Write email")
    # Get the list of tasks after marking and deleting
    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)
    assert current_tasks == {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}


test_task_manager()
