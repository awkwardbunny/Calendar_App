//class Calendar

#include "Calendar.hpp"

using namespace std;

void Calendar::readInput()
{
	int tempDate;
	fstream myfile ("input.txt");
	string line;
	if(myfile.is_open())						//checks file open
	{
		while(getline(myfile, line) )			//returns reference to line, false if EOF or error
		{
			tempDate = readDate(line);
			printf("")
			// if(!dayMap.contains(tempDate))				//if not repeating date
			// {
			// 	dayMap[tempDate] = Day(line);	//add new Day to daze
			// }
			// else
			// {
			// 	dayMap.find(tempDate) -> second.add(line);
			// }
		}
	myfile.close();								//closes file
	}
	else 
	{
		cout << "Unable to open file"; 			//error message
	}
}

void Calendar::writeOutput()
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