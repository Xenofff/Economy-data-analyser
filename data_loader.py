import csv

def load_data(file_paths):
    all_rows = []
    for path in file_paths:
        with open(path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_rows.append(row)
    return all_rows