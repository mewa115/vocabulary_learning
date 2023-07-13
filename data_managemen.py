import pandas as pd
import csv

# Open the file
rows = 0

with open('Saved translations.csv', 'r') as file:
    # Read the file
    csv_reader1 = csv.reader(file)
    for row in csv_reader1:
        print(row)
        rows = rows +1
print(rows)
print ('---------')

with open('Saved translations.csv', 'r') as file:
    csv_reader2 = csv.reader(file)
    print(csv_reader2)

# Read the CSV file into a dataframe
df = pd.read_csv('Saved translations.csv')
df.columns = ['from_lang', 'to_lang', 'from_value', 'to_value']
print(df)
# Access and manipulate the data in the dataframe
# ...
specific_row = df.iloc[12]
print(type(specific_row))


list_of_lists = df.values.tolist()
print(list_of_lists)
