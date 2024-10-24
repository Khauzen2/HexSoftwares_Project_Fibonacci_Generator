# This is my version of The Fibonacci Generation system using tkinker and messagebox modules

import tkinter as tk
from tkinter import messagebox

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Function to handle button click and display the result
def show_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        fib_sequence = generate_fibonacci(n)
        result = ", ".join(map(str, fib_sequence))
        
        # Show the result in a pop-up window
        messagebox.showinfo("Fibonacci Sequence", f"The first {n} numbers: {result}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
window = tk.Tk()
window.title("Fibonacci Generator")

# Label and input field
label = tk.Label(window, text="Enter the number of Fibonacci numbers to generate:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

# Button to generate Fibonacci sequence
button = tk.Button(window, text="Generate", command=show_fibonacci)
button.pack(pady=20)

# Start the GUI loop
window.mainloop()


