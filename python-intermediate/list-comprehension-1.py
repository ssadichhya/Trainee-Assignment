input_list = input("Enter a list of strings ")
string_list = input_list.split(' ')
result = [string for string in string_list if len(string) > 5]
print(result)
