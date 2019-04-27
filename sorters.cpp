//non-member text processing functions

#include <iostream>
#include <string>
#include <vector>
#include "Event.cpp"

using namespace std;

//reads the date that the file represents
int readDate(string s)
{
	string temp = "";						//init and declare helper vars
	int i = 0;

	while(s[i] != 'T')						//iterates through date 
	{
		if(s[i] != '-')						//ignores dashes
		{
			temp += s[i];					//stores date YYYYMMDD
		}
		i++;
	}
	return stoi(temp);
}

int readTime(string s)
{
	string temp = "";
	for(int i = 0, i < 8; i++)
	{
		if(isdigit(s[i]))
		{
			temp += s[i];
		}
	}
	return stoi(temp);
}

string readName(string s)
{
	string temp = "";
	int i = s.length() -1;
	while(s[i] != '\t')
	{
		s = s[i] + s;
	}
	return s;
}
//parses string from input.txt
Event:Event parse(string s)
{
	Event e;

	e.setDate(readDate(s));			
	
	e.setStart(readTime(s.substr(11, 8)));					
	
	e.setEnd(readTime(s.substr(37, 8)));					

	e.setName(readName(s));						
}

//concatenates int into ##:##:##
string timeCat(int t)
{
	string s = to_string(t);
	while(s.length() < 6)
	{
		s = "0" + s;
	}

	return s.substr(0, 2) + ":" + s.substr(2, 2) + ":" + s.substr(4, 2);
}

//concatenates int into ####-##-##
string dateCat(int d)
{
	string s = to_string(d);

	return s.substr(0, 4) + "/" + s.substr(4, 2) + "/" + s.substr(6, 2);
}

int main()
{
	/*Task k;
	Task &t = k;
	string s = "2019-04-27T09:30:00-04:00 Kappa";

	parse(s,t);

	cout << t.getName() << endl;
	cout << t.getDate() << endl;
	cout << t.getStart() << endl;
	cout << t.getEnd() << endl;*/

	cout << dateCat(12345678) << endl;;
	cout << dateCat(20000131) << endl;

	return 0;
}

