/** 
  * Dijkstra class with MinHeap
  *
  * Lee Jin Won
  *
	*	2016-12-28
*/


#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "minheap.h"
#include <iostream>

class graphNode {
public:
	unsigned int idx;  // vertex index
	double weight;     // edge weight
	graphNode* link;   // link to next node
};

// Dijkstra class
class Dijkstra {
public:
	Dijkstra() { mheap = NULL; adjList = NULL; };
	~Dijkstra();
	
	void ReadGraph(const char* file);
	
	double FindPath(const unsigned int v0, const unsigned int v1);
	
private:
	MinHeap* mheap;
	int vertices_num;
	graphNode* adjList;
};

#endif
