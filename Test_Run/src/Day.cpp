//class Day

#include <Day.hpp>

using namespace std;

Day::Day(string s)
{
	dayDate = readDate(s);
	add(s);
}

//returns formatted day schedule
string Day::getSched()
{
	string sched = "";
	for (auto it=events.begin(); it!=events.end(); ++it)
	{
    	sched += it->getInfo() + '\n';
	}
	for (auto it=reminders.begin(); it!=reminders.end(); ++it)
	{
    	sched += it->getInfo() + '\n';
	}
	return sched;
}

//determines reminder or Event, adds to appropriate vector
void Day::add(string s)
{
	if(readTags(s).find("event"))
	{
		Event e(s);
		events.push_back(e);
	}
	else if(readTags(s).find("reminder"))
	{
		Reminder r(s); 
		reminders.push_back(r);
	}
}
