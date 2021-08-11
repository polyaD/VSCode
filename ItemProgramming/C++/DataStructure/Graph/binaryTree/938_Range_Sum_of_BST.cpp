/*############################################################################

##############################################################################*/

/*############################################################################
#Author:polya polyaluthor@gmail.com
#938_Range_Sum_of_BST
#Last updated:2021.08.08
#Version: 0.1
#Purpose:
##############################################################################
#Main logic principle:
#cloction all nice solutions,anlyasis and write by self.
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
// Definition for a binary tree node.
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
TreeNode* TN;
class Solution {
public:
//recusion
      int Range_Sum_of_BST_m1(){
		  return 0;

      
//print BST
	void printVector2D(vector<vector<int>>& vector2D){
	    for (auto &vec : vector2D){
		    for (auto &x : vec)
		    	cout << x << ", ";
		    cout << endl;
	    }
	cout << endl;
    }
	};
//call main function
int main(int argc, char* argv[])
{
   //###########################################
   //  delcare vector init by value
    //self test ###################################################################
	clock_t begin = clock();
	cout<<"Hello polya,welcome to the programming world" <<endl;
	cout<<"===========================================" <<endl;
	cout<<"Please input element: vector " <<endl;

//main programming
    //Solution sl;
	
	cout<<"=================The result: ==========================" <<endl;
//##programming##############################
//###########################################
	cout<<"=================<<<<==========================" <<endl;
	clock_t end = clock();
	double elapsed_secs = static_cast<double>(end - begin) / CLOCKS_PER_SEC;
	time_t now = time(0);
	char* dt = ctime(&now);
	cout<<"The programming had finished at time : "<< dt << "==============================" <<endl;
	cout <<"The programming running time: "<< elapsed_secs << " s" << endl;
//out test ####################################################################
//unit test ###################################################################
    //system("pause");
	return 0;
}
