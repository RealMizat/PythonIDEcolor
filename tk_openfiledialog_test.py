import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()


__leading_double_underscore
Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass.Interpreter changes variable name with class extension and that feature known as the Mangling

.Python does not specify truly private so this ones can be call directly from other modules if it is specified in __all__, We also call it weak Private

Leading Underscore before variable/function/method name indicates to programmer that It is for internal use only, that can be modified whenever class want.

Python has their by default keywords which we can not use as the variable name. To avoid such conflict between python keyword and variable we use underscore after name



For ignoring values:

Multiple time we do not want return values at that time assign those values to Underscore. It used as throwaway variable.

filter_none


In Interpreter:
_ returns the value of last executed expression value in Python Prompt/Interpreter

Single Underscore:
In Interpreter
After a name
Before a name
Double Underscore:
__leading_double_underscore
__before_after__
