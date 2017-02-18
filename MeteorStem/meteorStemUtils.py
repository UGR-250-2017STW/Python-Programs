
# this file contains utility functions for the program

# these are here to show data for testing only

import tkinter
import tkinter.messagebox

# validates that a float has been entered
def validInput(txt):


   # tkinter.messagebox.showinfo('In validInput', 'Arrived in validInput with the value : ' + str(txt))

    try:
        float(txt)
        tkinter.messagebox.showinfo('In validInput', ' try clause returning TRUE : ' + str(txt))
        return True
    except ValueError:
        tkinter.messagebox.showinfo('In validInput', ' except clause returning FALSE : ' + str(txt))
        return False
    
 



# file reserved for error checking
