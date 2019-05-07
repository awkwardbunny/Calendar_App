//Class Reminder

#include <Reminder.hpp>

//constructor, takes in file line
//currently assumes all information available
Reminder::Reminder(string s, string t = "reminder")
{
	date = readDate(s);							
	name = readName(s);
	tags.push_back(t);					
}

//get functions
string Reminder::getName()
{
	return name;
}

string Reminder::getTags()
{
	return "#" + tags[0];
}

string Reminder::getInfo()
{
	return dateCat(date) + "\t" + dateCat(date) + "\t" + name + "\t#" + getTags();
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
		while(t[i] != ',')					//find tag
		{
			temp[j] += t[i];
			i++;
			j++;
		}
		if(temp != "event" && temp !="reminder")
		{
			tags.push_back(temp);				//add tag
		}
		temp = "";
		i++;
		j = 0;
	}
}







