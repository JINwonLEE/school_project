/** 
  * Dijkstra class with MinHeap
  *
  * Lee Jin Won
  *
	*	2016-12-28
*/


#include "dijkstra.h"
#include <cfloat>
#include <fstream>

Dijkstra::~Dijkstra()
{
/*	
	graphNode* current;
	graphNode* next;
	
	for(int i = 0; i < vertices_num; i++)
	{
		current = adjList[i].link;
		next = current->link;
		while(current != NULL)
		{
			delete current;
			current = next;
			next = current->link;
		}
		i++;
	}
	delete [] adjList;
	delete [] mheap;*/	
	
}
	
void 
Dijkstra::ReadGraph(const char* file)
{
	std::ifstream is;
	is.open(file);
	unsigned int vNum, eNum;
	is >> vNum >> eNum;
	vertices_num = vNum;
	adjList = new graphNode[vNum];
	for(int i = 0; i < vNum; i++)
		adjList[i].link = NULL;

	unsigned int ind = 0;
	while(is)
	{
		
		unsigned int ver, nbr;
		double wht;
		is >> ver >> nbr >> wht;
		graphNode *list = &adjList[ver];
		graphNode *temp = new graphNode;
		temp->idx = nbr;
		temp->weight = wht;
		temp->link = NULL; // down
		while(list->link != NULL)
		{
			list = list->link;
		}
		list->link = temp;
	}

	mheap = new MinHeap(vNum);
	is.close();
}

double 
Dijkstra::FindPath(const unsigned int v0, const unsigned int v1)
{
	int cap = mheap->capacity;
	bool *visit = new bool[mheap->capacity];
	unsigned int* previous = new unsigned int[mheap->capacity];
	heapElem *vertices = new heapElem[mheap->capacity];
	int i;
	int vertex_ind = 0;
	for(i = 0; i < mheap->capacity; i++)
	{
		vertices[i].dist = DBL_MAX;
		vertices[i].vidx = -1;
		visit[i] = false;
		previous[i] = -1;
	}
	vertices[vertex_ind].dist = 0;
	vertices[vertex_ind].vidx = v0;
	mheap->Push(vertices[vertex_ind++]);
	int test = 0;
	while(!mheap->IsEmpty())
	{
		heapElem least_elem = mheap->Top();
		mheap->Pop();
		visit[least_elem.vidx] = true;
		if(least_elem.vidx == v1) break;
		graphNode* tlist = adjList[least_elem.vidx].link;
		for(;tlist != NULL;)
		{
			unsigned int tind = tlist->idx;
			int tmp_ind = -1;
			for(int i = 0; i < vertex_ind; i ++) {
				if(vertices[i].vidx == tind) {
					tmp_ind = i;
					break;
				}
			}
			if(tmp_ind == -1) {
				vertices[vertex_ind].vidx = tind;
				tmp_ind = vertex_ind++;
			}
			if(!visit[tind] && vertices[tmp_ind].dist > least_elem.dist + tlist->weight)
			{
				vertices[tmp_ind].dist = least_elem.dist + tlist->weight;
				previous[vertices[tmp_ind].vidx] = least_elem.vidx; // previous point
				if(!mheap->IsInHeap(vertices[tmp_ind])) mheap->Push(vertices[tmp_ind]);
				else mheap->Modify(vertices[tmp_ind]);
			}
			tlist = tlist->link;
		}
	}
	unsigned int track = v1;
	unsigned int max = 10;
	unsigned int* back_trace = new unsigned int[mheap->size]; 
	int j = 0;
	back_trace[j++] = v1;
	while(previous[track] != v0)
	{
		back_trace[j++] = previous[track];
		track = previous[track];
		if(previous[track] == -1)
		{
			std::cout << "No path" <<std::endl;
			 return -1;
		}
	} 
	back_trace[j] = v0;
		
	while(j >= 1)
	{
		std::cout << back_trace[j] << ",";
		j--;
	}
	std::cout << back_trace[0] <<  std::endl;
	double distance;
	for(int i = 0; i < cap; i++) {
		if(vertices[i].vidx == v1)	{
			distance = vertices[i].dist;
			std::cout << "Distance: " << vertices[i].dist <<std::endl;
			break;
		}
	}

	delete [] visit;
	delete [] vertices;
	delete [] back_trace;
	delete [] previous;

	return distance;
	
}
	

	
