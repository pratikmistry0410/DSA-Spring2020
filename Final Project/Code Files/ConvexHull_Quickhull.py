from random import randint                          # for sorting and creating data pts
from math import atan2                              # for computing polar angle
from matplotlib import pyplot as plt                # for plotting the hull and points
import math
import numpy as np
import time


class Quick_hull():
    
    def __init__(self):
        self.points=[]
        self.sorted_points=[]
        self.number_of_points= len(self.points)
        self.convex_hull=[]
        
    def add_points(self,x,y):
        self.points.append([x,y])
        
    def sort_points(self):
        self.sorted_points = sorted(self.points)
        return self.sorted_points
    
    def line_dist(self,p1,p2,p3): #distance of p3 from the line made by p2 and p1
            p1 = np.array(p1)
            p2 = np.array(p2)
            p3 = np.array(p3)
            distance = np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)
            return distance


    def quickhull_util(self,array,lowest,highest):
        if len(array) == 0:
            return
        max_distance = 0
        max_point= None
        
        # find the point whcih is at the maximum distance from the line joining lowest and highest
        for i in array:
            point_dist = self.line_dist(lowest,highest,i)
            if point_dist>=max_distance:
                max_distance=point_dist
                max_point=i
        self.convex_hull.append(max_point)

        # find points in the array that is on the right of the lines joining lowest to max_point and 
        #max_point to highest
        sub_left_array=[]
        sub_right_array=[]
        for i in array:
            if (i[1]-lowest[1])*(max_point[0]-lowest[0]) - (i[0]-lowest[0])*(max_point[1]-lowest[1]) > 0:
                sub_left_array.append(i)
            elif (i[1]-max_point[1])*(highest[0]-max_point[0]) - (i[0]-max_point[0])*(highest[1]-max_point[1]) > 0:
                sub_right_array.append(i)
            else:
                pass
        
        # recursively call on the new formed divisions.
        self.quickhull_util(sub_left_array,lowest,max_point)
        self.quickhull_util(sub_right_array,max_point,highest)
        
        
    
    def quickhull(self):
        #sort the points on basis of x coordinates, select minimum x and maximum x
        self.sort_points()
        min_xy = self.sorted_points[0]
        max_xy = self.sorted_points[-1]

        # add the 2 points to the convex hull final array
        self.convex_hull.append(min_xy)
        self.convex_hull.append(max_xy)

        # divide the points set into 2 halves based on the line joining min_xy, max_xy
        left_array=[]
        right_array=[]
        for i in self.sorted_points:
            if (i[1]-min_xy[1])*(max_xy[0]-min_xy[0]) - (i[0]-min_xy[0])*(max_xy[1]-min_xy[1]) > 0:
                left_array.append(i)
            elif (i[1]-min_xy[1])*(max_xy[0]-min_xy[0]) - (i[0]-min_xy[0])*(max_xy[1]-min_xy[1]) < 0:
                right_array.append(i)
            else:
                pass

        
        self.quickhull_util(left_array,min_xy,max_xy)
        self.quickhull_util(right_array,max_xy,min_xy)

        return self.convex_hull
        
    
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

    def generate_points(self,total_points,min=0,max=50):     # Function to generate random points having coordinate values from min to max passed in function
        pointss = []                                     # List to store points
        for i in range(total_points):
            x = randint(min,max)                        # Randomly generate x coordinate
            y = randint(min,max)                        # Randomly generate y coordinate
            pointss.append((x,y))                       # Append the tuple (x,y) to list
        
        self.points=pointss

    def centeroidpython(self,data):
        x, y = zip(*data)
        l = len(x)
        return sum(x) / l, sum(y) / l


# Main/Driver Function
if __name__ == "__main__":

    q=Quick_hull()
    
    file = open("8.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    points = []
    for i in data:
        coord = []
        point = i.split()
        x = float(point[0])
        y = float(point[1])
        q.add_points(x,y)
    
    start_time = time.time()
    result = q.quickhull()
    end_time = time.time()
    print("\nConvex Hull Points are: ",result,"\n")
    print("Total Time is: ", end_time-start_time," seconds")
    
    cent_x,cent_y=q.centeroidpython(result)

    xy_sorted = sorted(result, key = lambda x: math.atan2((x[1]-cent_y),(x[0]-cent_x)))

    q.scatter_plot(q.points,xy_sorted)                     # Plotting the points generated randomly and its equivalent convex hull points calculated

    
