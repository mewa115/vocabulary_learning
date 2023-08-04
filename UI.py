import tkinter as tk
import data_managemen as dm
import verify_the_input as vi
from tkinter import Tk, Entry, Button, Label, StringVar, messagebox
import data_managemen as dm

counter = 0

current_lesson = dm.the_words_for_the_lesson()

def action_on_submit():
    global counter
    entered_value = input_field.get()
    if entered_value.lower() == current_lesson[counter][3]:
        messagebox.showinfo("Correct!")
    else:
        messagebox.showinfo('The right translation is ', current_lesson[counter][3])
    sequence.set(str(counter + 1) + "/10".format(counter))
    if counter >= 10:
        print("Lesson is over")

    counter += 1


class MainWindow:
    def __init__(self, root, width=400, height=400):
        self.root = root
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calculate position coordinates
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        # Position the window in the center of the screen and set the size
        root.geometry(f"{width}x{height}+{position_right}+{position_top}")


# Create the main window
root = tk.Tk()
# Set the window title here
root.title("Let's Learn English Words")

window = MainWindow(root)

# Set the placeholder for the counter of the word to be translated, e.g. 1/10, 2/10 etc.
sequence = Label(root, text=str(counter + 1) + "/10", font=("Arial", 20, "bold"))
sequence.pack(padx=10, pady=10)  # Add padding

# Set the placeholder for the word to be translated
word_to_translate = Label(root, text=current_lesson[counter][2], font=("Arial", 16, "bold"))
word_to_translate.pack(padx=10, pady=10)  # Add padding

# Create an input field (Entry)
input_field = tk.Entry(root)
# Add the input field to the window
input_field.pack(padx=10, pady=10)

# Set the functionality behind the button
button = tk.Button(root, text="Verify", command=action_on_submit)
# Add the button to the window
button.pack()

# If you don't call root.mainloop() in your Tkinter application, the window will open and then immediately close,
# because there's nothing telling the program to keep the window open.
# So it's usually the last line in a simple Tkinter application.
root.mainloop()
