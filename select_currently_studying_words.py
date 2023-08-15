import pandas as pd
import random

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'

df_select_currently_studying = pd.read_csv(copy_file)
# calculate the number of rows in the file
num_rows = df_select_currently_studying.shape[0]

# generate 50 numbers from the range
random_indexes = random_numbers = random.sample(range(0, num_rows), 50)

# set the value to TRUE for the words, which I want to learn. I need to fins the row with the index from the
# random_indexes and set the TRUE value to the last column
for each in random_indexes:
    if df_select_currently_studying.loc[each:each, 'already_learned'] ==  False:
        df_select_currently_studying.loc[each:each, 'currently_studying'] = True
df_select_currently_studying.to_csv(copy_file)

number_total = df_select_currently_studying['word_from'].notna().sum()
print(number_total)