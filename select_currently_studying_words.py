import pandas as pd
import random
import file_preparation as fp

original_file = 'Saved_translations_orig.csv'
copy_file = 'Saved_translations_copy.csv'


def update_the_list_of_learning_words():
    df_select_currently_studying = fp.file_preparation()
    # get the list of indexes of all words in the file
    all_indexes = df_select_currently_studying.index.tolist()
    print('all indexes are', all_indexes)
    # get the list of indexes of currently studying words in the file
    indexes_of_currently_studying_words = \
        df_select_currently_studying[df_select_currently_studying['currently_studying'] == True].index.tolist()
    print('indexes_of_currently_studying_words', indexes_of_currently_studying_words)
    try:
        count_the_indexes_of_currently_studying_words = indexes_of_currently_studying_words.count()
    except TypeError:
        count_the_indexes_of_currently_studying_words = 0

    # get the indexes of already learned words
    indexes_of_already_learned_words = df_select_currently_studying[
        df_select_currently_studying['already_learned'] == True].index.tolist()
    print('indexes_of_already_learned_words', indexes_of_already_learned_words )

    # calculate the total number of all learned words
    try:
        count_of_already_learned_words = indexes_of_already_learned_words.count()
    except TypeError:
        count_of_already_learned_words = 0
    # get the indexes of the words, which are available for pickup to learn, i.e. the words which are
    # not currently being learned or words which have been already learned
    indexes_of_available_to_learn_words = [x for x in all_indexes if
                                           x not in indexes_of_currently_studying_words and x not in indexes_of_already_learned_words]
    print('indexes_of_available_to_learn_words', indexes_of_available_to_learn_words)


    if count_the_indexes_of_currently_studying_words == 0:
        indexes_of_new_to_learn_words = random.sample(indexes_of_available_to_learn_words, 50)
        # pick random list of indexes of the words, which are available for learn
        for each in indexes_of_new_to_learn_words:
            df_select_currently_studying[each, 'currently_studying'] = True
    elif count_the_indexes_of_currently_studying_words < 50:
        indexes_of_new_to_learn_words = random.sample(indexes_of_available_to_learn_words, 50 - (
                count_of_already_learned_words + indexes_of_available_to_learn_words))
        for each in indexes_of_new_to_learn_words:
            df_select_currently_studying[each,'currently_studying'] = True

    df_select_currently_studying.to_csv(copy_file, header=0, index=None)
    print('update has been completed')
    print(df_select_currently_studying)
    return df_select_currently_studying

update_the_list_of_learning_words()