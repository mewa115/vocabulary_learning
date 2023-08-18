import pandas as pd
import random
#import file_preparation as fp

copy_file = 'Saved_translations_copy.csv'

# This function defines the set of 10 words for the lesson
def the_words_for_the_lesson():
    df_the_words_for_the_lesson = pd.read_csv(copy_file, index_col=False, header=0)
    list_dictionary = df_the_words_for_the_lesson.values.tolist()
    # construct a dictionary where the second element of each sub-list is the key
    # if a key repeats, the value gets overwritten, effectively removing duplicates
    unique_dict = {item[2]: item for item in list_dictionary}
#    print(unique_dict)
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


the_words_for_the_lesson()

# prepare the data_frame
#df_pick_up_words_for_the_lesson = pd.read_csv(copy_file)

#df_pick_up_words_for_the_lesson.loc[
#    df_pick_up_words_for_the_lesson['word_from'] == 'Zusatzpanzerung', 'number_of_completed_translations'] = 3

#df_pick_up_words_for_the_lesson.to_csv('test.csv', header=0, index=False)
