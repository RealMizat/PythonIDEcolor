from tkinter import *
root = Tk()
root.title=('Title Goes Here')
root.geometry('400x300')

menu = Menu(root)
root.config(menu=menu)


def close():     #Cannot be named exit as it is the command/function
    exit()

subm = Menu(menu)
menu.add_cascade(label='File', menu = subm)
subm.add_command(label='Save')
subm.add_command(label='EXIT',command=close)     #Cannot name exit, it is function


sub1 = Menu(menu)
menu.add_cascade(label='Tools',menu=sub1)
sub1.add_command(label='color')

root.mainloop()
