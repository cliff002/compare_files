import csv
import codecs
from datetime import datetime, timedelta

# list of working days
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# function to check if a given date is a working day
def is_working_day(date):
    day = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
    return day in working_days

# list of columns to compare (indices start from 0)
columns_to_compare = [1,2,3]

# index of date column in first file
date_column_index_file1 = 0
# index of date column in second file
date_column_index_file2 = 2

#index of column to check if its blank
blank_column_index = 4

# open first file and read data
with codecs.open("file1.csv", "r",encoding='utf-8', errors='ignore') as f1:
    reader1 = csv.reader(f1)
    data1 = [row for row in reader1]

# open second file and read data
with codecs.open("file2.csv", "r",encoding='utf-8', errors='ignore') as f2:
    reader2 = csv.reader(f2)
    data2 = [row for row in reader2]

# variable to keep track of working days checked
working_days_checked = 0

# loop through rows in both files
for row1, row2 in zip(data1, data2):
    # check if it's a working day
    if is_working_day(row1[date_column_index_file1]):
        working_days_checked += 1
        # check if specified columns match
        if (row1[blank_column_index] or row2[blank_column_index]) and [row1[i] for i in columns_to_compare] != [row2[i] for i in columns_to_compare]:
            print(f"Mismatch on {row1[date_column_index_file1]}: {[row1[i] for i in columns_to_compare]} != {[row2[i] for i in columns_to_compare]}")
    if working_days_checked == 5:
        break
