import tkinter as tk

def submit():
    user_input = input_field.get()
    result = backend_function(user_input)  # Replace backend_function with your actual backend logic
    result_label.config(text=": " + result)

# Create the main window
window = tk.Tk()
window.title("Simple UI Example")

# Create the result label at the top
result_label = tk.Label(window, text="Result: ")
result_label.pack(padx=10, pady=10)

# Create the input field with margins
input_field = tk.Entry(window)
input_field.pack(padx=10, pady=10)

# Create the submit button with margins
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(padx=10, pady=10)

# Create the section to display the output with margins
output_section = tk.Label(window)
output_section.pack(padx=10, pady=10)

# Start the main loop
window.mainloop()
