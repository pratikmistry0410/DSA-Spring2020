import time

# Global variable to calculate the complexity for algorithm
complexity_count = 0

# Function to read the dataset
def readDataset():
    filename = "data1.1024"                             # Dataset file name 
    file = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename           # Complete File Path
    file_object = open(file,"r")
    lines = file_object.readlines()                     # Reading all the lines from the file opened
    dataset = []
    for line in lines:
        line = line.strip()
        dataset.append(int(line))                        # Casting to int as numbers are read as strings while reading file
    return dataset                                       # Return the dataset


# Function to calculate median of the array
def medianOf3(arr,low,mid,high):
    if arr[low] > arr[high]:
        if arr[high] > arr[mid]:
            return high
        elif arr[mid] > arr[low]:
            return low
        else:
            return mid
    else:
        if arr[low] > arr[mid]:
            return low
        elif arr[mid] > arr[high]:
            return high
        else:
            return mid

# Function to quick sort the array with median of 3 method
def medianQuickSort(data_list,low,high):
    if high <= low:                                 # Base condition to end recursion
        return
    mid = int((low+high)/2)
    median = medianOf3(data_list,low,mid,high)          # Calculate the median of array
    swap(data_list,low,median)                          # Swap median with lowest index of the array
    pivot_partition = partition(data_list,low,high)     # Find the pivot/partition
    medianQuickSort(data_list,low,pivot_partition-1)    # Apply quick sort to left subarray
    medianQuickSort(data_list,pivot_partition+1,high)   # Apply quick sort to right subarray

# Function to partition the array and returning the pivot element
def partition(arr,low,high):
    global complexity_count                               # Referring global scope variable for counting complexity
    pivot = arr[low]                                      # Selecting lowest element as pivot
    left = low
    right = high
    while left < right:                                   
        while arr[right] >= pivot and left < right:        # Move from right towards left and check for element less than pivot
            complexity_count+=1                            # Increment the count complexity
            right-=1
        if right!=left:
            arr[left] = arr[right]                          # Swap the smaller element at the right to the left of pivot
            left+=1
        
        while arr[left] <= pivot and left < right:          # Move from left towards right and check for element greater than pivot
            complexity_count+=1                             # Increment the count complexity
            left += 1
        if right!=left:                                     # Swap the greater element at the left to the right of pivot
            arr[right] = arr[left]
            right-=1
    
    arr[left] = pivot
    return left

# Function to swap the median and lowest index of the subarray
def swap(data_list,low,median):
    temp = data_list[median]
    data_list[median] = data_list[low]
    data_list[low] = temp


# Driver/Main program to read dataset, and call quick sort with median of 3 and printing output
if __name__ == "__main__":
    data_list = readDataset()                           # Reading the dataset
    start = time.time()
    medianQuickSort(data_list,0,len(data_list)-1)       # Calling Quick Sort: median of 3 
    end = time.time()

    total_time = end-start                              # Calculating physical clock time

    # Printing the outputs
    print("\nThe sorted list using quick sort with cutoff to insertion sort is: ")
    print(data_list)
    print("\nThe total time taken for quick sort with cutoff to insertion sort is:",total_time*1000 , " ms")
    print("\nThe complexity count for quick sort with cutoff to insertion sort is:",complexity_count)