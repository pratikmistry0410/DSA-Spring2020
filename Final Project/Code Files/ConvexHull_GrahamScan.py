from random import randint                          # for sorting and creating data pts
from math import atan2                              # for computing polar angle
from matplotlib import pyplot as plt                # for plotting the hull and points
import time

def scatter_plot(points,convex_hull=None):          # Function to plot points and convex hull
    x_coords,y_coords = zip(*points)                  # Zip the points to create x and y coord lists - [x0,x1,x2,...] and [y0,y1,y2,...]
    plt.scatter(x_coords,y_coords)                  # Plot the points
    if convex_hull!=None:                           # Plot the convex hull boundary
        for i in range(1,len(convex_hull)+1):
            if i==len(convex_hull):                 # Connecting last point of stack with the anchor/source point i.e. Wrapping up
                i=0
            p1 = convex_hull[i-1]
            p2 = convex_hull[i]
            plt.plot((p1[0],p2[0]),(p1[1],p2[1]),'black',label='Convex Hull',marker='o',markerfacecolor='green', markersize=6)     # Passing x and y coordiates of two points for connecting using black line
    plt.show()                                      # Display the plot

def generate_points(total_points,min=0,max=50):     # Function to generate random points having coordinate values from min to max passed in function
    points = []                                     # List to store points
    for i in range(total_points):
        x = randint(min,max)                        # Randomly generate x coordinate
        y = randint(min,max)                        # Randomly generate y coordinate
        points.append((x,y))                        # Append the tuple (x,y) to list
    return points

def convex_hull_graham_scan(points,show_progress=True):                                     # Function to calculate the convex hull among the list of points passed
    # Starting point of convex hull i.e. anchor point - having lowest 
    # y-coordinate (or lowest x,y cooridate if lowest y cooridates of two points are same)
    global anchor             

    min_index = None                                                # Setting minimum index to None
    for i,(x,y) in enumerate(points):                               # Enumerate over the points to find the anchor point of convex hull
        if min_index == None or y < points[min_index][1]:           # If minimum index is None or y coordinate of current point is less than previous lowest
            min_index = i                                           
        if y == points[min_index][1] and x < points[min_index][0]:  # Check if y coordinate of current and previous lowest is same then compare x coordinate
            min_index = i
    
    anchor = points[min_index]                                      # Setting anchor point using index found


    sorted_points = sort_points(points)                             # Sorting the points
    del sorted_points[sorted_points.index(anchor)]                  # Deleting the anchor to exclude from convex hull calculation
    
    # Anchor and Point with smallest polar angle will always be on convex hull
    convex_hull = [anchor,sorted_points[0]]

    for sp in sorted_points[1:]:
        while determine_rotation(convex_hull[-2],convex_hull[-1],sp) <= 0:            # Backtracking if three points are colinear or right turn from 2nd to 3rd point
            del convex_hull[-1]                             # If clockwise rotation or right turn from 2nd point to 3rd point, remove second point
        
        convex_hull.append(sp)                              # Append the sorted point if anticlockwise rotation or left turn 

        if show_progress:                                   # If show progress is True, plot the current convex hull and points 
            scatter_plot(points,convex_hull)

    return convex_hull                                      # Return convex hull points


############# Utility Functions used for Calculation of Convex Hull ##############

def sort_points(points):                                # Function to quick sort the points in list
    if len(points) <= 1:                                
        return points                                   # Return list as is if only one point
    
    # Lists to store points less, equal and more than pivot angle. Also final list to return sorted points
    left_elements = []
    equal_elements = []
    right_elements = []

    pivot_angle = find_polar_angle(points[randint(0,len(points)-1)])        # Calculating pivot angle of random point with respect to anchor

    for point in points:                                # Find polar angle of each point and place it to left, right or equal list with respect to the pivot
        relative_angle = find_polar_angle(point)        

        if relative_angle < pivot_angle:                # append the point in lists defined based on its relative polar angle with pivot angle
            left_elements.append(point)
        elif relative_angle == pivot_angle:
            equal_elements.append(point)
        else:
            right_elements.append(point)

    # Recursively sort elements in left and right and sort elements of middle/equal list based on distance formula
    return sort_points(left_elements) + sorted(equal_elements,key = calculateDist) + sort_points(right_elements)

def find_polar_angle(p1,p2 = None):                     # Function to calculate polar Angle in radians between two points
    if p2 == None:                                      # if second point is not passed, consider it as anchor point
        p2 = anchor
    
    y = p1[1] - p2[1]
    x = p1[0] - p2[0]
    return atan2(y,x)                                   # Value betweek -PI and PI as angle of (x, y) point and positive x-axis

def calculateDist(p1,p2 = None):                        # Function to calculate distance between points
    if p2 == None:                                      # if second point is not passed, consider it as anchor point
        p2 = anchor

    y_dist = p2[1] - p1[1]
    x_dist = p2[0] - p1[0]
    distance = pow(y_dist**2 + x_dist**2, 0.5)          # Distance formula = sqrt((y2-y1)^2 + (x2-x1)^2))
    return distance

def determine_rotation(p1,p2,p3):                       # Function to determine the rotation or turn with respected to 2nd point
    rotation = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])    # Calculating determinant of three points
    return rotation                                     # If rotation > 0 then counter-clockwise, rotation < 0 then clockwise, rotation = 0 then collinear


# Main/Driver Function
if __name__ == "__main__":
    file = open("8192.txt","r")        # Open the dataset file
    data = file.readlines()                 # Read all the lines
    points = []
    for i in data:
        coord = []
        point = i.split()
        x = float(point[0])
        y = float(point[1])
        coord.append(x)
        coord.append(y)
        points.append(coord)

    # scatter_plot(points,None)                            # Plotting the points generated randomly
    
    start_time = time.time()
    convex_hull = convex_hull_graham_scan(points,False)
    end_time = time.time()
    print("\nConvex Hull Points are: ",convex_hull,"\n")
    print("Total Time is: ", end_time-start_time," seconds")

    scatter_plot(points,convex_hull)                     # Plotting the points generated randomly and its equivalent convex hull points calculated