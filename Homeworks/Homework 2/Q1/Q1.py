import time

# Function to read the dataset
def readDataset():
    filename = "data1.1024"                 # Dataset file name
    file = "/Users/learning/Documents/Pratik Mistry/Sem2/Data Structures and Algorithms/dataset-problem2-hw2/" + filename       # Complete File Path
    file_object = open(file,"r")
    lines = file_object.readlines()         # Reading all the lines from the file opened
    dataset = []
    for line in lines:
        line = line.strip()
        dataset.append(int(line))           # Casting to int as numbers are read as strings while reading file
    return dataset                          # Return the array/list of dataset
  

# Function to shell sort the array/list passed based on the values of "h" passed as an array in second parameter
def shellsort(data_list,h_sortlist):
    N = len(data_list)
    h_len = len(h_sortlist)
    if h_len == 1:                                      # If array has only h=1 - 1-sort the array i.e. Insertion Sort
        h_insertion_count = 0                           # Counter to count the complexity
        h = h_sortlist[0]
        for i in range(h,N,1):
            j = i
            h_insertion_count+=1                        # Increment the count complexity
            while j >= h and data_list[j] < data_list[j-h]:  # Sort all the h-array elements in each pass
                h_insertion_count+=1                    # Increment the count complexity
                temp = data_list[j]
                data_list[j] = data_list[j-h]
                data_list[j-h] = temp
                j = j-h                                
        return h_insertion_count
    else:
        h_shell_count = 0                               # Counter to count the complexity
        for k in range(h_len):
            h = h_sortlist[k]   
            for i in range(h,N,1):                      # Iterate through all the values of h=7,3,1
                j = i
                h_shell_count+=1                        # Increment the count complexity
                while j >= h and data_list[j] < data_list[j-h]:  # Sort all the h-array elements in each pass
                    h_shell_count+=1
                    temp = data_list[j]
                    data_list[j] = data_list[j-h]
                    data_list[j-h] = temp
                    j = j-h
        return h_shell_count


# Driver/Main program to read dataset, and call shell sort functions for both the phases and printing output
if __name__ == "__main__":
    data_list = readDataset()                                               # Reading the dataset     
    h_shellSort = [7,3,1]
    h_insertionSort = [1]

    start_shell = time.time()
    h_shell_count = shellsort(data_list,h_shellSort)                        # Calling Shell Sort all the way function
    end_shell = time.time()
    print("\nSorted List after shell sorting using h=7,3,1 is: ")
    print(data_list)
    
    data_list = readDataset()
    start_ins = time.time()
    h_insertion_count = shellsort(data_list,h_insertionSort)                # Calling Insertion Sort Phase function
    end_ins = time.time()
    print("\nSorted List after insertion sort phase i.e. h=1 is: ")
    print(data_list)

    # Calculating physical clock time
    total_time_shell = end_shell-start_shell
    total_time_insertion = end_ins-start_ins

    # Printing the outputs
    print("\nThe total time taken for shell sort for h = 7,3,1 is:",total_time_shell*1000, " ms")
    print("\nThe total time taken for insertion based shell sort i.e. when h = 1 is:",total_time_insertion*1000, " ms")
    print("\nThe total comparisons made for shell sort for h = 7,3,1 is:",h_shell_count)
    print("\nThe total comparisons made for insertion based shell sort i.e. when h = 1 is:",h_insertion_count)