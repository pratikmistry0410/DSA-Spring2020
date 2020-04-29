#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#define SIZE 8192											// Size of array is maximum value of a point label i.e. 8192 for all the different input data set  - DO NOT CHANGE THIS VALUE
#define PAIRS 8											    // Very Important: Please change the value based on the dataset file name - 8,32,128,512,1024,4096,8192 which has "M" particular pairs
using namespace std;

bool findQF(int,int,int []);								// Function to find whether the elements/pairs are connected
void unionQF(int, int, int []);								// Function to connect/union if two elements/pairs are not connected
double complexityCounter = 0;								// complexity counter to count the complexity of the functions - find() and union()

int main(){
	std::fstream datafile;									// Create file stream object
	datafile.open("C:\\Users\\pdm79\\Desktop\\hw1-2.data\\" + to_string(PAIRS) + "pair.txt", std::fstream::in); // Open the dataset file for reading in file stream based on value of "PAIRS" i.e. "M" selected
	int inputArray[SIZE];									// Array for denoting the connections between two elements/nodes

	for(int i=0;i<SIZE;i++){
		inputArray[i]=i;									// Initializing the array based on the index numbers	
	}


	int index1, index2;										// Variable to store the value of two nodes from the file
	
    while(!datafile.eof()){									// While loop to read dataset file till end of file
		   datafile >> index1;
		   datafile >> index2;
		   if(!findQF(index1,index2,inputArray)){			// Check If two nodes/elements are connected
			   unionQF(index1,index2,inputArray);			// Calling the union function to pair/connect the elements and printing the pair
			   cout << "Union performed for two elements: " << index1 << " " << index2 << endl;
		   }else{
			cout<< "Connected" << endl;
		 }
    }
	 
	datafile.close();										// Close the file

	// Print the complexity count for quick find algorithm - Includes cost of find and union operations i.e. O(M) + O(M*N) ~= O(M*N)
	cout << "The complexity count for the Quick Find Algorithm is: " << complexityCounter << endl;
	return 0;
}

// Some of the code is referred from the slides of the Professor
bool findQF(int index1, int index2, int inputArray[]){
	complexityCounter++;									// Increment the complexity counter everytime function is called to check if pairs are connected
	if(inputArray[index1] == inputArray[index2]){			// Return true if pairs are connected
		return true;
	}
	return false;
}


// Some of the code is referred from the slides of the Professor
void unionQF(int index1, int index2, int inputArray[]){		// Function to connect the two pairs/elements if not connected
	int num1 = inputArray[index1];							// VERY IMPORTANT - Retrieve the number present at the first location of the pair
	int num2 = inputArray[index2];							// VERY IMPORTANT - Retrieve the number present at the second location of the pair

	for(int i=0; i<SIZE; i++){								// Traverse through entire array
		complexityCounter++;								// increment the complexity counter everytime the union is performed
		if(inputArray[i] == num1){							// If the number associated with first location of the pair is encountered
			inputArray[i] = num2;							// assign the number associated with the second location of the pair
		}
	}
}