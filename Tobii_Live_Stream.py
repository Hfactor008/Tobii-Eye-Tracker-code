import tobii_research as tr
import time
import numpy as np
import turtle

found_eyetrackers = tr.find_all_eyetrackers()
print(found_eyetrackers)

my_eyetracker = found_eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

L = []
R = []

def Htest(): 
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("BANDIT Examination Simulator - H Test!")
    wn.screensize(1800,1000)
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(5,5)
    ball.penup()
    ball.speed(0)
    ball.goto(0,0)

    # Int data 
    x = 0
    y = 0

    #wn.tracer(8, 25)
    coord = []

    T =0.00005
    # Excuting H test
    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        x +=1

        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())
        #BallPostition(i)=ball.position()


    #pdb.set_trace()
    #wn.tracer(8, 25)
    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        
        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        y -=1
        time.sleep(T)
    
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())
        
    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    for i in range(1600):
        #ball.forward(i)
        ball.goto(x,y)
        x -=1
        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        time.sleep(T)
    
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        y -=1
        time.sleep(T)
    
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())
        
    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        x +=1
        time.sleep(T)
        
        ScreenCoordinate = (ball.pos())
        coord.append(ScreenCoordinate)
        print(ball.pos())

    coord = np.asarray(coord)
    np.save('SreenCoordinates', coord)
    wn.mainloop()


def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))
    L.append(gaze_data['left_gaze_point_on_display_area'])
    R.append(gaze_data['right_gaze_point_on_display_area'])


my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
Htest()
input('Press Enter to Quit')

    
    
my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

L=np.asarray(L)
R=np.asarray(R)

print(L[:,1])

import matplotlib.pyplot as plt

# plt.figure(1)  # create a plot figure
# plt.subplot(2, 1, 1)

# plt.plot(L,'-b')
# plt.subplot(2, 1, 2)
# plt.plot(R,'-g')

# #plt.legend(['Left Eye-X', 'Left Eye-Y', 'Right Eye-X', 'Right Eye-Y'], loc='upper left')

plt.show()


fig, ax = plt.subplots()
ax.scatter(L[:,0],L[:,1], label='Left eye gaze', c='red')
ax.scatter(R[:,0],R[:,1], label='Right eye gaze', c='blue')
ax.legend()
ax.grid(True)

plt.show()