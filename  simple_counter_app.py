import tkinter as tk

# Function to update the counter display
def update_display():
    counter_label.config(text=str(counter[0]))

# Function to increase the counter
def increase():
    counter[0] += 1
    update_display()

# Function to decrease the counter
def decrease():
    counter[0] -= 1
    update_display()

# Function to reset the counter with a new starting number
def reset():
    try:
        new_starting_number = int(starting_number_entry.get())
        counter[0] = new_starting_number
        update_display()
    except ValueError:
        # Handle invalid input
        counter_label.config(text="Invalid Number")

# Create the main window
root = tk.Tk()
root.title("Simple Counter App")

# Create a counter variable
counter = [0]

# Create and place the counter label with a larger font size
counter_label = tk.Label(root, text=str(counter[0]), font=('Arial', 48))
counter_label.pack(pady=20)

# Create and place the Increase button
increase_button = tk.Button(root, text="+1", command=increase, font=('Arial', 24))
increase_button.pack(side=tk.LEFT, padx=20)

# Create and place the Decrease button
decrease_button = tk.Button(root, text="-1", command=decrease, font=('Arial', 24))
decrease_button.pack(side=tk.RIGHT, padx=20)

# Create and place the Reset button
reset_button = tk.Button(root, text="Reset", command=reset, font=('Arial', 24))
reset_button.pack(side=tk.BOTTOM, pady=10)

# Create and place the entry for new starting number
starting_number_entry = tk.Entry(root, font=('Arial', 24))
starting_number_entry.pack(side=tk.BOTTOM, pady=10)

# Set initial value in the entry field
starting_number_entry.insert(0, "Enter new number")

# Start the main event loop
root.mainloop()
