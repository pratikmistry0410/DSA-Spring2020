#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;


int main(){
	int inputArray[] = {-6,5,7,6,1,-7,14};								// Array initialization
	int size = sizeof(inputArray)/sizeof(inputArray[0]);				// Size of the array will be dynamically determined based on the number of array elements

	if(size >=2){
		int complexityCount = 0;											// Complexity counter to count the complexity of the algorithm
		int count = 0;														// Counter to count the number of pairs whose sum is 0	

		// Bubble Sort to sort the array for finding the two sum pair
		int flag = 1;
		for(int i = 0; i < (size-1) && flag == 1; i++){					// Flag variable will terminate the loop early if values are already sorted in array
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

	
	// Algorithm to find the pairs whose sum is 0 in Linear time i.e. O(n)
	int i_left = 0;													// Left index will store the first index of array	i.e. index of minimum value
	int i_right = size-1;											// Right index will store the last index of array i.e. index of maximum value
	while(i_left < i_right){										// Traverse the array from both the ends and check whether the left index is less than right
		int sum = inputArray[i_left] + inputArray[i_right];			// for current values of left and right index, calculate the sum	
		if(sum == 0){												// If sum is 0,increment counter and increment left index and decrement right index	
			count++;
			i_right--;
			i_left++;
		}else if(sum > 0){											// If sum is greater than 0, decrement the right index by 1 to move to lower value
			i_right--;
		}else{
			i_left++;												// If sum is lesser than 0, increment the right index by 1 to move to higher value
		}
		complexityCount++;											// Increment complexity count for each run	
	}

	cout << "The count sum of pairs equal 0 is: " << count << endl;		// Print the count of pairs whose sum is 0
	cout << "The complexity count for finding the two sum pair in linear time is: " << complexityCount << endl;			// Print the complexity count for the algorithm developed
	}else{
		cout << "Please create an array of minimum 2 elements" << endl;			// Display message if array has only one element
	}

	return 0;
}