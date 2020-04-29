import time

# Global variable to calculate the complexity for algorithm
complexity_counter = 0

# Function to read the dataset
def readDataset():
    filename = "data1.1024"                    # Dataset file name 
    file = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename   # Complete File Path
    file_object = open(file,"r")
    lines = file_object.readlines()             # Reading all the lines from the file opened
    dataset = []
    for line in lines:
        line = line.strip()
        dataset.append(int(line))               # Casting to int as numbers are read as strings while reading file
    return dataset                              # Return the dataset
        

# Function to create Auxiliary Array of size "N" used while merging two sub-arrays
def createAuxiliaryList(length):
    aux_list = []
    for i in range(length):
        aux_list.append(0)
    return aux_list


# Merge Function two merge two subarrays
def merge(data_list, aux_list, low, mid, high):
    global complexity_counter                           # Referring global scope variable for counting complexity
    i = low
    j = mid+1
    for k in range(low,high+1):                         # Traversing each subarray formed after dividing whole array
        complexity_counter+=1                           # Increment the count complexity
        if i<=mid and j<=high:
            if data_list[i] > data_list[j]:
                aux_list[k] = data_list[j]              # Move right subarray element in auxiliary array
                j+=1
            else:
                aux_list[k] = data_list[i]              # Move left subarray element in auxiliary array
                i+=1
        elif i > mid:
            aux_list[k] = data_list[j]                  # Move all the right subarray elements in auxiliary array
            j+=1
        elif j > high:
            aux_list[k] = data_list[i]                  # Move all the left subarray elements in auxiliary array
            i+=1

    for k in range(low,high+1):
        data_list[k] = aux_list[k]                      # Swap back all the merged and sorted elements to original array
    

# Merge Sort Function called recursively
def mergesort(data_list, aux_list,low, high):
    if (high-low) <= 0:                                 # Base condition to end recursion calls
        return
    mid = int((low + high)/2)                           # Midpoint of the passed array based on start and end index passed
    mergesort(data_list,aux_list,low,mid)               # Sorting left subarray
    mergesort(data_list,aux_list,mid+1,high)            # Sorting right subarray    
    merge(data_list,aux_list,low,mid,high)              # Merging left-right subarrays


# Driver/Main program to read dataset, and call Merge Sort (Top-Down) function and printing output
if __name__ == "__main__":
    data_list = readDataset()                                   # Reading the dataset
    aux_list = createAuxiliaryList(len(data_list))              # Creating auxiliary array of size N

    start = time.time()
    mergesort(data_list,aux_list,0,len(data_list)-1)            # Calling merge sort function
    end = time.time()

    total_time = end-start                                      # Calculating physical clock time

    # Printing the outputs
    print("\nSorted List after merge sort using top-down is: ")
    print(data_list)
    print("\n")
    print("The total time taken for MergeSort using top-down approach is:", total_time*1000 , " ms")
    print("The total complexity count for MergeSort using top-down approach is:", complexity_counter)