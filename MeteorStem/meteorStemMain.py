# This program mirrors the meteor program in C++
# getting input from a GUI (ref page 542/543)
# This is for the STEM Festival programs

import tkinter
from random import randrange, randint
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
        # self.main_window.overrideredirect(1)           # potentially malicious line
        self.main_window.title("Meteor Simulation")
        self.main_window.minsize(width=w, height=h)  # set the window size

        # create frames for widgets....................see page 549
        # set up a frame for each widget to position them correctly
        self.earth_y = 400
        self.earth_x = 1000

        self.top_frame = tkinter.Frame(self.main_window)
        self.heading_frame = tkinter.Frame(self.main_window)  # has the title
        self.canvas_h = 800
        self.canvas_w = 2000
        self.earth_canvas = tkinter.Canvas(self.main_window, width=self.canvas_w, height=self.canvas_h, bg="black")
        self.explosion_image = Image.open('explosion.png')
        self.explosion_photo_image = ImageTk.PhotoImage(self.explosion_image)
        self.earth_image = Image.open('earth.png')
        self.earth_photo_image = ImageTk.PhotoImage(self.earth_image)
        self.meteor_image = Image.open('meteor.png')
        self.meteor_photo_image = ImageTk.PhotoImage(self.meteor_image)
        self.meteor_x = 0
        self.meteor_y = 0
        self.meteor_dx = 1
        self.meteor_dy = 1
        self.meteor_deltaerr = self.earth_y/self.earth_x
        self.meteor_err = self.meteor_deltaerr - 0.5
        self.meteor_drr = 1
        self.meteor_h = 250
        self.meteor_w = 250
        self.rocket_x = 1050
        self.rocket_y = 400
        self.rocket_h = 10
        self.rocket_w = 20
        self.rocket_dy = 5
        self.rocket_dx = 5

        # self.blank_frame1 = tkinter.Frame(self.main_window)
        self.diameter_frame = tkinter.Frame(self.main_window)
        # self.blank_frame2 = tkinter.Frame(self.main_window)
        self.distance_frame = tkinter.Frame(self.main_window)
        # self.blank_frame3 = tkinter.Frame(self.main_window)


        self.bottom_frame = tkinter.Frame(self.main_window)  # bottom frame for buttons

        # create widgets for the top frame
        # self.blank_label1 = tkinter.Label(self.top_frame, text=' ')
        self.heading_label = tkinter.Label(self.heading_frame, \
                                           text='Meteor Defense System Simulation', font=("Helvetica", 18), fg="blue")

        # self.blank_label2 = tkinter.Label(self.blank_frame1, text=' ')
        # self.blank_label3 = tkinter.Label(self.blank_frame2, text=' ')



        # the Enry widgets
        self.diameter_label = tkinter.Label(self.diameter_frame, \
                                            text='Enter the meteor diameter in meters:  ', font=("Helvetica", 10))
        self.diameter_entry = tkinter.Entry(self.diameter_frame, width=20)
        self.diameter_entry.insert(0, 3)

        self.distance_label = tkinter.Label(self.distance_frame, \
                                            text='     Enter the meteor distance from Earth in miles:  ',
                                            font=("Helvetica", 10))

        self.distance_entry = tkinter.Entry(self.distance_frame, width=20)
        self.distance_entry.insert(0, 300)

        # pack (position and order) the top frame's widgets
        # self.blank_label1.pack()
        self.heading_label.pack()
        # self.blank_label2.pack()

        self.diameter_label.pack(side='left')
        self.diameter_entry.pack(side='left')
        # self.blank_label3.pack()

        self.distance_label.pack(side='left')
        self.distance_entry.pack(side='left')

        # create the button widgets and label for the bottom frame
        # self.blank_label4 = tkinter.Label(self.bottom_frame, text=' ')
        self.runSim_button = tkinter.Button(self.bottom_frame, \
                                            state='normal', text='Run Simulation', command=self.processData)
        # self.runSim_button = tkinter.Button(self.bottom_frame, \
        # text='Run Simulation', command=self.processData)
        # self.blank_label5 = tkinter.Label(self.bottom_frame, text=' ')
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
                                          command=self.main_window.destroy)
        # self.blank_label6 = tkinter.Label(self.bottom_frame, text=' ')





        # pack the blank label and buttons in the bottom frame
        # self.blank_label4.pack()
        self.runSim_button.pack()
        # self.blank_label5.pack()
        self.quit_button.pack()
        # self.blank_label6.pack()

        # pack the frames
        self.top_frame.pack()
        self.heading_frame.pack()
        self.earth_canvas.pack()
        self.earth_canvas_image = self.earth_canvas.create_image(self.earth_x, self.earth_y, image=self.earth_photo_image)
        self.meteor_canvas_image = self.earth_canvas.create_image(int(self.meteor_x), int(self.meteor_y),
                                                                  image=self.meteor_photo_image)
        # self.blank_frame1.pack()
        self.diameter_frame.pack()
        # self.blank_frame2.pack()
        self.distance_frame.pack()
        # self.blank_frame3.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def animate_meteor(self, cancel=False):
        if cancel==False:
            self.draw_one_meteor_frame()
            self.distance = self.distance - (self.meteorSpeed / 60/10)
            self.distance_label.config(text='Distance is now {:d}'.format(int(self.distance)))
            if (int(self.distance) >= 1200 and int(self.distance) <= 1400):
                self.runSim_button.config(background='green', command=self.animate_rocket_success)
            else:
                self.runSim_button.config(background='red',command=self.animate_rocket_fail)
            self.animate_meteor_id = self.main_window.after(50, self.animate_meteor)
        else:
            self.explosion_image = Image.open('explosion.png')
            self.explosion_image = self.explosion_image.resize((self.meteor_w+40, self.meteor_h+40), Image.ANTIALIAS)
            self.explosion_photo_image = ImageTk.PhotoImage(self.explosion_image)
            self.explosion_canvas_image = self.earth_canvas.create_image(int(self.meteor_x), int(self.meteor_y),
                                                                         image=self.explosion_photo_image)
            self.main_window.after_cancel(self.animate_meteor_id)

    def animate_rocket_fail(self, cancel=False):
        self.runSim_button.config(state='disabled')
        self.rocket_h += 2
        self.rocket_w += 2
        self.rocket_x -= 5
        self.rocket_y -= 5
        self.rocket_image = Image.open('rocket.png')
        self.rocket_image = self.rocket_image.resize((self.rocket_h, self.rocket_w), Image.ANTIALIAS)
        self.rocket_photo_image = ImageTk.PhotoImage(self.rocket_image)
        self.rocket_canvas_image = self.earth_canvas.create_image(int(self.rocket_x), int(self.rocket_y),
                                                                  image=self.rocket_photo_image)
        self.animate_rocket_fail_id =self.main_window.after(100, self.animate_rocket_fail)

    def animate_rocket_success(self, cancel=False):
        if self.rocket_h == 10:
            self.runSim_button.config(state='disabled')
        if cancel==False:
            #while abs(self.meteor_x - self.rocket_x) > 10 and abs(self.meteor_y - self.rocket_y) > 10:
            self.rocket_h += 2
            self.rocket_w += 2
            if self.meteor_x > self.rocket_x:
                self.rocket_x += self.rocket_dx
            elif self.meteor_x < self.rocket_x:
                self.rocket_x -= self.rocket_dx
            if self.meteor_y > self.rocket_y:
                self.rocket_y += self.rocket_dy
            elif self.meteor_y < self.rocket_y:
                self.rocket_y -= self.rocket_dy
            if abs(self.meteor_x - self.rocket_x) < 20 and abs(self.meteor_y - self.rocket_y) < 20:
                self.main_window.after_cancel(self.animate_rocket_success_id)
                self.animate_meteor(True)
                return                      # appears to be needed to cancel after loop
            self.rocket_image = Image.open('rocket.png')
            self.rocket_image = self.rocket_image.resize((self.rocket_h, self.rocket_w), Image.ANTIALIAS)
            self.rocket_photo_image = ImageTk.PhotoImage(self.rocket_image)
            self.rocket_canvas_image = self.earth_canvas.create_image(int(self.rocket_x), int(self.rocket_y),
                                                                          image=self.rocket_photo_image)
            self.animate_rocket_success_id =self.main_window.after(50, self.animate_rocket_success)

    def draw_one_meteor_frame(self):
        self.meteor_image = Image.open('meteor.png')
        self.meteor_image = self.meteor_image.resize((self.meteor_h, self.meteor_w), Image.ANTIALIAS)
        self.meteor_photo_image = ImageTk.PhotoImage(self.meteor_image)
        self.meteor_err = self.meteor_err + self.meteor_deltaerr
        self.meteor_canvas_image = self.earth_canvas.create_image(int(self.meteor_x), int(self.meteor_y),
                                                                  image=self.meteor_photo_image)
        self.meteor_x += self.meteor_dx
        if abs(self.meteor_err) >= 0.5:
            self.meteor_y += self.meteor_dy
            self.meteor_w -= 1
            self.meteor_h -= 1
            self.meteor_err -= self.meteor_drr

    # Retrieve the data from the text box and call the function in meteorCalc
    def processData(self):
        # have to calculate distance relative to Earth, add
        self.distance = 1500
        #self.distance = int((self.distance_entry.get())) + self.earth_x
        self.diam = int((self.diameter_entry.get()))
        self.meteorSpeed = float(120 * self.diam)
        self.meteor_y = randint(0,self.canvas_h)
        self.meteor_x = math.floor(math.sqrt(abs(pow(self.canvas_h, 2) - pow(self.meteor_y, 2))))    # Pythagoras's Identity
        self.meteor_deltaerr = (self.earth_y-self.meteor_y)/(self.earth_x-self.meteor_x)
        self.runSim_button.config(state='normal', text='Launch', background='red', command=self.animate_rocket_fail)
        if self.meteor_x > self.earth_x:
            self.meteor_dx = -self.meteor_dx
        #if self.meteor_x == self.earth_x:
        #    self.meteor_dx = 0
        if self.meteor_y > self.earth_y:
            self.meteor_dy = -self.meteor_dy
            self.meteor_drr = -self.meteor_drr
        #if self.meteor_y == self.earth_y:
        #    self.meteor_dy = 0
        if (self.meteor_x > self.canvas_w):
            self.meteor_x = self.canvas_w
        elif (self.meteor_x < 0):
            self.meteor_x = 0
        if(self.meteor_y > self.canvas_h):
            self.meteor_y = self.canvas_h
        elif (self.meteor_y < 0):
            self.meteor_y = 0
        self.animate_meteor()

        self.diam = (float(self.diam))
        #distance = float(distance)
        # = randrange(800)
        # = int(math.sqrt(math.pow(int(distance*20),2)- math.pow(self.meteor_y, 2)))

        badDiam = False
        badDistance = False

        self.diameter_notice_label = tkinter.Label(self.diameter_frame, \
                                                   text='NOTICE Heding into ifs now and diam is: {:d}'.format(diam))
        self.distance_notice_label = tkinter.Label(self.distance_frame, \
                                                   text='NOTICE Heading into ifs now and distance is: {:d}'.format(
                                                       self.distance))
        self.diameter_notice_label.pack()
        self.distance_notice_label.pack()

        # tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and diam is: ' + str(diam))
        # tkinter.messagebox.showinfo('NOTICE', 'Heading into ifs now and distance is: ' + str(distance))

        if meteorStemUtils.validInput(diam) == False:
            diam = '3'
            badDiam = True
            self.badDiam_label = tkinter.Label(self.diameter_frame, \
                                               text='Bad Input Provided badDiam now equals ' + str(badDiam))
            self.badDiam_label.pack()
            # tkinter.messagebox.showinfo('Bad Input Provided ', 'badDiam now equals ' + str(badDiam))

        # tkinter.messagebox.showinfo('BACK IN MAIN', 'Checking for valid distance now and badDistance is: ' + str(badDistance))
        self.badDistance_label = tkinter.Label(self.distance_frame, \
                                               text='BACK IN MAIN Checking for valid distance now and badDistance is: ' + str(
                                                   badDistance))
        self.badDistance_label.pack()
        self.badDistance_label.config(text='TEST')  # this is how I'll update a label within a loop
        for i in range(math.ceil(distance * 60 / meteorSpeed)):
            distance = distance - (meteorSpeed / 60/10)
            self.distance_label.config(text='Distance is now ' + str(distance))
            if (distance >= 1200 and distance <= 1400):
                self.runSim_button.config(background='green')
            elif (distance <= 0):
                self.main_window.destroy()
            else:
                self.runSim_button.config(background='red')
            self.main_window.update()
            # self.main_window.after_idle(self.badDistance_label.config(text='Distance is now: '.format(distance)))
            time.sleep(.1)
        if meteorStemUtils.validInput(distance) == False:
            distance = '300'
            badDistance = True
            self.badDistance_label.config(text='Bad Input Provided badDistance now equals ' + str(badDistance))

            # tkinter.messagebox.showinfo('Bad Input Provided ', 'badDistance now equals ' + str(badDistance))


            # if badDiam == True or badDistance == True:
            # tkinter.messagebox.showinfo('Bad Input Provided!', 'Bad input received.\n  Diameter:  "' + str(diam) +
            # '" \n  Distance: "' + str(distance) + '" \n\nRunning with 3 meters at 500 miles.')

        simRunning = False  # inserted for iconify and de-iconify, could use pack_forget, and then pack() again

        # disable the Run Simulation button until it completes
        # self.runSim_button['state']='disabled'

        # iconify the main window
        # self.main_window.iconify()

        meteorStemStatus.runSimulation(diam, distance, simRunning)

        # Enter the tkinter main loop

        tkinter.self.main_window.mainloop()

        # after the sim runs, de iconify
        if simRunning == False:
            self.main_window.deiconify()

    def runSimulation(diam, distance, simRunning):

        simRunning = True  # to let main loop know to deiconify the entry window

        # tkinter.messagebox.showinfo('Now in runSim function and boolean flag is ', str(simRunning))


        # type conversion page 64
        diamFloat = float(diam)
        distanceFloat = float(distance)

        # boolean vars page 111
        meteorInbound = True
        meteorSpeed = float(120 * diamFloat)
        meteorDistance = distanceFloat

        # showinfo page 538, output formatting page 69
        # tkinter.messagebox.showinfo('Now in runSim function', 'The speed is ' + format(meteorSpeed, '.2f'))




        # Generating another window for status output
        # status_window = tkinter.Tk()
        # status_window.title("System Status")
        # status_window.minsize(width=450,height=200)

        # status_window.geometry('600x400+50-100')   # width, ht, 50 pixels in from left, and 100 up from bottom


        # create frames for widgets....................see page 549
        # set up a frame for each widget to position them correctly

        # status_window.top_frame = tkinter.Frame(status_window)
        # status_window.bottom_frame = tkinter.Frame(status_window)



        # create widgets for the top frame, creating stringVars for text updates and output
        status_window.distanceValue = tkinter.StringVar()
        # convert distance to string and store it - page 546
        status_window.distanceValue.set(distanceFloat)

        status_window.blank_label1 = tkinter.Label(status_window.top_frame, text=' ')
        status_window.distance_label = tkinter.Label(status_window.top_frame, \
                                                     text='Meteor Distance = {:d}' + format(distanceFloat))
        status_window.distanceFloatValue = tkinter.Label(status_window.top_frame, \
                                                         textvariable=status_window.distanceValue)  # page 546

        # pack (position and order) the top frame's widgets
        status_window.blank_label1.pack(side='top')
        status_window.distance_label.pack(side='left')
        status_window.distanceFloatValue.pack(side='left')

        # create the button widget and label for the bottom frame
        status_window.blank_labelb = tkinter.Label(status_window.bottom_frame, text=' ')
        status_window.updateSim_button = tkinter.Button(status_window.bottom_frame, \
                                                        text='Update Simulation', command=simUpdate(distance, diam))

        # pack the blank label and buttons in the bottom frame
        status_window.blank_labelb.pack()
        status_window.updateSim_button.pack()

        # pack the frames
        status_window.top_frame.pack()
        status_window.bottom_frame.pack()

        status_window.lift()  # make it on top
        # tkinter.mainloop()



        # loops page 122, boolean vars page 111

        # call back function for the update button

    def simUpdate(distance, diam):
        distanceData = float(distance)
        diamData = float(diam)
        meteorSpeed = float(120 * diamData)
        # tkinter.messagebox.showinfo('In while loop now', 'The distance is ' + format(distanceData, '.2f'))

        # update the status
        while distanceData > 0:
            distanceData = distanceData - (meteorSpeed / 60)
            # tkinter.messagebox.showinfo('In while loop now', 'The distance is ' + format(distanceData, '.2f'))

        simRunning = False


# create an instance of the class
meteor_sim = MeteorGUI()
