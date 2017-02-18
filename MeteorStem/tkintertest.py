import tkinter

class MyGUI:
    def __init__(self):
        # main window widget
        # main_window -> frame -> labels
        self.main_window = tkinter.Tk()

        # frame container to hold widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # label widget 
        self.label1 = tkinter.Label(self.top_frame, \
                # display text
                text='Science Slam 2017')
        self.label2 = tkinter.Label(self.top_frame, \
                text='Presented by RCBC UGR-250 group')

        # displays widget
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        self.label3 = tkinter.Label(self.bottom_frame, \
                text='This is a python program using the Tk interface')

        self.label3.pack(side='bottom')

        self.top_frame.pack()
        self.bottom_frame.pack()

        # infinite loop to keep the window displayed
        tkinter.mainloop()

my_gui = MyGUI()
