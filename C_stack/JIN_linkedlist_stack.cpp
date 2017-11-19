#include <iostream>
using namespace std;

/*
		DATE: 2015-11-06
		EXPLANATION: Linked List를 이용해 stack의 기본 함수 구현 
*/

	
class JIN_LinkedStack{                                         
	class Node{												   
	public:
		string item;
		Node *next;
	};
	
	private :
	 Node *first = NULL;
	
	public:
	bool isEmpty(){
		return first == NULL;
	}
	
	void push(string item){
		Node *tmp = new Node();
		tmp->item = item;
		tmp->next = first;
		first = tmp;
	}
	
	string pop(){
		string item = first->item;
		first = first->next;
		return item;
	}

};

int main(){
	JIN_LinkedStack tmp;
	tmp.push("WOW");
	tmp.push("the");

	tmp.pop();
	tmp.pop();

	if(!tmp.isEmpty()) cout << tmp.pop() << endl;
	
	return 0;
}
