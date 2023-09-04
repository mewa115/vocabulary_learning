import pandas as pd
import os


def file_preparation():
    original_file = 'Saved_translations_orig.csv'
    copy_file = 'Saved_translations_copy.csv'
    column_names = ['language_from', 'language_to', 'word_from', 'word_to', 'number_of_completed_translations', \
                    'currently_studying', 'already_learned']
    df_file_preparation = pd.read_csv(original_file, header=0, index_col=False)
    if os.path.exists(copy_file):
        print('Skipped preparation... The file is already prepared')
        df_file_preparation.to_csv(copy_file, index=True, header=True)
    else:
        def add_missing_columns(df_file_preparation):
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
            return df_file_preparation

        def check_if_indexes__are_present(df_file_preparation):
            # Check for index column
            if 'Unnamed: 0' in df_file_preparation.columns:
                print("CSV file has an index column.")
            else:
                print("CSV file has NO index column.")
            # Check for index row by comparing the data frame index to a range from 0 to length of the data frame
            if not all(df_file_preparation.index == range(0, len(df_file_preparation))):
                print("CSV file has an index row.")
            else:
                print("CSV file has NO index row.")


        def remove_duplicates(df_file_preparation):
            list_dictionary = df_file_preparation.values.tolist()
            # construct a dictionary where the second element of each sub-list is the key
            # if a key repeats, the value gets overwritten, effectively removing duplicates
            unique_dict = {item[2]: item for item in list_dictionary}
            #    print(unique_dict)
            df_file_preparation = list(unique_dict.values())
            return df_file_preparation

        add_missing_columns(df_file_preparation)
        remove_duplicates(df_file_preparation)

        df_file_preparation.to_csv(copy_file, index=True, header=True)
        print("Preparation's been completed!")
        return df_file_preparation
