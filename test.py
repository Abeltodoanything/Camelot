
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(char))

def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)

# Entry widget for display
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=3, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3)
]

# Create and position buttons
for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=10, 
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=3, pady=3)

# Equal button
equals_btn = tk.Button(root, text='=', padx=20, pady=10, command=calculate)
equals_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

# Run the application
root.mainloop()
