import csv

csv_file = 'netflix_daily_top_10.csv'
with open(csv_file, newline="") as infile:
    reader = csv.DictReader(infile)
    rows_csv = list(reader)
    fieldnames = reader.fieldnames

csv_file_output = "csv_file_outputs/csv_output.csv"
with open(csv_file_output, newline="") as infile:
    reader = csv.DictReader(infile)
    rows_csv_output = list(reader)
    fieldnames = reader.fieldnames

# -----------------------------------------------------------------------------------

class Match:
    def __init__(self, column, value):
        self.column = column
        self.value = value

# -----------------------------------------------------------------------------------

def write_rows_to_file(rows):
    with open("csv_file_outputs/csv_output.csv", "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def match1(match):
    """Accepts 1 match phrase"""
    matching_rows = []
    for row in rows_csv:
        if row[match.column] == match.value:
            matching_rows.append(row)
    write_rows_to_file(matching_rows)

def not1(match):
    """Accepts 1 optional match phrase"""

    # nested query
    if not match:
        matching_rows = []
        for row_main in rows_csv:
            if row_main not in rows_csv_output:
                matching_rows.append(row_main)
        write_rows_to_file(matching_rows)
        return

    # match object
    matching_rows = []
    for row in rows_csv:
        if row[match.column] != match.value:
            matching_rows.append(row)
    write_rows_to_file(matching_rows)


def and1(match1, match2):
    """Accepts 2 match phrases"""
    matching_rows = []
    for row in rows_csv:
        if row[match1.column] == match1.value and row[match2.column] == match2.value:
            matching_rows.append(row)
    write_rows_to_file(matching_rows)


def or1(match1, match2):
    """Accepts 2 match phrases"""
    matching_rows = []
    for row in rows_csv:
        if row[match1.column] == match1.value or row[match2.column] == match2.value:
            matching_rows.append(row)
    write_rows_to_file(matching_rows)


# -----------------------------------------------------------------------------------
# Sample Match Instances
match_1 = Match("Netflix Exclusive", "Yes")
match_2 = Match("Title", "Ozark")
match_3 = Match("Rank", "1")
match_4 = Match("Rank", "2")


# Sample Queries - run one at a time, comment out others
match1(match_3)
# not1(match_2)
# and1(match_1, match_2)
# or1(match_3, match_4)
# not1(or1(match_3, match_4))


# NOT working: and1()
# and1(or1(match_3, match_4), not1(match_2))
