import pandas as pd
import random

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'

#read the csv file
df_select_currently_studying = pd.read_csv(copy_file, index_col=None)

# calculate the number of words, which are currently in the lesson. The value should be 50.
count_true = df_select_currently_studying[df_select_currently_studying['currently_studying'] == True].shape[0]
print('initial count_true is ', count_true)

if count_true == 0:
    # calculate the number of rows in the file. The attribute shape[0] - returns the number of rows and
    # shape[1] returns the number of columns.
    num_rows = df_select_currently_studying.shape[0]
    print('total number of rows is ', num_rows)
    # generate 50 numbers from the range
    random_indexes = random.sample(range(0, num_rows), 50)
    print('random_indexes are ', random_indexes)
    for each in random_indexes:
        if df_select_currently_studying.loc[each:each, 'already_learned'].values[0] == False:
            if df_select_currently_studying.loc[each:each, 'currently_studying'].values[0] == False:
                df_select_currently_studying.loc[each:each, 'currently_studying'] = True
# if count_true < 50:
#     difference = 50 - count_true
#     for each in range(1,difference+1):
#         if df_select_currently_studying.loc[each:each, 'already_learned'].values[0] == False:
#             if df_select_currently_studying.loc[each:each, 'currently_studying'].values[0] == False:
#                 df_select_currently_studying.loc[each:each, 'currently_studying'] = True


check_count_true = df_select_currently_studying[df_select_currently_studying['currently_studying'] == True].shape[0]
print('check_count_true is ', check_count_true)