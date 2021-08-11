/*
[120.Triangle](https://leetcode.com/problems/triangle/)
```
English version:  
Given a triangle array, return the minimum path sum from top to bottom.  

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.  

Example 1:  

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]  
Output: 11  
Explanation: The triangle looks like:  
   2  
  3 4  
 6 5 7  
4 1 8 3  
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).  
Example 2:  

Input: triangle = [[-10]]   
Output: -10   
*/
/*############################################################################
#Author:polya polyaluthor@gmail.com
#120_Triangle.cpp
#Last updated:2021.08.10
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
//define class
class Solution {
public://declare public  
     int triangle_minPathsum_recursion_m1(vector<vector<int>>& triangle){

     }
     int triangle_minPathsum_recursion_m2(vector<vector<int>>& triangle){

     }
     int triangle_minPathsum_DP_m1(vector<vector<int>>& triangle){
         int n=triangle.size();
         vector<vector<int>> DP(n,vector(n,0));
         

     }
     int triangle_minPathsum_DP_m2(vector<vector<int>>& triangle){

     }

     int convert_triangle_to_matrixtable()
     
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
    vector<vector<int>> triangle_test1{ 
                                {2}, 
                        		{3,4}, 
                                {6,5,7}, 
                                {4,1,8,3} };
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
