def convert(name):
    """_summary_

    Args:
        name (_type_): _description_

    Raises:
        ValueError: _description_
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        return (int(name))
    except ValueError:
        raise ValueError(f"Error: '{name}' cannot be converted.")
    except Exception as e:
        raise e


try:
    user_input = input('enter any input')
    print(convert(user_input))
except Exception as e:
    raise e
