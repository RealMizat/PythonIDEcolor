#This as a base I am going to create a color scheme pallete saver
#Hope I will soon have time to save color palletes and view them
#I will be using code similar to the other files in this project
#That makes each of them good starting points for something.

#End goal will be to apply themes to IDEs. Pythons default first then Visual Studio Code

#Once I get time, a good day of so. First I will be adding Frames or a Canvas to
# view the color swatches, and then tool bar, save to save color numbers
#Then a button to change pythons deafult IDE, creating a custom theme
#of the colors you choose.
import tkinter as tk

from tkinter.colorchooser import *

root = tk.Tk()

root.title('Color Swatch')
root.minsize(width=450, height=600)

def clr_clicked():
    color = askcolor()
    print(color)
    b_show.configure(bg = color[1])

def reset_clr() :
    b_show.configure(bg = 'white')

label1 = tk.Label(root, text = 'Tools')
label1.grid(row = 2, column = 1)

label2 = tk.Label(root, text = 'Text Editor')
label2.grid(row = 1, column = 4)

text_area = tk.Text(root, height = 6)
text_area.grid(row = 3, column = 2, rowspan = 3, columnspan = 5, sticky='S')

b_clr = tk.Button(root, text = "Color", command = clr_clicked, bg="black", fg="purple")
b_clr.grid(row = 2, column = 3)


b_show = tk.Button(root,text = 'SHOW', fg = 'white', command = reset_clr)
b_show.grid(row = 2, column = 5)

root.mainloop()


''' this color chooser will save custom colors until the application is closed
make sure to choose the color square you want the color to be placed if you just
opened the color chooser. Once opened it will automatically place the color in the
first box

There is a lot of potential using this as a starting point.

you could use the text widget to do everything from printing/drawing/both
the colors choosen, to saving the color numbers to another file with the
os package. If you plan to do either of those you should look into the text
widget and learn about tags and marks. If you can undertstand and make use of
all the text widgets widgets and functions you can make anything. it is a better
version of canvas once understood. You may embed buttons, drawings windows
and anything else, or just take users text and write them to a new or current
file.

I plan to merge this with two other scripts I have, and then ading some quick
functionality.

Menu buttons File and Edit will be avaible with sub-menus. The exit sub menu
button works. I plan to add some file saving and opening, to offer some quick
text editing. I basically already have the code written.

I would like to add frames, or a few canvas, or maybe just somehting in the
text widget, this would allow the colors to be viewd and saved to pallets
and or swatches, that can be viewed at later times, this allowing the user
to build custom color schemes they like.

That is the next step once I find time, I am also working on a game so I don't
have as much as I would like. The end goal is to be able to save color schemes
and implement them on IDE's. The builf in Python IDE will be obvious, as it
will be very easy to edit the file. Then Visual Studio Code, maybe Atom, if possible
PyCharm however they have a custom format i'm not sure about

That is my end goal. It is way to hard to edit themes in most IDEs. I don't
understand why there isn't a better option than the Java Visual Studio Code
npm color scheme tool, witch isn't easy to use and makes you download java.

that wawy a simple begginer and any user app exists to change color schemes and
store the colors they like. I may just have the colors be assigned randomly to
different properties, and you can just keep refreshing until it looks good.
or it will be basic, because there are tons of different areas/syantax that can be
colored'''
