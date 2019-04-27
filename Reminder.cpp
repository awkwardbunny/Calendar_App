//Class Task

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Reminder
{
protected:
	string name;
	vector <string> tags;
	int date;									//YYYYMMDD				

public:
	Reminder(int d) : date(d)
	{
		tags.push_back("reminder");
	}
	//get functions
	string getName()
	{
		return name;
	}

	vector <string> getTags()
	{
		return tags;
	}

	string getInfo()
	{
		return dateCat(date) + "T" + timeCat(start) + "\t" + dateCat(date) + "T" + timeCat(end)+ "\t" + name;
	}

	//set functions
	void setName(string n)
	{
		name = n;
	}

	void setTags(string t)						//tags separated by commas
	{
		string temp = "";
		int i = 0;
		int j = 0;
		
		while(t[i] != '\0')
		{
			while(t[i] == ' ')					//skips spaces
			{
				i++; 
			}
			while(t[i] != ',')					//find tag
			{
				temp[j] = t[i];
				i++;
				j++;
			}
			tags.push_back(temp);				//add tag, reset temp and temp index
			temp = "";
			i = 0;
		}
	}

	int setDate(int d)
	{
		date = d;
	}

	int setStart(int s)
	{
		start = s;
	}

	int setEnd(int e)
	{
		end = e;
	}

	friend void parse(string s, Event &e);
};







