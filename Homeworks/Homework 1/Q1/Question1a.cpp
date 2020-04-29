#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#define SIZE 8192								// Very Important: Please change the value based on the dataset file - 8,32,128,512,1024,4096,4192,8192 			
using namespace std;

double threeSumNaiveCounting(int []);		// Function that will calculate the three pairs whose sum is 0 - Brute Force Method

int main(){
	std::fstream datafile;					// Create file stream object					
	datafile.open("C:\\Users\\pdm79\\Desktop\\hw1-1.data\\" + to_string(SIZE) +"int.txt", std::fstream::in);				// Open the dataset file for reading in file stream based on value of "SIZE" selected
	int datasetArray[SIZE];					// Array for storing numbers of size based on input file selected

    while(!datafile.eof()){					// While loop to read dataset file till end of file
		for (int i = 0; i < SIZE; i++){
		   datafile >> datasetArray[i];		// Initializing the array with the values present in the file
		}
    }
	
	datafile.close();						// Close dataset file

	// Print the output returned from function which calculates complexity count for finding the pairs of three numbers whose sum is 0 for the array initialized
	cout << "The complexity count for the input dataset using the Naive (Brute Force) approach is: " << threeSumNaiveCounting(datasetArray) << endl;	

	return 0;
}


double threeSumNaiveCounting(int integerArray[]){					
	int count = 0;									// Counter to count pairs of three numbers whose sum is 0
	double complexityCount = 0;						// double complexity counter to count the complexity of the function
	
	for(int i = 0; i < SIZE; i++){					// Loop for the first number of the pair
		for(int j = i+1; j < SIZE; j++){			// Loop for the second number of the pair
			for(int k = j+1; k < SIZE;k++){			// Loop for the third number of the pair
				if(integerArray[i] + integerArray[j] + integerArray[k] == 0){				// Check if sum of three numbers is 0 and increase the counter
					count++;
				}
				complexityCount++;															// Increment the complexity counter each time the loop is running for finding the third number
			}
		}
	}
	return complexityCount;																	// return the complexity count value
}