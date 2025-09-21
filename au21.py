import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

# Create three labels
label1 = tk.Label(root, text="ahmad")
label2 = tk.Label(root, text="hamzah")
label3 = tk.Label(root, text="rajah")

# Grid the labels in a 2x2 grid
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop()