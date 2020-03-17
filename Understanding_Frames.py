from tkinter import *

class GreenFrame(Frame) :
    def __init__(self, the_window) :
        super().__init__()
        self["height"]=200
        self["width"]=200
        self["relief"]=RAISED
        self["bd"]=14
        self["bg"]="green"



class BlueFrame(Frame) :
    def __init__(self, the_window) :
        super().__init__()
        self["height"]=50
        self["width"]=70
        self["relief"]=RAISED
        self["bd"]=9
        self["bg"]='blue'
        

my_window=Tk()
my_window.title('TK - Frames')
my_window.geometry('280x520+425+450') #width x height + x axis + y axis

'''
#COULD USE:   winfo_screenwidth()/2   winfo_screenheight()/2   -for center
then use width/2 height/2  =>subtract half w&h from winfo above.
'''

my_window.resizable(width=False, height=False)

frame_a=GreenFrame(my_window)
frame_b=GreenFrame(my_window)
frame_a.grid(row=0, column=0)
frame_b.grid(row=1, column=0)

frame_c=BlueFrame(my_window)
frame_c.grid(row=1, column=1)
label_1 = Label(my_window, text ='Choose Type', font="Ubuntu 22")
label_1.grid(row = 2, column = 0, pady=25)

label_2=Label(my_window, text="TEQ", font="Deja 12")
label_2.grid(row=0, column=0)

my_window.mainloop()

             
