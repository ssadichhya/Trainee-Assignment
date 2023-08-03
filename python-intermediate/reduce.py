from functools import reduce

def concantenate_string(string_input):
    result=reduce((lambda x,y:x+y),string_input)
    return result

print(concantenate_string(["sad","mad","had"]))