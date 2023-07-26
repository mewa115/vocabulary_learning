import pandas as pd
import numpy as np
import csv
import random

# load the CSV file
df_add_new_column_if_doesnt_exist = pd.read_csv('Saved translations.csv')
# Check if the column exists
if 'number_of_right_answers' not in df_add_new_column_if_doesnt_exist.columns:
    # Add a new column
    df_add_new_column_if_doesnt_exist[
        'number_of_right_answers'] = None  # this will add a new column with all values set to "default_value"
# Save the DataFrame to CSV
df_add_new_column_if_doesnt_exist.to_csv('Saved translations.csv', index=False)

# Store the original number of rows
original_rows = df_add_new_column_if_doesnt_exist.shape[0]

df_remove_duplicate = pd.read_csv('Saved translations.csv')
# remove duplicated rows based on the 3rd column
# Split the data into two dataframes
# df1 contains rows with non-empty values in the 4th column
df1 = df_remove_duplicate[df_remove_duplicate[df_remove_duplicate.columns[4]].notna()]
print(df1)
# df2 contains rows with empty values in the 4th column
df2 = df_remove_duplicate[df_remove_duplicate[df_remove_duplicate.columns[4]].isna()]
print(df2)
# Remove duplicates in df2 based on the 3rd column
df2 = df2.drop_duplicates(subset=df_remove_duplicate.columns[2])
# Concatenate df1 and df2 to get the final dataframe
df = pd.concat([df1, df2])
# Write the updated dataframe to a new CSV file
df.to_csv('Saved translations.csv', index=False)

# Calculate and print the number of removed duplicates
removed_duplicates = original_rows - df.shape[0]
print(f'Removed {removed_duplicates} duplicates')


def the_words_for_the_lesson():
    dataframe = pd.read_csv('Saved translations.csv')
    list_dictionary = df.values.tolist()

    # construct a dictionary where the second element of each sub-list is the key
    # if a key repeats, the value gets overwritten, effectively removing duplicates
    unique_dict = {item[2]: item for item in list_dictionary}

    translations_without_duplicates = list(unique_dict.values())

    # declare a list in which I would store list of 10 numbers, which would serve as indexes for the words to pick up
    # for the current lesson
    i = 1
    random_numbers_list = list()

    # define the list of random numbers
    while i < 11:
        # define the range from which to pick up indexes. It is based on the number of rows in the df.
        random_number = random.randint(0, len(translations_without_duplicates))
        while random_number in random_numbers_list:
            random_number = random.randint(0, len(translations_without_duplicates))
        random_numbers_list.append(random_number)
        i = i + 1
    current_lesson = list()

    # find the translation using the index, which was generated randomly.
    for each in random_numbers_list:
        current_lesson.append(translations_without_duplicates[each])
    i = 0
    while i < 10:
        i = i + 1
    return current_lesson
