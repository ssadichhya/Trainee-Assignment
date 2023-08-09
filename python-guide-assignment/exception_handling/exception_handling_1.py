def division(num1, num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print("second number is zero")


try:
    num_1 = int(input("enter 1st number"))
    num_2 = int(input("enter 2nd number"))
    print(division(num_1, num_2))
except ValueError as ve:
    print(ve)
except Exception as e:
    print("An unexpected error occurred:", e)
