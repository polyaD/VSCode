/*############################################################################
#Author:polya polyaluthor@gmail.com
#Index_Number_model_version.cpp
#Last updated:2021.time
#Version: 0.1
#Purpose:
##############################################################################
#Main logic principle:
#mathmatics relation
#data structure choose
#algorithm relation
#Each steps
#features: 
#        advantage:
#        disvantage:
#        Need to iterative next version:
##############################################################################
#Usage:
#     example: model.cpp
g++ model.cpp -o model -std=gnu++11
make model
./model
#eg
g++ model.cpp -o model -std=gnu++11
make model
./model
############################################################################*/
//logic outline:print information
//include input and out library
//struture:
//
#include <iostream>
#include <ctime>
#include <vector>
#include <iterator>
#include <sstream>
#include <numeric>
#include <algorithm>
using namespace std;
class Solution {
public:
     
};
//call main function
int main(int argc, char* argv[])
{
    //self test ###################################################################
	clock_t begin = clock();
	cout<<"Hello polya,welcome to the programming world" <<endl;
	cout<<"===========================================" <<endl;
	cout<<"Please input element: " <<endl;
//###########################################
//main programming
    Solution ts;
//##programming##############################
//###########################################
	cout<<"===========================================" <<endl;
	clock_t end = clock();
	double elapsed_secs = static_cast<double>(end - begin) / CLOCKS_PER_SEC;
	time_t now = time(0);
	char* dt = ctime(&now);
	cout<<"The programming had finished at time : "<< dt << "==============================" <<endl;
	cout <<"The programming running time: "<< elapsed_secs << " s" << endl;
//out test ####################################################################
//unit test ###################################################################
	return 0;
}
