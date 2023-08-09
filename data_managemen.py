import pandas as pd
import random

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'
column_names = ['language_from', 'language_to', 'word_from', 'word_to', 'number_of_completed_translations']

# load the CSV file
df_add_new_column_if_doesnt_exist = pd.read_csv(original_file, header=None, index_col=False)
if 'number_of_completed_translations' not in df_add_new_column_if_doesnt_exist.columns:
    df_add_new_column_if_doesnt_exist['number_of_completed_translations'] = None
# Create a set of columns for O(1) lookup
existing_columns_set = set(df_add_new_column_if_doesnt_exist.columns)
for index, col_name in enumerate(column_names):
    if col_name not in existing_columns_set:
        df_add_new_column_if_doesnt_exist = df_add_new_column_if_doesnt_exist.rename(
            columns={df_add_new_column_if_doesnt_exist.columns[index]: column_names[index]})
df_add_new_column_if_doesnt_exist.to_csv(copy_file, index=False, header=True)


# If you want to save the DataFrame after renaming columns, you should add:
# df.to_csv(copy_file, index=False, header=True)


def check_if_indexes__are_present():
    # Load the CSV file into a DataFrame
    df = pd.read_csv(original_file)
    # Check for index column
    if 'Unnamed: 0' in df.columns:
        print("CSV file has an index column.")
    else:
        print("CSV file has NO index column.")
    # Check for index row by comparing the data frame index to a range from 0 to length of the data frame
    if not all(df.index == range(0, len(df))):
        print("CSV file has an index row.")
    else:
        print("CSV file has NO index row.")


# Store the original number of rows so that to clear against cleared dataframe
original_rows = df_add_new_column_if_doesnt_exist.shape[0]
df_remove_duplicate = pd.read_csv(copy_file, header=None)
# remove duplicated rows based on the 3rd column
# Split the data into two dataframes so that to compare then later once we clear one of the dataframes
# df1 contains rows with non-empty values in the 4th column
df1 = df_remove_duplicate[df_remove_duplicate[df_remove_duplicate.columns[4]].notna()]
# df2 contains rows with empty values in the 4th column
df2 = df_remove_duplicate[df_remove_duplicate[df_remove_duplicate.columns[4]].isna()]
# Remove duplicates in df2 based on the 3rd column where we have "words_from"
df2 = df2.drop_duplicates(subset=df_remove_duplicate.columns[2])
# Concatenate df1 and df2 to get the final dataframe
df = pd.concat([df1, df2])
# Write the updated dataframe to a new CSV file
df.to_csv(copy_file, index=False, header=False)

# Calculate and print the number of removed duplicates
removed_duplicates = original_rows - df.shape[0]
print(f'Removed {removed_duplicates} duplicates')


# This function defines the set of 10 words for the lesson
def the_words_for_the_lesson():
    df = pd.read_csv(copy_file)
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


print(the_words_for_the_lesson())