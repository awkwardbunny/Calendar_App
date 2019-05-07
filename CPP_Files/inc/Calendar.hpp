//Calendar header

#ifndef CALENDAR_HPP
#define CALENDAR_HPP

//#include <iostream>
#include <map>
//#include <string>
#include "Day.hpp"
#include <fstream>
//#include "formFunc.cpp"
using namespace std;

class Calendar
{
	map<int, Day> dayMap;

public: 
	void readInput();
	void writeOutput();
};

#endif