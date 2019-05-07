//non-member form functions

#include "formFunc.hpp"

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
	for(int i = 0; i < 8; i++)
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
	int i = 52;
	while(s[i] != '\t')
	{
		temp += s[i];
		i++;
	}
	return temp;
}

string readTags(string s)
{
	string temp = "";
	int i = s.length() - 1;
	while(s[i] != '#')
	{
		temp = s[i] + temp;
	}
	return temp;
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
