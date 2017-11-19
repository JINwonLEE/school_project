#include "dijkstra.h"
#include <iostream>

/** 
 * Assignment 5 for CSE221 Data Structures
 *
 * 2014. 11. 17
 *
 */


int main()
{

	Dijkstra ds;
	Dijkstra ds2;
	Dijkstra ds3;
	double cs;


	ds.ReadGraph("input.txt");

	std::cout << "Shortest path between 0 and 6 : ";
	
	cs = ds.FindPath(0,6);

	ds2.ReadGraph("graph-medium.txt");

	std::cout << "Shortest path between 0 and 9201 : ";

	cs = ds2.FindPath(0, 9201);

	ds3.ReadGraph("graph-large.txt");
	std::cout << "Shortest path between 0 and 36422 : ";

	ds3.FindPath(0, 36422);
	
	
	return 0;
}
