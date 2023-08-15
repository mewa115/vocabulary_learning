import pandas as pd
import random

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'

df_select_currently_studying = pd.read_csv(copy_file, index_col=None)
# calculate the number of rows in the file
num_rows = df_select_currently_studying.shape[0]

# generate 50 numbers from the range




random_indexes = random_numbers = random.sample(range(0, num_rows), 50)

number_total = df_select_currently_studying['word_from'].notna().sum()
print(number_total)

# calculate the number of words, which are currently in the lesson. The value should be 50.
count_true = df_select_currently_studying[df_select_currently_studying['currently_studying'] == True].shape[0]

if count_true < 50:
    difference = 50 - count_true
    for each in range(1,difference):
        if df_select_currently_studying.loc[each:each, 'already_learned'].values[0] == False:
            if df_select_currently_studying.loc[each:each, 'currently_studying'].values[0] == False:
                df_select_currently_studying.loc[each:each, 'currently_studying'] = True
else:
    for each in random_indexes:
        if df_select_currently_studying.loc[each:each, 'already_learned'].values[0] == False:
            if df_select_currently_studying.loc[each:each, 'currently_studying'].values[0] == False:
                df_select_currently_studying.loc[each:each, 'currently_studying'] = True


print(count_true)

