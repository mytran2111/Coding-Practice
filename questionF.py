from collections import Counter 
n = int(input())
best_key = 0 
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
factor_list = prime_factors(n)
factor_dict = dict()
for i in factor_list: 
    factor_dict[i] = factor_list.count(i)

min_key = None
max_value = 0
 
for key,value in factor_dict.items():
    if max_value < value:
        max_value = value
        min_key = key
    elif max_value == value:
        if min_key > key: 
            min_key = key

print(min_key)



