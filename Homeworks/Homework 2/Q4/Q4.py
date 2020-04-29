import time

# Global variable to calculate the complexity for algorithm
complexity_counter = 0

# Dataset file name to be saved with generated dataset at the filepath mentioned below
filename = "dataset"
file = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename

# Function to generate dataset and write to file and also use it for algorithm
def genrateDataset():
    file_object = open(file,"w") 
    data_set = []
    for i in range(0,1024):                 # Creating list of 1024 - 1's
        data_set.append(1)                  # Appending generated data
        file_object.write("1\n")
    
    for i in range(0,2048):                 # Creating list of 2048 - 11's
        data_set.append(11)                 # Appending generated data
        file_object.write("11\n")
    
    for i in range(0,4096):                 # Creating list of 4096 - 111's
        data_set.append(111)                # Appending generated data
        file_object.write("111\n") 
 
    for i in range(0,1024):                 # Creating list of 1024 - 1111's
        data_set.append(1111)               # Appending generated data
        file_object.write("1111\n")

    file_object.close()
    return data_set                         # Returning the dataset generated


# Function to sort the dataset using insertion sort - linear time complexity
def insertionSort(arr,low,high):            
    global complexity_counter               # Referring global scope variable for counting complexity
    for i in range(low+1,high,1):           # Traversing each array element
        temp = arr[i]
        index = i 
        complexity_counter+=1               # Increment the count complexity
        while index > 0 and arr[index-1] > temp:        # Sort the left subarray of the current index
            complexity_counter+=1           # Increment the count complexity   
            arr[index] = arr[index-1]
            index-=1
        arr[index] = temp


# Driver/Main program to read dataset, and call insertion sort and printing output
if __name__ == "__main__":
    data_list = genrateDataset()                    # Generating dataset
    insertionSort(data_list,0,len(data_list))       # Calling function to sort array element

    # Printing the outputs
    print("\nSorted List after insertion sort is: ")
    print(data_list)
    print("The total complexity count for insertion sort is:", complexity_counter)