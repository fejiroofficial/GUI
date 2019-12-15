from tkinter import *

window = Tk()

def rupee_to_dollar():
    t1.delete("1.0", END)
    dollar = float(e1_value.get()) * 0.014
    t1.insert(INSERT, dollar)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0, padx=10, pady=20)

b1 = Button(
    window,
    text="covert",
    command=rupee_to_dollar,
    bg="green",
    fg="white",
    bd=0,
    )
b1.grid(row=0, column=2, padx=10)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=4, padx=10)

window.mainloop()
