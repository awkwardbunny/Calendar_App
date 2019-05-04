#include <iostream>
#include <string>
#include <vector>
#include "Event.cpp"

class Day
{
	int date;						//YYMMDD
	vector <Event> events;
	vector <Reminder> reminders		

public:
	//constructor
	Day(int d) : date(d){}

	//copy constructor
	Day(Day &d)
	{
		tasks = d.getTasks();
	}

	//destructor
	~Day(){}

	//returns formatted day schedule
	string getSched()
	{
		string sched = "";
		for (auto it=intVector.begin(); it!=intVector.end(); ++it)
    	{
        	string += it->getInfo() + '\n';
    	}
	}

	//determines reminder or Event, adds to appropriate vector
	void add(string s)
	{
		if(s.find("#event"))
		{
			events.push_back()
		}
	}
};
