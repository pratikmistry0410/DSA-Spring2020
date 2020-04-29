#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#define SIZE 8192											// Very Important: Please change the value based on the dataset file - 8,32,128,512,1024,4096,4192,8192 			
using namespace std;

double threeSumSophisticatedCounting(int []);			// Function that will calculate the three pairs whose sum is 0 - Sophisticated Method
void sortArray(int []);									// Function to sort the array			

int main(){  
	std::fstream datafile;								// Create file stream object
	datafile.open("C:\\Users\\pdm79\\Desktop\\hw1-1.data\\" + to_string(SIZE) +"int.txt", std::fstream::in);				// Open the dataset file for reading in file stream based on value of "SIZE" selected
	int datasetArray[SIZE];								// Array for storing numbers of size based on input file selected

    while(!datafile.eof()){								// While loop to read dataset file till end of file
		for (int i = 0; i < SIZE; i++){		
		   datafile >> datasetArray[i];					// Initializing the array with the values present in the file
		}
    }

	datafile.close();						// Close dataset file

	// Print the output returned from function which calculates complexity count for finding the pairs of three numbers whose sum is 0 for the array initialized
	cout << "The complexity count for the input dataset using the Sophisticated approach is: " << threeSumSophisticatedCounting(datasetArray) << endl;
	return 0;
}


double threeSumSophisticatedCounting(int integerArray[]){
	int count = 0;										// Counter to count pairs of three numbers whose sum is 0			
	double complexityCount = 0;							// double complexity counter to count the complexity of the function
	
	sortArray(integerArray);							// Sorting the array first - Very important for this approach

	for(int i = 0; i < SIZE; i++){						// Loop for the first number of the pair
		for(int j = i+1; j < SIZE; j++){				// Loop for the second number of the pair

			// Binary Search Logic for finding the third number of the three sum pair where num3 = -(num1+num2)
			int left = j+1;								// search from index right next to second number in array
			int right = SIZE-1;
			int mid = (left+right)/2;
			while(left<=right){
				complexityCount++;						// increment the complexity counter everytime the third number is search - log(n) is complexity because its binary search
				if(integerArray[mid] == -(integerArray[i]+integerArray[j])){
					count++;							// Increment the counter if pair exists
				}
				else if(integerArray[mid]>-(integerArray[i]+integerArray[j])){
					right = mid-1;
				}
				else{
					left = mid+1;
				}
				mid = (left+right)/2;
			}		
		}
	}
	return complexityCount;								// return the complexity count value			
}


void sortArray(int integerArray[]){						// Bubble Sort function to sort the array for binary search of third number in the three sum pair
	int flag = 1;
	for(int i = 0; i < (SIZE-1) && flag == 1; i++){		// Flag variable will terminate the loop early if values are already sorted in array
		flag = 0;										
		for(int j = 0; j < (SIZE-i-1); j++){
			if(integerArray[j] > integerArray[j+1]){
				int temp = integerArray[j];
				integerArray[j] = integerArray[j+1];
				integerArray[j+1] = temp;
				flag = 1;							
			}
		}
		
	}
}