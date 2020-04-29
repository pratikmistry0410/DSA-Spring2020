import math
from random import randint                          # for sorting and creating data pts
from math import atan2                              # for computing polar angle
from matplotlib import pyplot as plt                # for plotting the hull and points
import math
import numpy as np
import time

class ConvexHull():
    def __init__(self):
        self.HullArray=[]
        self.pointsSet=[]
        
    def addPoints(self,x,y):
        self.pointsSet.append([x,y])
        
    def distance_between(self,point1,point2):
        return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    
    def orientation_check(self,point1,point2,point3):
        if (point2[1]-point3[1])*(point3[0]-point1[0])>(point3[1]-point1[1])*(point2[0]-point3[0]): #checks if the slope of line from point3
            # to point1 is more than slope of line point 2 to point 1. if so, it turn counter-clockwise
            return 1
        elif (point2[1]-point3[1])*(point3[0]-point1[0])==(point3[1]-point1[1])*(point2[0]-point3[0]):
            return 0
        else:
            return -1

    def leftmost_point(self):
        min_point = 0
        min_x = self.pointsSet[0][0]
        for i in range(0,len(self.pointsSet)):
            if min_x > self.pointsSet[i][0]:
                min_x = self.pointsSet[i][0]
                min_point = i
        return min_point
    
    def jarvis_march_boundary(self):
        min_point = self.leftmost_point()
        anchor_point = min_point
        
        self.HullArray.append(self.pointsSet[min_point])
        while (True):
            cursor_point = (anchor_point + 1) % len(self.pointsSet)
            for i in range(len(self.pointsSet)):
                if i == anchor_point:
                    continue
                d = self.orientation_check(self.pointsSet[anchor_point], self.pointsSet[i], self.pointsSet[cursor_point])
                if d > 0 or (d == 0 and self.distance_between(self.pointsSet[i], self.pointsSet[anchor_point]) > self.distance_between(self.pointsSet[cursor_point], self.pointsSet[anchor_point])):
                    cursor_point = i
            anchor_point = cursor_point
            if anchor_point == min_point:
                break
            self.HullArray.append(self.pointsSet[cursor_point])
            
        return self.HullArray

    def generate_points(self,total_points,min=0,max=50):     # Function to generate random points having coordinate values from min to max passed in function
        pointss = []                                     # List to store points
        for i in range(total_points):
            x = randint(min,max)                        # Randomly generate x coordinate
            y = randint(min,max)                        # Randomly generate y coordinate
            pointss.append((x,y))                       # Append the tuple (x,y) to list
        
        self.pointsSet=pointss

    def scatter_plot(self,pointss,convex_hull=None):          # Function to plot points and convex hull
        
        x_coords,y_coords=zip(*pointss)                  # Zip the points to create x and y coord lists - [x0,x1,x2,...] and [y0,y1,y2,...]
        
        plt.scatter(x_coords,y_coords)                  # Plot the points
        
        if convex_hull!=None:                           # Plot the convex hull boundary
            
            for i in range(1,len(convex_hull)+1):
                
                if i==len(convex_hull):                 # Connecting last point of stack with the anchor/source point i.e. Wrapping up
                    i=0
                p1 = convex_hull[i-1]
                p2 = convex_hull[i]
                plt.plot((p1[0],p2[0]),(p1[1],p2[1]),'black',label='Convex Hull',marker='o',markerfacecolor='green', markersize=6)    # Passing x and y coordiates of two points for connecting using black line
        
        plt.show()                                      # Display the plot

    def centeroidpython(self,data):
        x, y = zip(*data)
        l = len(x)
        return sum(x) / l, sum(y) / l

if __name__ == "__main__":
       
    q = ConvexHull()
    
    
    file = open("8.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    points = []
    for i in data:
        coord = []
        point = i.split()
        x = float(point[0])
        y = float(point[1])
        q.addPoints(x,y)
        
    start_time = time.time()
    result = q.jarvis_march_boundary()
    end_time = time.time()
    print("\nConvex Hull Points are: ",result,"\n")
    print("Total Time is: ", end_time-start_time," seconds")
  
    q.scatter_plot(q.pointsSet,result)
