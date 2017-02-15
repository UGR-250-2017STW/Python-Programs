# This program mirrors the meteor program in C++
# getting input from a GUI (ref page 542/543)
# This is for the STEM Festival programs

import tkinter  # page 529 simple GUI

import meteorStemStatus
import meteorStemUtils


class MeteorGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Meteor Simulation")
        self.main_window.minsize(width=550,height=100)   # set the window size

        # create frames for widgets....................see page 549
        # set up a frame for each widget to position them correctly
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.heading_frame = tkinter.Frame(self.main_window)    # has the title
        self.blank_frame1 = tkinter.Frame(self.main_window)
        self.diameter_frame = tkinter.Frame(self.main_window)
        self.blank_frame2 = tkinter.Frame(self.main_window)
        self.distance_frame = tkinter.Frame(self.main_window)
        self.blank_frame3 = tkinter.Frame(self.main_window)

        self.bottom_frame = tkinter.Frame(self.main_window)     # bottom frame for buttons


        # create widgets for the top frame
        self.blank_label1 = tkinter.Label(self.top_frame, text=' ')
        self.heading_label = tkinter.Label(self.heading_frame, \
                                          text='Meteor Defense System Simulation', font=("Helvetica",18), fg="blue")

        self.blank_label2 = tkinter.Label(self.blank_frame1, text=' ')
        self.blank_label3 = tkinter.Label(self.blank_frame2, text=' ')



    # the Enry widgets
        self.diameter_label = tkinter.Label(self.diameter_frame, \
                                          text='Enter the meteor diameter in meters:  ', font=("Helvetica",10))
        self.diameter_entry = tkinter.Entry(self.diameter_frame, width = 20)
        self.diameter_entry.insert(0, 3)
            

        self.distance_label = tkinter.Label(self.distance_frame, \
                                          text='     Enter the meteor distance from Earth in miles:  ', font=("Helvetica",10))

        self.distance_entry = tkinter.Entry(self.distance_frame, width = 20)
        self.distance_entry.insert(0, 500)


        # pack (position and order) the top frame's widgets
        self.blank_label1.pack(side = 'top')
        self.heading_label.pack(side = 'top')
        self.blank_label2.pack(side = 'top')

        self.diameter_label.pack(side = 'left')
        self.diameter_entry.pack(side = 'left')
        self.blank_label3.pack(side = 'left')
        
        self.distance_label.pack(side = 'left')
        self.distance_entry.pack(side = 'left')

        

        # create the button widgets and label for the bottom frame
        self.blank_label4 = tkinter.Label(self.bottom_frame, text=' ')
        self.runSim_button = tkinter.Button(self.bottom_frame, \
                                            text='Run Simulation', command=self.processData)
        self.blank_label5 = tkinter.Label(self.bottom_frame, text=' ')
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
                                          command=self.main_window.destroy)
        self.blank_label6 = tkinter.Label(self.bottom_frame, text=' ')

        
        

        # pack the blank label and buttons in the bottom frame
        self.blank_label4.pack()
        self.runSim_button.pack()
        self.blank_label5.pack()
        self.quit_button.pack()
        self.blank_label6.pack()

        # pack the frames
        self.top_frame.pack()
        self.heading_frame.pack()
        self.blank_frame1.pack()
        self.diameter_frame.pack()
        self.blank_frame2.pack()
        self.distance_frame.pack()
        self.blank_frame3.pack()

        self.bottom_frame.pack()


    # Retrieve the data from the text box and call the function in meteorCalc
    def processData(self):
         
        diam = (self.diameter_entry.get())
        distance = (self.distance_entry.get())

        badDiam = False
        badDistance = False

        tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and diam is: ' + str(diam))
        tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and distance is: ' + str(distance))

        if meteorStemUtils.validInput(diam) == False:
            diam = '3'
            badDiam = True
            tkinter.messagebox.showinfo('Bad Input Provided ', 'badDiam now equals ' + str(badDiam))
            


        tkinter.messagebox.showinfo('BACK IN MAIN', 'Checking for valid distance now and badDistance is: ' + str(badDistance))

        if meteorStemUtils.validInput(distance) == False:
            distance = '500'
            badDistance = True
            tkinter.messagebox.showinfo('Bad Input Provided ', 'badDistance now equals ' + str(badDistance))


        if badDiam == True or badDistance == True:
            tkinter.messagebox.showinfo('Bad Input Provided!', 'Bad input received.\n  Diameter:  "' + str(diam) +
                                         '" \n  Distance: "' + str(distance) + '" \n\nRunning with 3 meters at 500 miles.')
          

     #   if meteorStemUtils.validInput(diam) != True or meteorStemUtils.validInput(distance) != True:
      #       tkinter.messagebox.showinfo('Bad Input Provided!', 'Bad input received.\n  Diameter:  "' + str(diam) +
       #                                  '" \n  Distance: "' + str(distance) + '" \n\nRunning with 3 meters at 500 miles.')
       #      diam = 3
        #     distance = 500


             
        simRunning = False  # inserted for iconify and de-iconify, could use pack_forget, and then pack() again
        
        # disable the Run Simulation button until it completes
        self.runSim_button['state']='disabled'

        # iconify the main window
        #self.main_window.iconify()
        
        meteorStemStatus.runSimulation(diam,distance, simRunning)
        
        # Enter the tkinter main loop
        tkinter.mainloop()

       # after the sim runs, de iconify
        if simRunning == False:
            self.main_window.deiconify()

# create an instance of the class
meteor_sim = MeteorGUI()
