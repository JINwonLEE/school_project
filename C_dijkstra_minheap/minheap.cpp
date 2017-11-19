
/** 
  * Dijkstra class with MinHeap
  *
  * Lee Jin Won
  *
	*	2016-12-28
*/

#include "minheap.h"
#include <cfloat>


// Destructor
MinHeap::~MinHeap()
{
	delete [] heapArray;
	delete [] mapVidxToArray;
}

void 
MinHeap::Push(const heapElem& e)
{
	if(size == capacity)
	{
		int k = 0;
		capacity *= 2;
		heapElem *temp = new heapElem[capacity];
		std::copy(heapArray, heapArray+size, temp);
		delete [] heapArray;
		heapArray = temp;
		delete [] temp;
	}
	unsigned int currentNode = ++size;
	while(currentNode != 1 && heapArray[currentNode/2].dist > e.dist)
	{
		heapArray[currentNode] = heapArray[currentNode/2];
		currentNode /= 2;
	}
	heapArray[currentNode] = e;
	mapVidxToArray[heapArray[currentNode].vidx] = currentNode;
}

const heapElem & 
MinHeap::Top()
{
	return heapArray[1];
}

void 
MinHeap::Pop()
{	
	mapVidxToArray[heapArray[1].vidx] = 0;
	heapElem lastE = heapArray[size--];
	if(size == 0) return;
	unsigned int currentNode = 1;
	unsigned int child = 2;
	while(child <= size)
	{
		if(child < size && heapArray[child].dist > heapArray[child+1].dist) child++;
		if(lastE.dist <= heapArray[child].dist) break;
		heapArray[currentNode] = heapArray[child];
		currentNode = child; 
		child *= 2;
	}
	heapArray[currentNode] = lastE;
}

void MinHeap::Modify(const heapElem& e)
{
	unsigned int ind = mapVidxToArray[e.vidx];
	if(e.dist < heapArray[ind/2].dist)
	{
		while(ind != 1 && heapArray[ind/2].dist > e.dist)
		{
			heapArray[ind] = heapArray[ind/2];
			ind /= 2;
		}
		heapArray[ind] = e;
		return;
	}
	if(e.dist > heapArray[ind*2].dist || e.dist > heapArray[ind*2+1].dist)
	{
		unsigned int r = ind;
		unsigned int ch = ind*2;
		while(ch <= size)
		{
			if(ch < size && heapArray[ch].dist > heapArray[ch+1].dist) ch++;
			if(e.dist <= heapArray[ch].dist) break;
			heapArray[r] = heapArray[ch];
			r = ch;
			ch *= 2;
		}
		heapArray[r] = e;
		return;
	}
}

bool MinHeap::IsEmpty()
{
	if(!size) return true;
	else return false;
}
