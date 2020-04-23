from tkinter import *

root = Tk()
root.resizable(0,0)

#Display
e = Entry(root , width = 25)
e.grid(row = 1,column = 1, columnspan = 3, padx = 5, pady = 5)


def push(no):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(no))

def button_clear():
    e.delete(0, END)
    add_list.clear()

add_list = []

def button_add():
    add_list.append(int(e.get()))
    e.delete(0, END)
    print(add_list)

def equal():
    add_list.append(int(e.get()))
    e.delete(0, END)
    print(add_list)
    e.insert(0, sum(add_list))

#iniatialize widgets
but0 = Button(root, text = "0", command = lambda: push(0), padx = 20, pady = 20)
but1 = Button(root, text = "1", command = lambda: push(1), padx = 20, pady = 20)
but2 = Button(root, text = "2", command = lambda: push(2), padx = 20, pady = 20)
but3 = Button(root, text = "3", command = lambda: push(3), padx = 20, pady = 20)
but4 = Button(root, text = "4", command = lambda: push(4), padx = 20, pady = 20)
but5 = Button(root, text = "5", command = lambda: push(5), padx = 20, pady = 20)
but6 = Button(root, text = "6", command = lambda: push(6), padx = 20, pady = 20)
but7 = Button(root, text = "7", command = lambda: push(7), padx = 20, pady = 20)
but8 = Button(root, text = "8", command = lambda: push(8), padx = 20, pady = 20)
but9 = Button(root, text = "9", command = lambda: push(9), padx = 20, pady = 20)
but_add = Button(root, text = "ADD", command = lambda: button_add(), padx = 11, pady = 20)
but_clear = Button(root, text = "CLEAR", command = button_clear, padx = 5.5, pady = 20)
but_equal = Button(root, text = "=", command = equal, padx = 75, pady = 20)

#Position Widgets
but1.grid(row = 2, column = 1)
but2.grid(row = 2, column = 2)
but3.grid(row = 2, column = 3)

but4.grid(row = 3, column = 1)
but5.grid(row = 3, column = 2)
but6.grid(row = 3, column = 3)

but7.grid(row = 4, column = 1)
but8.grid(row = 4, column = 2)
but9.grid(row = 4, column = 3)

but0.grid(row = 5, column = 1)
but_add.grid(row = 5, column = 2)
but_clear.grid(row = 5, column = 3)
but_equal.grid(row = 6,column = 1, columnspan = 3)

root.mainloop()  