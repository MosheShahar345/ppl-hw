# Moshe Shahar - 211692165
# Yehonatan Klein - 322961764

from time import time
from functools import reduce
import math
import sys

#-------------------Recursions-------------------

# 1
def make_tuple(n):
    if n == 1:
        return (1,)
    return make_tuple(n - 1) + (n,)


def make_tuple_tail(n):
    def make_tuple_tail_helper(n, acc):
        if n == 1:
            return (1,) + acc
        return make_tuple_tail_helper(n - 1, acc + (n,))
    return make_tuple_tail_helper(n, ())


# 2
def sum_elements(a):
    if len(a) == 1:
        return a[0]
    return a[0] + sum_elements(a[1:])

def sum_elements_tail(a):
    def sum_elements_tail_helper(a, acc):
        if len(a) == 1:
            return a[0] + acc
        return sum_elements_tail_helper(a[1:], acc + a[0])
    return sum_elements_tail_helper(a, 0)

# 3

# def lcm(n1, n2):
#     if n1 < n2:
#         n1, n2 = n2, n1
#     ori_n1 = n1
#     while n1 % n2 != 0:
#             n1 += ori_n1
#     return n1

def lcm_tail(n1, n2):
    def lcm_helper(n1, n2, ori):
        if n1 % n2 == 0:
            return n1
        return lcm_helper(n1 + ori, n2, ori)
    if n1 > n2:
        return lcm_helper(n1, n2, n1)
    else:
        return lcm_helper(n2, n1, n2)

def lcm(n1, n2):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return abs(n1 * n2) // gcd(n1, n2)


# 4
def is_palindrome_tail(n: int) -> bool:
    if len(str(n)) <= 1:
        return True
    if str(n)[0] != str(n)[-1]:
        return False
    return is_palindrome(int(str(n)[1:-1]))

def is_palindrome(n: int) -> bool:
    if len(str(n)) <= 1:
        return True
    return is_palindrome(s[1:-1]) and str(n)[0] == str(n)[-1]


# 5
def sortedzip(lsts):
    def sortedzip_helper(lsts):
        if len(lsts) == 1:
            return [sorted(lsts[0])]
        return [(sorted(lsts[0]))] + sortedzip_helper(lsts[1:])
    return zip(*sortedzip_helper(lsts))

def sortedzip_tail(lsts):
    def sortedzip_tail_helper(lsts, acc):
        if len(lsts) == 1:
            return acc + [sorted(lsts[0])]
        return sortedzip_tail_helper(lsts[1:], acc + [sorted(lsts[0])])
    return zip(*sortedzip_tail_helper(lsts, []))


#-------------------Generators-------------------

# 1.1
def arr_gen():
    return [i for i in range(10000 + 1)]

def arr_lazy_gen():
    for i in range(10000 + 1):
        yield i


# Measure execution time and size for eager evaluation
tic = time()
eager_result = arr_gen()
toc = time()
eager_time = (toc - tic) * 1000
eager_size = sys.getsizeof(eager_result)

# Measure execution time and size for lazy evaluation
tic = time()
lazy_result = arr_lazy_gen()
toc = time()
lazy_time = (toc - tic) * 1000
lazy_size = sys.getsizeof(lazy_result)

print(f"Eager Evaluation:\nTime: {eager_time} seconds\nSize: {eager_size} bytes \n")
print(f"Lazy Evaluation:\nTime: {lazy_time} seconds\nSize: {lazy_size} bytes \n")


# 1.2
def arr_gen_cut():
    arr = arr_gen()
    print(f"Type of full array eager: {type(arr)}")
    print(f"Type of half array eager: {type(arr[:5000])}\n")
    return arr[:5000]

def arr_lazy_gen_cut():
    arr = arr_lazy_gen()
    print(f"Type of full array lazy {type(arr)}")
    print(f"Type of half array lazy {type((next(arr) for _ in range(5000)))}\n")
    return (next(arr) for _ in range(5000))


# Measure execution time and size for eager cut evaluation
tic = time()
eager_cut_result = arr_gen_cut()
toc = time()
eager_cut_time = (toc - tic) * 1000
eager_cut_size = sys.getsizeof(eager_cut_result)

# Measure execution time and size for lazy cut evaluation
tic = time()
lazy_cut_result = arr_lazy_gen_cut()
toc = time()
lazy_cut_time = (toc - tic) * 1000
lazy_cut_size = sys.getsizeof(lazy_cut_result)

print(f"Eager Cut Evaluation:\nTime: {eager_cut_time} seconds\nSize: {eager_cut_size} bytes \n")
print(f"Lazy Cut Evaluation:\nTime: {lazy_cut_time} seconds\nSize: {lazy_cut_size} bytes \n")


# 2
def isPrime(n: int) -> bool:
    if n < 2:
        return False
    dividers = set(i for i in range(2, int(n ** 0.5 + 1)) if n % i == 0)
    return not dividers

def get_prime():
    i = 0
    while True:
        while not isPrime(i):
            i += 1
        yield i


# 3
def power_function(n: int):
    return lambda x: x ** n

def map_of_power_functions(n: int) -> map:
    return map(power_function, range(n))

def taylor_series(x: int, n: int):
    return reduce(lambda a, b: a + b, map(lambda f: f[1](x) / math.factorial(f[0]), enumerate(map_of_power_functions(n))))

def get_taylor_series(x: int):
    i = 1
    while True:
        yield taylor_series(x, i)
        i += 1


a = get_taylor_series(2)
print(list(next(a) for _ in range(8)))
