//Event header
#ifndef EVENT_HPP
#define EVENT_HPP

//#include <iostream>
//#include <string>
//#include <vector>
#include "Reminder.hpp"
#include "formFunc.hpp"

using namespace std;

class Event : public Reminder
{
public:
	Event(string);
	int start;				
	int end;

	string getTags();
	string getInfo();
	void setTags(string t);	//tags separated by commas
};

#endif


