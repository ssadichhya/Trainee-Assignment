def find_bigger_number(a,b,c):
    return "Equal" if a == b == c else (a if a >= b and a >= c else (b if b >= c else c))

print(find_bigger_number(3,4,5))
