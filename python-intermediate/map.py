def squared_num(input_numbers):
    squared_list=list(map(lambda x: x*x,input_numbers))
    return squared_list

number_list=[1,2,4,5,7]
print(squared_num(number_list))