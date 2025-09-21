from tkinter import *
top = Tk()
mb = Menubutton ( top, text = "5.11")
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.menu.add_checkbutton ( label = 'back', variable = aVar )
mb.pack()
top.mainloop()