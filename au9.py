import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Printing: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Printing: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["DELL 1", "HP 2", "Canon 3"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Printer")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()