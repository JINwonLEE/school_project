#include <iostream>
#include <algorithm>
using namespace std;

/* 	Binary Search
	Date: 2015-11-09
	EXPLANATION: Sorted 된 어레이의 Binary Search
*/
 
int BinarySearch(int* a, int key, int size);

int BinarySearch(int* a, int key, int size){
	int low = 0;
	int high = size -1;
	while(low <= high){
		int mid = low + (high - low) / 2;
		if(key < a[mid]) high = mid -1;
		else if(key > a[mid]) low = mid +1;
		else return mid;
	}
	return -1;
}


int main(){
	int a[10];
	for(int i = 0; i< 10; i++)
		a[i] = 2*i;
	cout << "index of 15: " << BinarySearch(a, 15, 10) << endl;
	cout << "index of 20: " << BinarySearch(a, 20, 10) << endl;
	cout << "index of 16: " << BinarySearch(a, 16, 10) << endl;
	
	return 0;	
}
