class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(
            f"InvalidAgeError: Age '{age}' is not within the valid range (0 to 120).")
        

def age_check(age):
    if age<0 and age>120:
        raise InvalidAgeError
    return age


try:
    age=int(input("enter age"))
    age_check(age)
except ValueError:
        print("Error: Please enter a valid integer for age.")
except InvalidAgeError:
        print(InvalidAgeError)
except Exception as e:
        print("An unexpected error occurred:", e)

