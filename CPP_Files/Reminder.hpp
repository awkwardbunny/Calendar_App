//Reminder header
#ifndef REMINDER_HPP
#define REMINDER_HPP

#include <iostream>
#include <formFunc.hpp>
#include <vector>

using namespace std;

class Reminder
{
public:
	Reminder(string, string);
	int date;									//YYYYMMDD				
	string name;
	vector <string> tags;

	string getName();
	string getTags();
	string getInfo();
	void setTags(string t);
};

#endif