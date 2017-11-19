/** 
  * Hashmap
  *
	* dictionary
	*
  * Lee Jin Won
  *
	*	2016-12-29
*/

#ifndef HASHMAP_H
#define HASHMAP_H

#include <iostream>


// Map element
template <class KeyType, class ValType>
class MapElem
{
public:
	typedef KeyType ktype;
	typedef ValType vtype;
	
	KeyType key;
	ValType val;

	MapElem* link;
	~MapElem() { delete link;};
};

bool inline operator==(std::string a, std::string b)
{
	if((a).compare(b) == 0) return true;
	return false;
}

//
// Hash Map data structure
//
template <class HashMapElemType> 
class HashMap
{
public:
	typedef typename HashMapElemType::ktype KeyType;
	typedef typename HashMapElemType::vtype ValType;
	
	// constructor
	HashMap(unsigned int c = 1000);
	
	// destructor
	~HashMap();
	
	// Modify below functions
	int size() { return mapsize; };
	
	bool isEmpty() { return (mapsize == 0); };
	
	// ToDo
	HashMapElemType* find(const KeyType k);
	
	void insert(const KeyType k, const ValType v);
		
	bool remove(const KeyType k);
	
	unsigned int hashfunction(const KeyType k);
	
	unsigned int Hashfunction(std::string k);
	
	unsigned int Hashfunction(int k);
	
	unsigned int Hashfunction(double k);
	
	void print();
	
private:
	// Hash Table
	HashMapElemType** ht;
	unsigned int mapsize, capacity, divisor;
};



//
// - Implementation -
//

// constructor
template <class HashMapElemType>
HashMap<HashMapElemType>::HashMap(unsigned int c) 
{
	capacity = divisor = c;
	mapsize = 0;
	ht = new HashMapElemType*[capacity];
	int i = 0;
	for(; i< capacity; i++)
	{
		ht[i] = new HashMapElemType();
		ht[i]->link = NULL;
	}
}

// destructor
template <class HashMapElemType>
HashMap<HashMapElemType>::~HashMap() 
{
	delete [] ht;
}

template <class HashMapElemType>
HashMapElemType* 
HashMap<HashMapElemType>::find(const KeyType k) 
{ 
	unsigned int kcon = hashfunction(k);
	HashMapElemType* com = ht[kcon];
	if(com->link == NULL) return NULL;
	while(com->link != NULL)
	{
		HashMapElemType* temp = new HashMapElemType;
		temp = com->link;
		if(k == temp->key)
		return temp;
		else
		{ 
			com = com->link;
		}
	}
	return NULL;	
}

template <class HashMapElemType>
void 
HashMap<HashMapElemType>::insert(const KeyType k, const ValType v) 
{
	unsigned int kcon = hashfunction(k);
	HashMapElemType* temp = new HashMapElemType;
	temp->key = k;
	temp->val = v;
	temp->link = NULL;
	HashMapElemType* com = ht[kcon];
	if(com->link == NULL) 
	{
		com->link = temp;
		return;
	}
	while(com->link != NULL)
	{
		com = com->link;
	}
	com->link = temp; 
	mapsize++; 
}

template <class HashMapElemType>
bool 
HashMap<HashMapElemType>::remove(const KeyType k) 
{
	unsigned int kcon = hashfunction(k);
	HashMapElemType* com = ht[kcon];
	if(com->link == NULL) return false;
	while(com->link != NULL)
	{
		HashMapElemType* temp = new HashMapElemType;
		temp = com->link;
		if(temp->key == k) //check
		{
			HashMapElemType* del = com->link;
			com->link = del->link;
			delete del;
			mapsize--;
			return true;
		}	
		com = com->link;
	}
	return false;
}

template <class HashMapElemType>
unsigned int 
HashMap<HashMapElemType>::hashfunction(const KeyType k)
{
	return Hashfunction(k);
}

template <class HashMapElemType>
unsigned int 
HashMap<HashMapElemType>::Hashfunction(std::string k)
{
	int number = 0;
	int i = 0;
	while(k[i])
	{
		number += k[i];
		i++;
		if(k[i])
		{
			number += ((int) k[i]) << 8;
			i++;
		}
	}
	return number%divisor;	
}

template <class HashMapElemType>
unsigned int 
HashMap<HashMapElemType>::Hashfunction(int k)
{
	return k%divisor;
}

template <class HashMapElemType>
unsigned int 
HashMap<HashMapElemType>::Hashfunction(double k)
{
	int number = (int)k;
	return number%divisor;
}

template <class HashMapElemType>
void 
HashMap<HashMapElemType>::print()
{
	int i = 0;
	while(ht[i])
	{
		HashMapElemType* temp = ht[i]->link;
		while(temp)
		{
			std::cout << temp->key << ":" << temp->val << std::endl;
			temp = temp->link;
		}
		i++;
	}
}

#endif
