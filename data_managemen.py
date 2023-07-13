import pandas as pd
import csv
import random

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
print('-----------')

random_word = list_of_lists[random.randint(0, len(list_of_lists))]



i = 1
random_numbers_list = list()

while i < 11:
    random_number = random.randint(0, len(list_of_lists))
    while random_number in random_numbers_list:
        random_number = random.randint(0, len(list_of_lists))
    random_numbers_list.append(random_number)
    i = i + 1
print(random_numbers_list)

list_for_the_current_lesson = list()

for each in random_numbers_list:
    list_for_the_current_lesson.append(list_of_lists[each])
print(list_for_the_current_lesson[1])

