//Class Event

#include <Event.hpp>

//assumes all information present
Event::Event(string s) : Reminder(s)
{
	start = readTime(s.substr(11, 8));
	end = readTime(s.substr(37, 8));
}

//get functions
string Event::getInfo()
{
	return dateCat(date) + "T" + timeCat(start) + "-04:00\t" + dateCat(date) + "T" + timeCat(end)+ "-04:00\t" + name + "\t" + Reminder::getTags();
}

//TODO
//set functions
/*void Event::setTags(string t)						//tags separated by commas
{
	string temp = "";
	int i = 0;
	int j = 0;
	
	while(t[i] != '\0')
	{
		while(t[i] == ' ')					//skips unnecessary spaces
		{
			i++; 
		}
		while(t[i] != ',')					//find tag
		{
			temp[j] += t[i];
			i++;
			j++;
		}
		if(temp != "event")
		{
			tags.push_back(temp);				//add tag if not "event"
		}
		temp = "";
		i++;
		j = 0;
	}
}*/







