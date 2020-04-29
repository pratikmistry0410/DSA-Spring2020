#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#define SIZE 8192												// Size of array is maximum value of a point label i.e. 8192 for all the different input data set  - DO NOT CHANGE THIS VALUE
#define PAIRS 4096													// Very Important: Please change the value based on the dataset file name - 8,32,128,512,1024,4096,8192 which has "M" particular pairs
using namespace std;

bool findQU(int,int,int []);									// Function to find whether the elements/pairs are connected i.e whether they have the same roots
void unionQU(int, int, int []);									// Function to connect/union if two elements/pairs are not connected i.e. make their roots equal
double complexityCounter = 0;									// complexity counter to count the complexity of the root() functions called from find() and union() for each pair

int main(){
	std::fstream datafile;									   // Create file stream object
	datafile.open("C:\\Users\\pdm79\\Desktop\\hw1-2.data\\" + to_string(PAIRS) + "pair.txt", std::fstream::in); // Open the dataset file for reading in file stream based on value of "PAIRS" i.e. "M" selected
	int inputArray[SIZE];									   // Array for denoting the connections between two elements/nodes

	for(int i=0;i<SIZE;i++){
		inputArray[i]=i;										// Initializing the array based on the index numbers
	}

	int index1, index2;											// Variable to store the value of two nodes from the file

    while(!datafile.eof()){										// While loop to read dataset file till end of file	
		   datafile >> index1;
		   datafile >> index2;
		   if(!findQU(index1,index2,inputArray)){				// Check If two nodes/elements are connected i.e. have same roots
			   unionQU(index1,index2,inputArray);				// Calling the union function to pair/connect the elements i.e. making their roots equal and printing the pair
			   cout << "Union performed for two elements: " << index1 << " " << index2 << endl;
		   }else{
			   cout<< "Connected" << endl;
		   }
    }

	datafile.close();										// Close the file

	// Print the complexity count for quick union algorithm - Includes cost of root function called by find and union operations i.e. 2*O(M*N) + 2*O(M*N) ~= O(M*N)
	cout << "The complexity count for the Quick Union Algorithm is: " << complexityCounter << endl;
	return 0;
}

// Some of the code is referred from the slides of the Professor
int rootQU(int inputArray[], int index){
	complexityCounter++;									// Increment the complexity counter everytime function is called to check if elements/nodes have same roots
	while(index != inputArray[index]){						// While loop to find the root of the node
		complexityCounter++;								// Increment the complexity counter everytime code traverses the tree for getting the root
		index = inputArray[index];							// reassign the index with the index of parent node
	}
	return index;											// returning the index of the root
}

// Some of the code is referred from the slides of the Professor
bool findQU(int index1, int index2, int inputArray[]){		// Function to find whether two nodes are connected
	if(rootQU(inputArray,index1)==rootQU(inputArray,index2)){	// Get the root of both the nodes and return true or false after comparison
		return true;
	}
	return false;
}

// Some of the code is referred from the slides of the Professor
void unionQU(int index1, int index2, int inputArray[]){		// Union to connect the two nodes
	int num1 = rootQU(inputArray,index1);					// Find the root of the first number	
	int num2 = rootQU(inputArray,index2);					// Find the root of the second number	
	inputArray[num1] = num2;								// Assign the root of the second number to the first
}