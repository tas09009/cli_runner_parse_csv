import csv

# csv_file = 'netflix_daily_top_10.csv'
csv_file = "netflix_short.csv"


# Open the input CSV file and read its contents into a list of dictionaries
with open(csv_file, newline="") as infile:
    reader = csv.DictReader(infile)
    # reader.fieldnames = list of headers
    rows_csv = list(reader)
    fieldnames = reader.fieldnames


def write_rows_to_file(rows):
    with open("csv_file_outputs/csv_testing.csv", "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


class Match:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    # @staticmethod
    # def match(self, column, value):
    #     matching_rows = []
    #     for row in rows_csv:
    #         if row[column] == value:
    #             matching_rows.append(row)
    #     write_rows_to_file(matching_rows)

    # def __not__(self):
    #     matching_rows = []
    #     for row in rows_csv:
    #         if row[self.column] == self.value:
    #             matching_rows.append(row)
    #     write_rows_to_file(matching_rows)

def match1(match):
    """Accepts 1 match phrase"""
    matching_rows = []
    for row in rows_csv:
        if row[match.column] == match.value:
            matching_rows.append(row)
    write_rows_to_file(matching_rows)

def not1(match):
    """Accepts 1 match phrase"""
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


match11 = Match("Netflix Exclusive", "Yes")
match22 = Match("Type", "Movie")
match1(match1)                      # _____
# not1(match2)                      # WORKS
# and1(match1, match2)              # WORKS
# or1(match1, match2)               # _____




"""
FUNCTIONALITIES

MATCH(<column_name>, <matching_value>)

Ex:
    MATCH("Rank", "1")

--------------------------------------
NOT - 1 argument
AND -2 arguments
OR - 2 arguments

Ex:
    AND(MATCH("Rank", "1"), MATCH("Days in Top 10", "0"))

--------------------------------------
() to group commands

Ex:
    AND(OR(MATCH("Rank", "1"), MATCH("Rank", "2")), NOT(MATCH("Title", "Ozark")))
    NOT(OR(MATCH("Rank", "1"), MATCH("Rank", "2")))


"""