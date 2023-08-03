import csv
def filter_adults(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='') as csv_out_file:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csv_out_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


input_file = "data.csv"
output_file = "adults.csv"

try:
    filter_adults(input_file, output_file)
    print(f"Filtered data saved to {output_file}.")
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
