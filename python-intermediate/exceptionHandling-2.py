def openFile(name):
    try:
        with open(name, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{name}' not found.")
    except Exception as e:
        raise e
    

try:
    filename=input('enter filename')
    print(openFile(filename))
except Exception as e:
    raise e