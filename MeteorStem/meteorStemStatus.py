#  the functions here
import tkinter
import tkinter.messagebox

        # function to get input and display it ref page 546
        # Data conversion page 51
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

    status_window.geometry('600x400+50-100')   # width, ht, 50 pixels in from left, and 100 up from bottom


    # create frames for widgets....................see page 549
    # set up a frame for each widget to position them correctly
        
    status_window.top_frame = tkinter.Frame(status_window)
    status_window.bottom_frame = tkinter.Frame(status_window)
    


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
