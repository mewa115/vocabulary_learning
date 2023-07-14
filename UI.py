import tkinter as tk
import data_managemen as dm
import verify_the_input as vi



def submit():
    user_input = input_field.get()
    return(user_input)

#    result = user_input  # Replace backend_function with your actual backend logic
#    result_label.config(text=": " + result)





# Create the main window
window = tk.Tk()
window.title("Let's Learn New Words")

# Pick up the words for the current lesson
dm.return_the_words_for_the_lesson()

# Create the result label at the top
result_label = tk.Label(window, text="Translate the word: ")
result_label.pack(padx=10, pady=10)

# Create the input field with margins
input_field = tk.Entry(window)
input_field.pack(padx=10, pady=10)

# Create the submit button with margins
submit_button = tk.Button(window, text="Verify", command=submit)
submit_button.pack(padx=10, pady=10)

# Create the section to display the output with margins
output_section = tk.Label(window)
output_section.pack(padx=10, pady=10)

# Start the main loop
window.mainloop()
