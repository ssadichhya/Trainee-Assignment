def sum(*args):
    sum=0
    for argv in args:
        sum=sum+argv
    return sum

print(sum(1,2,3,4))