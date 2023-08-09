def search_log(log_file, search_keyword):
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
                f"No lines containing the search keyword '{search_keyword}' were found.")
    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


log_file = "sample.log"
search_keyword = "ERROR"
search_log(log_file, search_keyword)
