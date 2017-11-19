#include <iostream>
using namespace std;
/*
	DATE: 2015-11-06
	EXPLANATION: Array를 활용하여 Stack 구현. resize도 같이 구현
*/ 
	
class JIN_ArrayStack{
	private:
	 int *array;
	 int size;
	 int capacity;
	 
	public:
		JIN_ArrayStack(){
			capacity = 10;
			size = 0;
			array = new int[capacity];
		}
		
		JIN_ArrayStack(int i){
			capacity = i;
			size = 0;
			array = new int[capacity];
		}
		
		bool isEmpty(){
			if(size == 0) return true;
			else return false;
		}
		
		void push(int item){
			if(size == capacity) resize(capacity *2);
			array[size] = item;
			size++;
		}
		
		int pop(){
			int tmp = array[--size];
			array[size+1] = 0;
			return tmp;
		}
		
		void resize(int i){
			int * copy = new int[i];
			for(int j = 0; j < size; j++) copy[j] = array[j];
			array = copy;
			capacity = i;
		}
		
		int find(int i){
			int tmp = array[i];
			return tmp;
		}
		
};

int main(){
	JIN_ArrayStack tmp;
	for(int i = 0; i< 20; i++)
		tmp.push(i);
	
	return 0;
}
