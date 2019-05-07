//Class Reminder

#include <Reminder.hpp>

//constructor, takes in file line
//currently assumes all information available
Reminder::Reminder(string s)
{
	date = readDate(s);							
	name = readName(s);
	tags.push_back(readTags(s));
}

//get functions
string Reminder::getName()
{
	return name;
}

string Reminder::getTags()
{
	string s = "#";
	for(int i = 0; i < tags.size(); i++)
	{
		s += tags[i];
	}

	return "(Tag: " + s + ")";
}

string Reminder::getInfo()
{
	return dateCat(date) + "T00:00:00-04:00\t" + dateCat(date) + "T00:00:00-04:00\t" + name + "\t " + getTags();
}

//set tags
void Reminder::setTags(string t)						//tags separated by commas
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
		while(t[i] != '#')					//find tag
		{
			temp[j++] += t[i++];
		}
		tags.push_back(temp);
		temp = "";
		i++;
		j = 0;
	}
}







