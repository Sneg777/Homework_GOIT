'''
HOMEWORK TASK #1
'''

def caching_fibonacci():
    cache = dict()
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))

'''
HOMEWORK TASK 2
'''
from typing import Callable
import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r'\d+\.\d+|\d+'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    result = 0
    for number in func(text):
        result += number
    return result

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

