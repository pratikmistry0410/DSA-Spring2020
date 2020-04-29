import time

# Global variables to calculate the Tau Distance and also the complexity for two different algorithms
distance_sophisticated = 0
distance_bruteforce = 0
complexity_sophisticated = 0
complexity_brute = 0

# Function to read the dataset
def readDataset():
    filename_1 = "data0.1024"          # Dataset file name - Array 1
    filename_2 = "data1.1024"          # Dataset file name - Array 2
    file_1 = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename_1           # Complete File Path
    file_2 = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename_2           # Complete File Path
   
    file_object_1 = open(file_1,"r")
    lines_1 = file_object_1.readlines()             # Reading all the lines from the file opened
    dataset_1 = []
    for line in lines_1:
        line = line.strip()
        dataset_1.append(int(line))                 # Casting to int as numbers are read as strings while reading file

    file_object_2 = open(file_2,"r")
    lines_2 = file_object_2.readlines()             # Reading all the lines from the file opened
    dataset_2 = []
    for line in lines_2:
        line = line.strip()
        dataset_2.append(int(line))                 # Casting to int as numbers are read as strings while reading file
    return dataset_1,dataset_2                      # Return the array 1 and 2


# Function to create Auxiliary Array of size "N" used while merging two sub-arrays
def createAuxiliaryList(length):
    aux_list = []
    for i in range(length):
        aux_list.append(0)
    return aux_list


# Merge Function two merge two subarrays
def merge_inv(data_list, aux_list, low, mid, high):
    global distance_sophisticated                           # Referring global scope variable for calculating inversions
    global complexity_sophisticated                         # Referring global scope variable for counting complexity

    i = low
    j = mid+1
    for k in range(low,high+1):                             # Traversing each subarray formed after dividing whole array
        complexity_sophisticated+=1                         # Increment the count complexity
        if i<=mid and j<=high:
            if data_list[i] > data_list[j]:
                aux_list[k] = data_list[j]                  # Move right subarray element in auxiliary array
                distance_sophisticated+=(mid - i + 1)       # Calculating inversions if there is larger element in left subarray compared to right subarray
                j+=1
            else:
                aux_list[k] = data_list[i]                  # Move left subarray element in auxiliary array
                i+=1
        elif i > mid:
            aux_list[k] = data_list[j]                      # Move all the right subarray elements in auxiliary array
            j+=1
        elif j > high:
            aux_list[k] = data_list[i]                      # Move all the left subarray elements in auxiliary array
            i+=1

    for k in range(low,high+1):
        data_list[k] = aux_list[k]                          # Swap back all the merged and sorted elements to original array
    

# Merge Sort Function called recursively
def mergesort_inv(data_list, aux_list,low, high):
    if (high-low) <= 0:                                     # Base condition to end recursion calls
        return
    mid = int((low + high)/2)
    mergesort_inv(data_list,aux_list,low,mid)               # Sorting left subarray
    mergesort_inv(data_list,aux_list,mid+1,high)            # Sorting right subarray
    merge_inv(data_list,aux_list,low,mid,high)              # Merging left-right subarrays


# Function to calculate Kendall Tau Distance i.e. inversions in array 2 by Merge Sort (Sophisticated Method)
def kendall_tau_sophisticated(data_list_1,data_list_2):
    if(len(data_list_1) != len(data_list_2)):               # Check if criterias are satisfied
        print("Total array elements must be same in both the arrays to find Kendall Tau Distance")
        return

    aux_list = createAuxiliaryList(len(data_list_2))        # Creating auxiliary array of size N
    mergesort_inv(data_list_2,aux_list,0,len(data_list_2)-1)

    
# Function to calculate KEndall Tau Distance by Brute Force Method
def kendall_tau_bruteforce(data_list_1,data_list_2):
    if(len(data_list_1) != len(data_list_2)):               # Check if criterias are satisfied
        print("Total array elements must be same in both the arrays to find Kendall Tau Distance")
        return

    i=0
    j=0
    global distance_bruteforce              # Referring global scope variable for calculating inversions
    global complexity_brute                 # Referring global scope variable for counting complexity
    while(i < len(data_list_1)):            # Traversing array 1
        j=i+1
        while(j < len(data_list_2)):        # Traversing array 2
            complexity_brute+=1             # Increment the count complexity
            if(((data_list_1[j]-data_list_1[i]) * (data_list_2[j]-data_list_2[i])) < 0):    # Check for inversion
                distance_bruteforce+=1      # Increment the inversion count
            j+=1
        i+=1


# Driver/Main program to read dataset, and call functions to calculate Tau Distance and printing output
if __name__ == "__main__":
    data_list_1,data_list_2 = readDataset()                 # Reading the dataset 
    kendall_tau_bruteforce(data_list_1,data_list_2)         # Calling Brute Force method

    data_list_1,data_list_2 = readDataset()                 # Reading the dataset 
    kendall_tau_sophisticated(data_list_1,data_list_2)      # Calling Sophisticated method


    # Printing the outputs
    print("Kendall Tau Distance using Brute Force Method is: ", distance_bruteforce)
    print("Kendall Tau Distance using Sophisticated Method is: ", distance_sophisticated)
    print("\n")
    print("Complexity for Kendall Tau Distance using Brute Force Method is: ", complexity_brute)
    print("Complexity for Kendall Tau Distance using Sophisticated Method is: ", complexity_sophisticated)
    
