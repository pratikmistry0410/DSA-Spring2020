#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;


int main(){
	int inputArray[] = {-6,5,7,6,1,-7,14};										// Array initialization
	int size = sizeof(inputArray)/sizeof(inputArray[0]);						// Size of the array will be dynamically determined based on the number of array elements				

	if(size >= 3){
	int complexityCount = 0;													// Complexity counter to count the complexity of the algorithm
	int count = 0;																// Counter to count the number of pairs whose sum is 0	

	// Bubble Sort to sort the array for finding the three sum pair
	int flag = 1;
	for(int i = 0; i < (size-1) && flag == 1; i++){								// Flag variable will terminate the loop early if values are already sorted in array
		flag = 0;
		for(int j = 0; j < (size-i-1); j++){
			if(inputArray[j] > inputArray[j+1]){
				int temp = inputArray[j];
				inputArray[j] = inputArray[j+1];
				inputArray[j+1] = temp;
				flag = 1;
			}
		}
	}

	
	// Algorithm to find the pairs of three numbers whose sum is 0 in Quadratic time i.e. O(n^2)
	for(int i=0;i<size;i++){													// Loop for the first number
		int firstNum = inputArray[i];											// Store first number for each loop run

		int i_left = i+1;														// Start from the index number next to the first number as left index
		int i_right = size-1;													// Right index will always be the last element i.e. the maximum value

		while(i_left < i_right){												// Traverse the array from both the ends and check whether the left index is less than right
		int sumTwoNum = inputArray[i_left] + inputArray[i_right];				// for current values of left and right index, calculate the sum of the other two numbers
		if(sumTwoNum + firstNum == 0){											// if sum of all the numbers are 0, increment counter and increment left index and decrement right index
			count++;																
			i_right--;
			i_left++;
		}else if(sumTwoNum + firstNum > 0){										// If sum is greater than 0, decrement the right index by 1 to move to lower value
			i_right--;
		}else{
			i_left++;															// If sum is lesser than 0, increment the right index by 1 to move to higher value
		}
		complexityCount++;														// Increment complexity count for each run of inner loop
	}
	}

	cout << "The count of three sum pairs equal to 0 is: " << count << endl;	// Print the count of three sum pairs whose sum is 0
	cout << "The complexity count for finding the three sum pair in quadratic time is: " << complexityCount << endl;	// Print the complexity count for the algorithm developed
	}else{
		cout << "Please create an array of minimum 3 elements" << endl;			// Display message if array has less than two element
	}
	
	return 0;
}