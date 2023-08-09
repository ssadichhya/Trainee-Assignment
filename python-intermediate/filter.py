import math 
def filter_prime_numbers(input_num):
    is_prime= lambda num: num > 1 and all(num % i != 0 for i in range(2, math.isqrt(num) + 1))
    return list(filter(is_prime,input_num))

input_list=[1,2,5,7,88,9]
print(filter_prime_numbers(input_list))