//class Calendar

#include <Calendar.hpp>

using namespace std;

void Calendar::readInput()
{
	int tempDate;
	fstream myfile ("file1.txt");
	string line;
	if(myfile.is_open()){ //checks file open
		while(getline(myfile, line)) //returns reference to line, false if EOF or error
		{ 
			tempDate = readDate(line);
			if(dayMap.find(tempDate) == dayMap.end()) //if not repeating date
			{				
				//dayMap[tempDate] = Day(line);	
				dayMap.insert(pair<int, Day>(tempDate, Day(line))); // This somehow works instead of above line
			}
			else
			{
				dayMap.find(tempDate) -> second.add(line);
			}
		}
		myfile.close(); //closes file
	}
	else
	{
		cout << "Unable to open file" << endl; //error message
	}
}

void Calendar::writeOutput()
{
	ofstream myfile ("file2.txt");
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
