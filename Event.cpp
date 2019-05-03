//Class Task

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Event 
{
	string name;
	vector <string> tags;
	int date;									//YYYYMMDD
	int start;				
	int end;				

public:
	//constructor, takes in file line
	//currently assumes all information available
	Event(string s)
	{
		setDate(readDate(s));			
		setStart(readTime(s.substr(11, 8)));					
		setEnd(readTime(s.substr(37, 8)));					
		setName(readName(s));		
		setTags(readTags(s));			
	}

	//copy constructor
	Event(Task &t)
	{
		name = t.getName();
		tags = t.getTags();
		date = t.getDate();						
		start = t.getStart();				//change dep on algorithm
		end = t.getEnd();					//change dep on algorithm
	}

}
	//get functions
	string getName()
	{
		return name;
	}

	string getTags()
	{
		for(auto it=tags.begin(); it!=tags.end(); ++it)
    	{
        	string += it->getInfo() + '\n';
    	}
	}

	string getInfo()
	{
		return dateCat(date) + "T" + timeCat(start) + "\t" + dateCat(date) + "T" + timeCat(end)+ "\t" + name + "\t#" + getTags();
	}

	//set functions
	void setName(string n)
	{
		name = n;
	}

	void setTags(string t)						//tags separated by commas
	{
		string temp = "";
		int i = 0;
		int j = 0;
		
		while(t[i] != '\0')
		{
			while(t[i] == ' ')					//skips unnecess

				ary spaces
			{
				i++; 
			}
			while(t[i] != ',')					//find tag
			{
				temp[j] += t[i];
				i++;
				j++;
			}
			tags.push_back(temp);				//add tag, reset temp and temp index
			temp = "";
			i = 0;
		}
	}

	int setDate(int d)
	{
		date = d;
	}

	int setStart(int s)
	{
		start = s;
	}

	int setEnd(int e)
	{
		end = e;
	}
};







