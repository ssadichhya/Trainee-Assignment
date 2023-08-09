log_file = "sample.log"
search_keyword = "ERROR"


def search_log(log_file, search_keyword):
    """_summary_

    Args:
        log_file (_type_): _description_
        search_keyword (_type_): _description_
    """
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        found_lines = []
        for line in lines:
            if search_keyword in line:
                found_lines.append(line)

        if found_lines:
            print(f"Lines containing the search keyword '{search_keyword}':")
            for line in found_lines:
                print(line.strip())
        else:
            print(
                f"No lines containing the search keyword '{search_keyword}' \
                 were found."
                )
    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


search_log(log_file, search_keyword)
