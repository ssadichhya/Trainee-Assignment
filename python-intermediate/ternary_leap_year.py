def check_leap_year(input_year):
    result = ("Leap Year" if (input_year % 4 == 0 and input_year % 100 != 0)
              or (input_year % 400 == 0) else "Not a Leap Year")
    return result

print(check_leap_year(1999))