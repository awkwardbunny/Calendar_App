//Day header
#ifndef DAY_HPP
#define DAY_HPP

//#include <iostream>
//#include <string>
//#include <vector>
//#include "Reminder.cpp"
#include "Event.hpp"
//#include "formFunc.cpp"

using namespace std;

class Day
{
public:
	Day(string);
	int dayDate;								//YYYYMMDD
	vector <Event> events;
	vector <Reminder> reminders;		

	string getSched();
	void add(string s);
};

#endif