//Class Task

#include <iostream>
#include <string>
#include <vector>
#include "constants.hpp"

using namespace std;

class Task
{
	string name;
	vector <string> tags;
	int dueDate;				//6 digits YYMMDD
	int duration;				//units: minutes

public:
	//constructor, no tag added
	Task(string n, int due = 1234, int dur = 60) : name (n), dueDate(due), duration(dur){}
	
	//constructor, 1 tag added
	Task(string n, string t, int due = 1234, int dur = 60) : name(n), dueDate(due), duration(dur)
	{
		tags.push_back(t);
	}

	//copy constructor
	Task(Task &t)
	{
		name = t.getName();
		tags = t. getTags();
		dueDate = t.getDue();						//change dep on algorithm
		duration = t.getDuration();					//change dep on algorithm
	}

	//destructor
	~Task(){}

	//get functions
	string getName()
	{
		return name;
	}

	vector <string> getTags()
	{
		return tags;
	}

	int getDue()
	{
		return dueDate;
	}

	int getDuration()
	{
		return duration;
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
			while(t[i] == ' ')					//skips spaces
			{
				i++; 
			}
			while(t[i] != ',')					//find tag
			{
				temp[j] = t[i];
				i++;
				j++;
			}
			tags.push_back(temp);				//add tag, reset temp and temp index
			temp = "";
			i = 0;
		}
	}

	int setDue(int due)
	{
		dueDate = due;
	}

	int setDuration(int dur)
	{
		duration = dur;
	}
};

int main()
{
	return 0;
}






