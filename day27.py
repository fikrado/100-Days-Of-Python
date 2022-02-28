from tkinter import *


def conver():
    miles = float(e1.get())
    km = miles * 1.609
    l4.config(text=km)

# Window----------------
window = Tk()
window.title("MILES  TO  KILOMETER  CONVERTER")
window.config(padx=28, pady=28)

# Lebels----------------
l1 = Label(text="Miles")
l1.grid(column=3, row=1)
l2 = Label(text="km")
l2.grid(column=3, row=2)
l3 = Label(text="is equal to")
l3.grid(column=1, row=2)
l4 = Label(text="mile = km")
l4.grid(column=2, row=2)

# Entry-------------------
e1 = Entry(width=12)
e1.grid(column=2, row=1)


# Buttom----------------
b = Button(text="calculate", command=conver)
b.grid(column=2, row=3)

window.mainloop()