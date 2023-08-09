class InvalidAgeError(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, age):
        """_summary_

        Args:
            age (_type_): _description_
        """
        super().__init__(
            f"InvalidAgeError:'{age}' is not within the valid rang.")


def age_check(age):
    """_summary_

    Args:
        age (_type_): _description_

    Raises:
        InvalidAgeError: _description_

    Returns:
        _type_: _description_
    """
    if age < 0 and age > 120:
        raise InvalidAgeError
    return age


try:
    age = int(input("enter age"))
    age_check(age)
except ValueError:
    print("Error: Please enter a valid integer for age.")
except InvalidAgeError:
    print(InvalidAgeError)
except Exception as e:
    print("An unexpected error occurred:", e)
