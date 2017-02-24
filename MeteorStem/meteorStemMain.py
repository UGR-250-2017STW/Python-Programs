# This program mirrors the meteor program in C++
# getting input from a GUI (ref page 542/543)
# This is for the STEM Festival programs

import tkinter
from PIL import ImageTk, Image

import time

import math

import meteorStemStatus
import meteorStemUtils


class MeteorGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()
        w, h = self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()
        self.main_window.overrideredirect(1)           # potentially malicious line
        self.main_window.title("Meteor Simulation")
        self.main_window.minsize(width=w,height=h)   # set the window size

        # create frames for widgets....................see page 549
        # set up a frame for each widget to position them correctly
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.heading_frame = tkinter.Frame(self.main_window)    # has the title
        self.earth_frame = tkinter.Frame(self.main_window)
        self.earth_image = ImageTk.PhotoImage(Image.open('earth.png'))
        self.meteor_image = ImageTk.PhotoImage(Image.open('meteor.png'))
        self.earth_label = tkinter.Label(self.earth_frame, image=self.earth_image)
        self.meteor_label = tkinter.Label(self.earth_frame, image=self.meteor_image)

        #self.blank_frame1 = tkinter.Frame(self.main_window)
        self.diameter_frame = tkinter.Frame(self.main_window)
        #self.blank_frame2 = tkinter.Frame(self.main_window)
        self.distance_frame = tkinter.Frame(self.main_window)
        #self.blank_frame3 = tkinter.Frame(self.main_window)


        self.bottom_frame = tkinter.Frame(self.main_window)     # bottom frame for buttons


        # create widgets for the top frame
        #self.blank_label1 = tkinter.Label(self.top_frame, text=' ')
        self.heading_label = tkinter.Label(self.heading_frame, \
                                          text='Meteor Defense System Simulation', font=("Helvetica",18), fg="blue")



        #self.blank_label2 = tkinter.Label(self.blank_frame1, text=' ')
        #self.blank_label3 = tkinter.Label(self.blank_frame2, text=' ')



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
        #self.blank_label1.pack()
        self.heading_label.pack()
        #self.blank_label2.pack()

        self.diameter_label.pack(side='left')
        self.diameter_entry.pack(side='left')
        self.earth_label.pack()
        self.meteor_label.pack()
        #self.blank_label3.pack()
        
        self.distance_label.pack(side='left')
        self.distance_entry.pack(side='left')

        

        # create the button widgets and label for the bottom frame
        #self.blank_label4 = tkinter.Label(self.bottom_frame, text=' ')
        self.runSim_button = tkinter.Button(self.bottom_frame, \
                                            text='Run Simulation', command=self.processData)
        #self.blank_label5 = tkinter.Label(self.bottom_frame, text=' ')
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
                                          command=self.main_window.destroy)
        #self.blank_label6 = tkinter.Label(self.bottom_frame, text=' ')

        
        

        # pack the blank label and buttons in the bottom frame
        #self.blank_label4.pack()
        self.runSim_button.pack()
        #self.blank_label5.pack()
        self.quit_button.pack()
        #self.blank_label6.pack()

        # pack the frames
        self.top_frame.pack()
        self.heading_frame.pack()
        self.earth_frame.pack(ipadx=100, ipady=100)
        #self.blank_frame1.pack()
        self.diameter_frame.pack()
        #self.blank_frame2.pack()
        self.distance_frame.pack()
        #self.blank_frame3.pack()

        self.bottom_frame.pack()
        tkinter.mainloop()

    # Retrieve the data from the text box and call the function in meteorCalc
    def processData(self):
        self.runSim_button.config(text='Launch')
        diam = (self.diameter_entry.get())
        diam = float(diam)
        distance = (self.distance_entry.get())
        distance = float(distance)
        meteorSpeed = float(120 * diam)
        badDiam = False
        badDistance = False

        self.diameter_notice_label = tkinter.Label(self.diameter_frame, \
                                                   text='NOTICE Heding into ifs now and diam is: {}'.format(diam))
        self.distance_notice_label = tkinter.Label(self.distance_frame, \
                                                   text='NOTICE Heading into ifs now and distance is: {}'.format(distance))
        self.diameter_notice_label.pack()
        self.distance_notice_label.pack()


        #tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and diam is: ' + str(diam))
        #tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and distance is: ' + str(distance))

        if meteorStemUtils.validInput(diam) == False:
            diam = '3'
            badDiam = True
            self.badDiam_label = tkinter.Label(self.diameter_frame, \
                                               text='Bad Input Provided badDiam now equals ' + str(badDiam))
            self.badDiam_label.pack()
            #tkinter.messagebox.showinfo('Bad Input Provided ', 'badDiam now equals ' + str(badDiam))
            


        #tkinter.messagebox.showinfo('BACK IN MAIN', 'Checking for valid distance now and badDistance is: ' + str(badDistance))
        self.badDistance_label = tkinter.Label(self.distance_frame, \
                                               text='BACK IN MAIN Checking for valid distance now and badDistance is: ' + str(badDistance))
        self.badDistance_label.pack()
        self.badDistance_label.config(text='TEST') # this is how I'll update a label within a loop
        for i in range(math.ceil(distance * 60 / meteorSpeed)):
            distance = distance - (meteorSpeed / 60)
            self.badDistance_label.config(text='Distance is now ' + str(distance))
            if(distance >= 1200 and distance <= 1400):
                self.runSim_button.config(background='green')
            elif(distance <= 0):
                self.main_window.destroy()
            else:
                self.runSim_button.config(background='red')
            self.main_window.update()
            #self.main_window.after_idle(self.badDistance_label.config(text='Distance is now: '.format(distance)))
            time.sleep(1)
        if meteorStemUtils.validInput(distance) == False:
            distance = '500'
            badDistance = True
            self.badDistance_label.config(text='Bad Input Provided badDistance now equals ' + str(badDistance))

            #tkinter.messagebox.showinfo('Bad Input Provided ', 'badDistance now equals ' + str(badDistance))


        #if badDiam == True or badDistance == True:
            #tkinter.messagebox.showinfo('Bad Input Provided!', 'Bad input received.\n  Diameter:  "' + str(diam) +
                                         #'" \n  Distance: "' + str(distance) + '" \n\nRunning with 3 meters at 500 miles.')

        simRunning = False  # inserted for iconify and de-iconify, could use pack_forget, and then pack() again
        
        # disable the Run Simulation button until it completes
        #self.runSim_button['state']='disabled'

        # iconify the main window
        #self.main_window.iconify()
        
        meteorStemStatus.runSimulation(diam,distance, simRunning)
        
        # Enter the tkinter main loop

        tkinter.self.main_window.mainloop()

       # after the sim runs, de iconify
        if simRunning == False:
            self.main_window.deiconify()

    def runSimulation(diam, distance, simRunning):

        simRunning = True       # to let main loop know to deiconify the entry window

        #tkinter.messagebox.showinfo('Now in runSim function and boolean flag is ', str(simRunning))


        # type conversion page 64
        diamFloat = float(diam)
        distanceFloat = float(distance)


        # boolean vars page 111
        meteorInbound = True
        meteorSpeed = float(120 * diamFloat)
        meteorDistance = distanceFloat


        # showinfo page 538, output formatting page 69
        #tkinter.messagebox.showinfo('Now in runSim function', 'The speed is ' + format(meteorSpeed, '.2f'))




        # Generating another window for status output
        #status_window = tkinter.Tk()
        #status_window.title("System Status")
        #status_window.minsize(width=450,height=200)

        #status_window.geometry('600x400+50-100')   # width, ht, 50 pixels in from left, and 100 up from bottom


        # create frames for widgets....................see page 549
        # set up a frame for each widget to position them correctly

        #status_window.top_frame = tkinter.Frame(status_window)
        #status_window.bottom_frame = tkinter.Frame(status_window)



        # create widgets for the top frame, creating stringVars for text updates and output
        status_window.distanceValue = tkinter.StringVar()
        # convert distance to string and store it - page 546
        status_window.distanceValue.set(distanceFloat)

        status_window.blank_label1 = tkinter.Label(status_window.top_frame, text=' ')
        status_window.distance_label = tkinter.Label(status_window.top_frame, \
                                                text='Meteor Distance = '+ format(distanceFloat, '.2f'))
        status_window.distanceFloatValue = tkinter.Label(status_window.top_frame, \
                                                   textvariable=status_window.distanceValue)    # page 546


        # pack (position and order) the top frame's widgets
        status_window.blank_label1.pack(side='top')
        status_window.distance_label.pack(side='left')
        status_window.distanceFloatValue.pack(side='left')



        # create the button widget and label for the bottom frame
        status_window.blank_labelb = tkinter.Label(status_window.bottom_frame, text=' ')
        status_window.updateSim_button = tkinter.Button(status_window.bottom_frame, \
                                                text='Update Simulation', command = simUpdate(distance, diam))


        # pack the blank label and buttons in the bottom frame
        status_window.blank_labelb.pack()
        status_window.updateSim_button.pack()



        # pack the frames
        status_window.top_frame.pack()
        status_window.bottom_frame.pack()

        status_window.lift()    # make it on top
        #tkinter.mainloop()



        #loops page 122, boolean vars page 111

        # call back function for the update button
    def simUpdate(distance, diam):
        distanceData = float(distance)
        diamData = float(diam)
        meteorSpeed = float(120 * diamData)
        #tkinter.messagebox.showinfo('In while loop now', 'The distance is ' + format(distanceData, '.2f'))

        # update the status
        while distanceData > 0:
            distanceData = distanceData - (meteorSpeed/60)
            #tkinter.messagebox.showinfo('In while loop now', 'The distance is ' + format(distanceData, '.2f'))

        simRunning = False

# create an instance of the class
meteor_sim = MeteorGUI()
