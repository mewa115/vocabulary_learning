import random
import select_currently_studying_words as sl


# This function defines the set of 10 words for the lesson
def the_words_for_the_lesson():
    df_the_words_for_the_lesson = sl.update_the_list_of_learning_words()
    # declare a list in which I would store list of 10 numbers, which would serve as indexes for the words to pick up
    # for the current lesson
    i = 1
    random_numbers_list = list()
    # define the list of random numbers
    while i < 11:
        # define the range from which to pick up indexes. It is based on the number of rows in the df.
        random_number = random.randint(0, 50)
        while random_number in random_numbers_list:
            random_number = random.randint(0, 50)
        random_numbers_list.append(random_number)
        i = i + 1
    current_lesson = list()
    # find the translation using the index, which was generated randomly.
    for each in random_numbers_list:
        current_lesson.append(translations_without_duplicates[each])
    i = 0
    while i < 10:
        i = i + 1
