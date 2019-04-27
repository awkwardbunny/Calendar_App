#include <map>
#include "Day.cpp"
#include "sorters.cpp"

using namespace std;

class Calendar
{
	map<int, Day> dayMap;

public: 
	Calendar()
	{
		readInput();
	}

	~Calendar()
	{
		writeOutput();
	}

	int contains(int d)								//returns 1 if day already in dayMap, 0 if not
	{
		for (auto it=dayMap.begin(); it!=dayMap.end(); ++it)
		{
			if(it-> first == d)
			{
				return 1;
			}
		}
		return 0;
	}

	void readInput()
	{
		int tempDate;
		fstream myfile ("input.txt");
		if(myfile.is_open())						//checks file open
  		{
    		while(getline(myfile, line) )			//returns reference to line, false if EOF or error
    		{
    			tempDate = findDate(line);
    			if(!contains(tempDate))				//if not repeating date
    			{
    				dayMap[tempDate] = Day(tempDate);	//add new Day to daze
    			}
    		}
    	myfile.close();								//closes file
  		}
  		else 
  		{
  			cout << "Unable to open file"; 			//error message
  		}
	}

	void writeOutput()
	{
		fstream myfile ("output.txt");
		if(myfile.is_open())						//checks file open
  		{
    		for (auto it=dayMap.begin(); it!=dayMap.end(); ++it)
			{
				myfile << (it->second).getSched() << endl;	//print each day's schedule
			}
    		myfile.close();							//close file
  		}
  		else 
  		{
  			cout << "Unable to open file" << endl;	//error message
  		}
	}
};