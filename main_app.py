import tkinter as tk
import re
import pick_up_words_for_the_lesson as pk
from tkinter import Tk, Entry, Button, Label, StringVar, messagebox

current_lesson = pk.the_words_for_the_lesson()

# This class defines the default CSS characteristics of the main window
class MainWindow:
    counter = 0
    right_answers = 0
    wrong_answers = 0

    def __init__(self, root, width=400, height=400):
        self.root = root
        # Set the title of the window
        root.title("Let's learn some words")
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calculate position coordinates
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        # Position the window in the center of the screen and set the size
        root.geometry(f"{width}x{height}+{position_right}+{position_top}")
        # Set the placeholder for the counter of the word to be translated, e.g. 1/10, 2/10 etc.
        self.sequence_number = tk.Label(root, text=str(self.counter + 1) + "/10", font=("Arial", 20, "bold"))
        self.sequence_number.pack(padx=10, pady=10)  # Add padding

        self.word_to_translate = Label(root,
                                       text=current_lesson[self.counter][2] + " -> " + current_lesson[self.counter][1],
                                       font=("Arial", 16, "bold"))
        self.word_to_translate.pack(padx=10, pady=10)  # Add padding

        # Create an input field (Entry)
        self.input_field = Entry(root)
        # Add the input field to the window
        self.input_field.pack(padx=5, pady=1)
        self.input_field.bind("<Return>", lambda event=None: self.verify_input())
        self.input_field.focus_set()

        # Create a frame to contain the buttons
        frame = tk.Frame(root)
        # Create two buttons
        self.verify_button = tk.Button(root, text="Verify", command=self.verify_input)
        self.next_button = tk.Button(root, text="Next", command=self.next_word)
        # Use pack to place buttons at the bottom
        self.verify_button.pack(padx=5, pady=10)
        self.next_button.pack(padx=5, pady=5)

        # Binding the Enter key to the button's action
        self.next_button.bind("<Return>", lambda event=None: self.next_word())
        self.verify_button.bind("<Return>", lambda event=None: self.verify_input())

        self.msg_label_positive = tk.Label(root, text="", fg="green")
        self.msg_label_positive.pack(pady=1)
        self.msg_label_negative = tk.Label(root, text="", fg="red")
        self.msg_label_negative.pack(pady=5)

        self.results_positive = tk.Label(root, text="", fg="green")
        self.results_positive.pack(pady=10, padx=1)

        self.results_negative = tk.Label(root, text="", fg="red")
        self.results_negative.pack(pady=1, padx=1)

        self.close_app_button = tk.Button(root, text="Close App", command=self.close_app)
        self.close_app_button.bind("<Return>", lambda event=None: self.close_app())

        self.new_lesson_button = tk.Button(root, text="Start New Lesson", command=self.new_lesson)
        self.new_lesson_button.bind("<Return>", lambda event=None: self.new_lesson)

    def create_input_field(self):
        # Create an input field (Entry)
        self.input_field = Entry(root)
        # Add the input field to the window
        self.input_field.pack(padx=5, pady=1)
        self.input_field.bind("<Return>", lambda event=None: self.verify_input())

    def verify_input(self):
        value = self.input_field.get()
        # Example: Checking the value against a predefined value
        # Check if content is empty
        if not value.strip():
            self.wrong_answers = self.wrong_answers + 1
            self.msg_label_negative.config(text=current_lesson[self.counter][3])
            self.verify_button.config(state='disabled')
            self.next_button.focus_set()
        else:
            if re.search(value, current_lesson[self.counter][3]):
                self.msg_label_positive.config(text="It is correct!" + " " + current_lesson[self.counter][3])
                self.right_answers = self.right_answers + 1

                # take the number of correct translations from previous lessons
                english_word_to_find = current_lesson[int(self.counter)][2]


                print(pk.df_all_words_from_update_csv_file.loc[pk.df_all_words_from_update_csv_file['word_from'] == english_word_to_find, 4])
                historical_number_of_right_translations = pk.df_all_words_from_update_csv_file.loc[pk.df_all_words_from_update_csv_file['word_from'] == english_word_to_find, 4]
                new_number_of_right_translations = historical_number_of_right_translations + 1
                print(new_number_of_right_translations)

                # # update dataframe with the new number of correctly translated transactions
                #
                #
                # pk.df_all_words_from_update_csv_file.loc[pk.df_all_words_from_update_csv_file['word_from'] == english_word_to_find, 'number_of_completed_translations'] = new_number_of_right_translations
                # pk.df_all_words_from_update_csv_file.to_csv('test_lesson', index= False, header=True)
            else:
                self.msg_label_negative.config(text="It is incorrect!" + " " + current_lesson[self.counter][3])
                self.wrong_answers = self.wrong_answers + 1
            self.verify_button.config(state='disabled')
            self.next_button.focus_set()
    def next_word(self):
        self.verify_button.config(state='normal')
        # Example: Checking the value against a predefined value
        # Check if content is empty
        if not self.input_field.get().strip():
            self.wrong_answers = self.wrong_answers + 1
        if self.counter < 9:
            self.counter += 1
            self.sequence_number.config(text=str(self.counter + 1) + "/10", font=("Arial", 20, "bold"))
            self.word_to_translate.config(
                text=current_lesson[self.counter][2] + " -> " + current_lesson[self.counter][1],
                font=("Arial", 16, "bold"))
            self.msg_label_positive.config(text="")
            self.msg_label_negative.config(text="")
            self.input_field.delete(0, tk.END)
            self.input_field.focus_set()
        else:
            self.sequence_number.destroy()
            self.word_to_translate.destroy()
            self.input_field.destroy()
            self.verify_button.destroy()
            self.next_button.destroy()
            self.new_lesson_button.focus_set()
            self.msg_label_positive.destroy()
            self.msg_label_negative.destroy()
            # Use pack to place buttons at the bottom
            self.results_positive.config(text="Right answers - " + str(self.right_answers) + "/10")
            self.results_negative.config(text="Wrong answers - " + str(self.wrong_answers) + "/10")

            self.close_app_button.pack(padx=5, pady=10)
            self.new_lesson_button.pack(padx=5, pady=5)
            self.new_lesson_button.focus_set()

    def close_app(self):
        root.destroy()

    def new_lesson(self):
        self.close_app.destroy()
        self.new_lesson.destroy()
        counter = 0
        right_answers = 0
        wrong_answers = 0
        MainWindow(root)


# Create the main window
root = tk.Tk()
window = MainWindow(root)
root.mainloop()

# If you don't call root.mainloop() in your Tkinter application, the window will open and then immediately close,
# because there's nothing telling the program to keep the window open.
# So it's usually the last line in a simple Tkinter application.
