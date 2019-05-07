//class Calendar

#include <Calendar.hpp>

using namespace std;

void Calendar::readInput()
{
	int tempDate;
	fstream myfile ("input.txt");
	string line;
	if(myfile.is_open()){ //checks file open
		while(getline(myfile, line)){ //returns reference to line, false if EOF or error
			tempDate = readDate(line);
			if(dayMap.find(tempDate) == dayMap.end()){ //if not repeating date
				printf("Day %d does not yet exist! Adding...\n", tempDate);
				
				//dayMap[tempDate] = Day(line);	//add new Day to daze
				dayMap.insert(pair<int, Day>(tempDate, Day(line))); // This somehow works instead of above line
			}else{
				printf("Day %d found.\n", tempDate);
				dayMap.find(tempDate) -> second.add(line);
			}
		}
		myfile.close(); //closes file
	}else{
		cout << "Unable to open file" << endl; //error message
	}
}

void Calendar::writeOutput()
{
	ofstream myfile ("output.txt");
	if(myfile.is_open())						//checks file open
	{
		//myfile << "Test line! :)" << endl;

		//for (auto it=dayMap.begin(); it!=dayMap.end(); ++it)
		//{
		//	myfile << (it->second).getSched() << endl;	//print each day's schedule
		//}
		myfile.close();							//close file
	}
	else 
	{
		cout << "Unable to open file" << endl;	//error message
	}
}
