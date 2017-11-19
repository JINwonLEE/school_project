/** 
  * Hashmap
  *
	* dictionary
	*
  * Lee Jin Won
  *
	*	2016-12-29
*/


#include "hashmap.h"
#include <iostream>
#include <fstream>


using namespace std;

HashMap< MapElem<string, int> > dict;	

void spellcheck(std::string s)
{
	if(s == "q") return;
	unsigned int len = s.length();
	if(dict.find(s) == NULL)
	{
		std::string temp = s;
		std::cout <<"> " << s << " is NOT in the dictionary" << std::endl;
		std::cout << "> " << s << " : ";
		int i = 0;
		int comma = 0;
		for(;i<len; i++)
		{
			char re = s[i];
			char k = 97;
			for(; k < 123; k++)
			{
				if(k != s[i])
				{
					s[i] = k;
					if(dict.find(s) != NULL)
					{
						if(comma != 0)
						{
							std::cout << ", ";
						}
						std::cout << s;
						comma++;
					}
					s[i] = re;
				}
			}
		}
		if(comma == 0) std::cout << "no suggestion";
		std::cout << std::endl;
	}
	else
	std::cout << "> " << s << " is in the dictionary" << std::endl;				
}


int main()
{
	char filename[] = "dictionary.txt";
	std::ifstream ifs(filename, std::ifstream::in);
	std::string s((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
	std::transform(s.begin(), s.end(),
				   s.begin(), ::tolower);

	std::string token;	
	unsigned int len = s.length();
		
	for(int i=0; i<len; i++)
	{
		int ascii = s[i];
		
		if(ascii < 97 || ascii > 127) 
		{
			if(token.length() > 0) 
			{
				dict.insert(token, 0);
				token.clear();
			}
			continue;
		}
		token.push_back(s[i]);
	}

	//
	// infinite loop to accept user input word
	//
	while(1)
	{
		std::string s;
		std::cout << "> ";
		std::cin >> s;
		if(s == "q") break;
		spellcheck(s);
		
	}
	
	
	return 0;
}
