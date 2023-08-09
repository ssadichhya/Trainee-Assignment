def open_file(name):
    """_summary_

    Args:
        name (_type_): _description_

    Raises:
        FileNotFoundError: _description_
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        with open(name, 'r', encoding="utf-8") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{name}' not found.")
    except Exception as e:
        raise e


try:
    filename = input('enter filename')
    print(open_file(filename))
except Exception as e:
    raise e
