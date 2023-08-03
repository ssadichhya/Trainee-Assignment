def convert(name):
    try:
        return(int(name))
    except ValueError:
        raise ValueError(f"Error: '{name}' cannot be converted.")
    except Exception as e:
        raise e


try:
    user_input = input('enter any input')
    print(convert(user_input))
except Exception as e:
    raise e
