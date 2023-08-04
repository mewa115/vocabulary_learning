import tkinter as tk
import data_managemen as dm
import verify_the_input as vi
from tkinter import Tk, Entry, Button, Label, StringVar, messagebox
import data_managemen as dm

i = 0
current_lesson = dm.the_words_for_the_lesson()
print(current_lesson)
print(current_lesson[i][2])


def submit():
    # get the input from the Entry field
    entered_value = input_entry.get()
    if entered_value.lower() == current_lesson[i][2]:
        messagebox.showinfo("Correct!")
    else:
        messagebox.showinfo('The right translation is ', current_lesson[i][2])

root = Tk()

# Set the window title here
root.title("Let's Learn English Words")

# Set the window size (width x height)
window_width = 400
window_height = 400

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position coordinates
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Position the window in the center of the screen
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

input_var = StringVar()

while i < 9:
    # this block controls the sequence, e.g. 1/10, 2/10 etc.
    input_label = Label(root, text = str(i+1) + "/10", font=("Arial", 20, "bold"))
    input_label.pack(padx=5, pady=5)  # Add padding

# This controls the word for which I need to provide the translation
    input_label = Label(root, text=current_lesson[i][2], font=("Arial", 16, "bold"))
    input_label.pack(padx=5, pady=5)  # Add padding

input_label = Label(root, text="Provide the translation for the word:")
input_label.pack(padx=5, pady=15)  # Add padding

input_entry = Entry(root, textvariable=input_var)
input_entry.pack(padx=20, pady=20)  # Add padding

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

#root.bind('<Return>', get_input)

root.mainloop()







