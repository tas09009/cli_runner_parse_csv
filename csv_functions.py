
import csv

def write_rows_to_file(rows):
    with open("csv_file_outputs/csv_output.csv", "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
