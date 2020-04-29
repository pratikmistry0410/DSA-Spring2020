from random import randint                          # for sorting and creating data pts
from math import atan2                              # for computing polar angle
from matplotlib import pyplot as plt                # for plotting the hull and points
import time

def scatter_plot(points,convex_hull=None):          # Function to plot points and convex hull
    x_coords,y_coords=zip(*points)                  # Zip the points to create x and y coord lists - [x0,x1,x2,...] and [y0,y1,y2,...]
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

def determine_rotation(p1,p2,p3):                       # Function to determine the rotation or turn with respected to 2nd point
    rotation = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])    # Calculating determinant of three points
    return rotation                                     # If rotation > 0 then counter-clockwise, rotation < 0 then clockwise, rotation = 0 then collinear


def convex_hull_monotone_chain(points,show_progress=True):
    if len(points) <= 3:
        print("Convex Hull Not Possible because of small number of points")
    else:
        #First in monotone chain we have to sort lexicographically
        sorted_points = sorted(points, key=lambda element: (element[0], element[1]))
        
        # Build lower hull 
        lower_hull_points = []
        for p in sorted_points:
            while len(lower_hull_points) >= 2 and determine_rotation(lower_hull_points[-2], lower_hull_points[-1], p) <= 0:
                lower_hull_points.pop()
            lower_hull_points.append(p)
        
            if show_progress:                                   # If show progress is True, plot the Lower convex hull and points 
                scatter_plot(sorted_points,lower_hull_points)
        
        # Build upper hull
        upper_hull_points = []
        for p in reversed(sorted_points):
            while len(upper_hull_points) >= 2 and determine_rotation(upper_hull_points[-2], upper_hull_points[-1], p) <= 0:
                upper_hull_points.pop()
            upper_hull_points.append(p)

            if show_progress:                                   # If show progress is True, plot the Upper convex hull and points 
                scatter_plot(sorted_points,upper_hull_points)

        convex_hull_points=lower_hull_points[:-1] + upper_hull_points[:-1]

        return convex_hull_points

# Main/Driver Function
if __name__ == "__main__":
    file = open("8.txt","r")        # Open the dataset file
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

    start_time = time.time()
    convex_hull = convex_hull_monotone_chain(points,False)
    end_time = time.time()
    print("\nConvex Hull Points are: ",convex_hull,"\n")
    print("Total Time is: ", end_time-start_time," seconds")

    scatter_plot(points,convex_hull)                     # Plotting the points generated randomly and its equivalent convex hull points calculated