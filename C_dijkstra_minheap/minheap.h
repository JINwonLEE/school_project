/** 
  * Dijkstra class with MinHeap
  *
  * Lee Jin Won
  *
	*	2016-12-28
*/

#ifndef MINHEAP_H
#define MINHEAP_H

#include <iostream>


// Heap element
class heapElem {
public:
	unsigned int vidx; // vertex index
	double dist; // shortest path distance
};


// MinHeap class
class MinHeap {
	//friend class graphNode;
	friend class Dijkstra; 
public:
	MinHeap(unsigned int maxheapsize)
	{
		size = 0;      // current heap size
		capacity = maxheapsize; // maximum heap capacity
		heapArray = new heapElem[capacity+1]; // first element is stored in heapElem[1]
		for(int i = 1; i <= capacity; i++) {
			heapArray[i].vidx = 0;
			heapArray[i].dist = -1;
		}
		mapVidxToArray = new unsigned int[capacity]; 
		//mapVidxToArray[i] = j means vertex i has index j in heaparray
		for(int i=0; i<capacity; i++) mapVidxToArray[i] = 0; // new init
	};
	
	~MinHeap();
	
	void Push(const heapElem& e);
	
	const heapElem & Top();
	
	void Pop();
	
	void Modify(const heapElem& e);
	
	bool IsEmpty();
	
	// new function
	bool IsInHeap(const heapElem& e) 
	{
		if(mapVidxToArray[e.vidx] == 0) return false;
		return true;		
	};
	
private:
	heapElem* heapArray;
	unsigned int* mapVidxToArray; // map between vertex index to heapArray
	unsigned int capacity, size;
};

#endif
