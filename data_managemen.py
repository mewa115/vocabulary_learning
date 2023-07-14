import pandas as pd
import csv
import random

current_lesson = list()

def return_the_words_for_the_lesson():
# Read the CSV file into a dataframe
    df = pd.read_csv('Saved translations.csv')
# create columns in the dataframe
#df.columns = ['from_lang', 'to_lang', 'from_value', 'to_value']
    list_dictionary = df.values.tolist()


# construct a dictionary where the second element of each sub-list is the key
# if a key repeats, the value gets overwritten, effectively removing duplicates
    unique_dict = {item[2]: item for item in list_dictionary}

    translations_without_duplicates = list(unique_dict.values())


# declare a list in which I would store list of 10 numbers, which would serve as indexes for the words to pick up for
# current lesson
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


# find the tranlsation using the index, which was generated randomly.
#    print(random_numbers_list)
    for each in random_numbers_list:
         current_lesson.append(translations_without_duplicates[each])


    i = 0
    while i < 10:
#        print(current_lesson[i])
        i = i + 1

    return(current_lesson)


return_the_words_for_the_lesson()
