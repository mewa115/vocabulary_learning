import pandas as pd
import random

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'
column_names = ['language_from', 'language_to', 'word_from', 'word_to', 'number_of_completed_translations',\
                'currently_studying', 'already_learned']

df_file_preparation = pd.read_csv(original_file, header=0, index_col=False)


def add_missing_columns(df_file_preparation):
    # load the CSV file.
    if 'number_of_completed_translations' not in df_file_preparation.columns:
        df_file_preparation['number_of_completed_translations'] = 0
    # Create a set of columns for O(1) lookup
    existing_columns_set = set(df_file_preparation.columns)
    if 'currently_studying' not in df_file_preparation.columns:
        df_file_preparation['currently_studying'] = False
    if 'already_learned' not in df_file_preparation.columns:
        df_file_preparation['already_learned'] = False

    for index, col_name in enumerate(column_names):
        if col_name not in existing_columns_set:
            df_file_preparation = df_file_preparation.rename(
                columns={df_file_preparation.columns[index]: column_names[index]})
    df_file_preparation.to_csv(copy_file, index=False, header=True)

# Remove the data from the variable, which was used to store the datafrome from the original file.


def check_if_indexes__are_present(original_file):
    # Load the CSV file into a DataFrame
    df_index_check = pd.read_csv(original_file)
    # Check for index column
    if 'Unnamed: 0' in df_index_check.columns:
        print("CSV file has an index column.")
    else:
        print("CSV file has NO index column.")
    # Check for index row by comparing the data frame index to a range from 0 to length of the data frame
    if not all(df_index_check.index == range(0, len(df_index_check))):
        print("CSV file has an index row.")
    else:
        print("CSV file has NO index row.")

add_missing_columns(df_file_preparation)

df_remove_duplicate = pd.read_csv(copy_file, header=None, index_col=False)

# Store the original number of rows so that to clear against cleared dataframe
original_rows = df_remove_duplicate.shape[0]
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
if removed_duplicates != 0:
    print(f'Removed {removed_duplicates} duplicates')

del df, df1, df2, removed_duplicates, df_remove_duplicate, original_rows
