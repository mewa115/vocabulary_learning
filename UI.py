import tkinter as tk
import re
import data_managemen as dm
from tkinter import Tk, Entry, Button, Label, StringVar, messagebox
import data_managemen as dm

counter = 0
current_lesson = dm.the_words_for_the_lesson()



# This class defines the default CSS characteristics of the main window
class MainWindow:
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


def verify_input():
    global input_field
    global next_button
    global current_lesson
    value = input_field.get()
    # Example: Checking the value against a predefined value
    # Check if content is empty
    if not value.strip():
        msg_label_negative.config(text=current_lesson[counter][3])
        verify_button.config(state='disabled')
        next_button.focus_set()
    else:
        if re.search(value, current_lesson[counter][3]):
            msg_label_positive.config(text="It is correct!" + " " + current_lesson[counter][3])
        else:
            msg_label_negative.config(text="It is incorrect!" + " " + current_lesson[counter][3])
        verify_button.config(state='disabled')
        next_button.focus_set()
def next_word():
    global counter
    verify_button.config(state='normal')
    if counter < 9:
        counter += 1
        sequence_number.config(text=str(counter + 1) + "/10", font=("Arial", 20, "bold"))
        word_to_translate.config(text=current_lesson[counter][2] + " -> " + current_lesson[counter][1], font=("Arial", 16, "bold"))
        msg_label_positive.config(text="")
        msg_label_negative.config(text="")
        input_field.delete(0, tk.END)
        input_field.focus_set()
    else:
        sequence_number.destroy()
        word_to_translate.destroy()
        input_field.destroy()
        verify_button.destroy()
        next_button.destroy()
        new_lesson.focus_set()
        # Use pack to place buttons at the bottom
        close_app.pack(padx=5, pady=10)
        new_lesson.pack(padx=5, pady=5)
def reset_window():
    global window
    global sequence_number
    counter == 0
    window = MainWindow(root)
    sequence_number= tk.Label(root, text=str(counter + 1) + "/10", font=("Arial", 20, "bold"))


def close_app():
    root.destroy()

# Create the main window
root = tk.Tk()
window = MainWindow(root)

# Set the placeholder for the counter of the word to be translated, e.g. 1/10, 2/10 etc.
sequence_number= tk.Label(root, text=str(counter + 1) + "/10", font=("Arial", 20, "bold"))
sequence_number.pack(padx=10, pady=10)  # Add padding

word_to_translate = Label(root, text=current_lesson[counter][2] + " -> " + current_lesson[counter][1], font=("Arial", 16, "bold"))
word_to_translate.pack(padx=10, pady=10)  # Add padding

# Create an input field (Entry)
input_field = Entry(root)
# Add the input field to the window
input_field.pack(padx=5, pady=1)
input_field.bind("<Return>", lambda event=None: verify_input())

# Create a frame to contain the buttons
frame = tk.Frame(root)
# Create two buttons
verify_button = tk.Button(root, text="Verify", command=verify_input)
next_button = tk.Button(root, text="Next", command=next_word)
# Use pack to place buttons at the bottom
verify_button.pack(padx=5, pady=10)
next_button.pack(padx=5, pady=5)
# Binding the Enter key to the button's action
next_button.bind("<Return>", lambda event=None: next_word())
verify_button.bind("<Return>", lambda event=None: verify_input())

msg_label_positive = tk.Label(root, text="", fg="green")
msg_label_positive.pack(pady=1)
msg_label_negative = tk.Label(root, text="", fg="red")
msg_label_negative.pack(pady=5)

close_app = tk.Button(root, text="Close App", command=close_app)
new_lesson = tk.Button(root, text="Start New Lesson",command=reset_window)

# If you don't call root.mainloop() in your Tkinter application, the window will open and then immediately close,
# because there's nothing telling the program to keep the window open.
# So it's usually the last line in a simple Tkinter application.
root.mainloop()

