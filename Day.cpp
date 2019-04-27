#include <iostream>
#include <string>
#include <vector>
#include "constants.hpp"
#include "Task.cpp"

class Day
{
	int date;						//YYMMDD
	std :: vector <Task> tasks;		

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

	//get function
	vector <Task> getTasks()
	{
		return tasks;
	}

	//set function
	void setTasks()
	{
		//not sure what should go here
		//what are we allowing? copying a task? automatic add task identified by task tags?
	}
};
