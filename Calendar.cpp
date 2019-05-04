






				myfile << (it->second).getSched() << endl;	//print each day's schedule
				return 1;
			if(it-> first == d)
			{
			{
			}
			}
		for (auto it=dayMap.begin(); it!=dayMap.end(); ++it)
		fstream myfile ("input.txt");
		fstream myfile ("output.txt");
		if(myfile.is_open())							//checks file open
		if(myfile.is_open())							//checks file open
		int tempDate;
		iterator it;
		ppp08
		return 0;
		writeOutput();
		{
		}
	//reads input.txt
	Calendar()
	int contains(int d)								//returns 1 if day already in dayMap, 0 if not
	map<int, Day> dayMap;
	void readInput()
	void writeOutput()
	{
	{
	{
	{
	{
	}
	}
	}
	}
	}
	~Calendar()
  			cout << "Unable to open file" << endl;	//error message
  			cout << "Unable to open file"; 				//error message
  		else 
  		else 
  		{
  		{
  		{
  		{
  		}
  		}
  		}
  		}
    				(dayMap.find(tempDate)->second).add(line);
    				dayMap[tempDate] = Day(tempDay);	//add new Day to daze
    				tempDay = line;
    			else									//if new date
    			if(it != dayMap.end())			//if repeating date
    			it = dayMap.find(dayMap.begin(), dayMap.end(), tempDate)
    			tempDate = readDate(line);
    			{
    			{
    			}
    			}
    		for (auto it=dayMap.begin(); it!=dayMap.end(); ++it)
    		myfile.close();								//closes file
    		myfile.close();							//close file
    		while(getline(myfile, line) )				//returns reference to line, false if EOF or error
    		{
#include "Day.cpp"
#include "sorters.cpp"
#include <iostream>
#include <map>
#include <string>
class Calendar
public: 
using namespace std;
{
};