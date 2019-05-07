//Class Event

#include <Event.hpp>

Event::Event(string s) : Reminder(s, "event")
{
	start = readTime(s.substr(11, 8));					
	end = readTime(s.substr(37, 8));
	setTags(readTags(s));							
}

//get functions
string Event::getTags()
{
	string s = "";
	for(int i = 0; i < tags.size(); i++)
	{
		s += tags[i];
		if(tags[i] != tags.at(tags.size() - 1))
		{
			s += ", ";
		}
	}

	return "#" + s;
}

string Event::getInfo()
{
	return dateCat(date) + "T" + timeCat(start) + "\t" + dateCat(date) + "T" + timeCat(end)+ "\t" + name + "\t#" + getTags();
}

//TODO
//set functions
void Event::setTags(string t)						//tags separated by commas
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
}







