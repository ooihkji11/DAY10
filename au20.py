import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="samsung 1")
button2 = tk.Button(root, text="DELL 2")
button3 = tk.Button(root, text="HP 3")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()

root.mainloop()