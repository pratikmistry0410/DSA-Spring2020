#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;


int main(){
	double inputArray[] = {6,5,7,2,1,3,14};									// Array initialization	
	int size = sizeof(inputArray)/sizeof(inputArray[0]);					// Size of the array will be dynamically determined based on the number of array elements

	if(size >=2){
		double lowest = inputArray[0];										// Assign the first element as lowest
		double highest = inputArray[0];										// Assign the first element as highest
		int complexityCount = 0;											// Complexity counter to count the complexity of the algorithm
		for(int i=0; i<size; i++){											// Loop through the array to find the lowest and highest value
			if(inputArray[i] < lowest){
			lowest = inputArray[i];
			}
			if(inputArray[i] > highest){
			highest = inputArray[i];
			}
			complexityCount++;												// Increment counter for every loop run
		}
		cout << "The absolute farthest distance is: " << highest-lowest << endl;		// Print the farthest distance i.e. highest - lowest
		cout << "The complexity count for finding the farthest pair is: " << complexityCount << endl;	// Print the complexity count of the algorithm
	}else{
		cout << "Please create an array of minimum 2 elements" << endl;			// Display message if array has only one element
	}
	
	return 0;
}