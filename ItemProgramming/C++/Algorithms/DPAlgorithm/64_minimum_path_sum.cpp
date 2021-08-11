/*############################################################################
  principle:
  1.Each line have  explains
  2.Iterative to get outs: BF algorith to better algorithm
  3.code explain at md,problem list, Item code md,distinguish code md
##############################################################################*/

/*############################################################################
#Author:polya polyaluthor@gmail.com
#64_minimum_path_sum.cpp
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
class Solution {
public:
//recusion insert 
//frame:f(A) call f(B),f(B) is recursion function.  
      int minimumPathSum_recursion_m1(vector<vector<int>>& grid){
		  return get_MinimumPathSum(grid,0,0);
      }
	  int get_MinimumPathSum(vector<vector<int>>& grid,int i,int j){
		  //cout<<grid.size()<<" size i,size j "<<grid[0].size()<<endl;
          //if out of the boundary
		  if(i==grid.size()||j==grid[0].size()){
			  return INT_MAX;
		  }
		  //
		  cout<<grid[i][j]<<"  grid i,j"<<endl;
		  //cout<<i<<" grid i  "<<grid.size()-1<<"  grid size "<<j<<"  ""grid j  "<<grid[0].size()-1<<"  grid j  "<<endl;
		  if(i==grid.size()-1 && j==grid[0].size()-1){
			  return grid[i][j];
		  }
		  //cout<<i+1<<"i,j"<<j+1<<endl;
		  cout<<min(get_MinimumPathSum(grid,i+1,j),get_MinimumPathSum(grid,i,j+1))<<"  min"<<endl;
		  return grid[i][j]+min(get_MinimumPathSum(grid,i+1,j),get_MinimumPathSum(grid,i,j+1));
	  }
     int minimumPathSum_TailRecursion_m1(){
		 return 0;

      }
//record search recursion
      int minimumPathSum_recursion_m2(vector<vector<int>>& grid){
		  return 0;
      }
//record + recursion
      int minimumPathSum_recursion_m3(vector<vector<int>>& grid){
		  return 0;
      }
//tail recursion
      int minimumPathSum_recursion_tail_m1(vector<vector<int>>& grid){
		  return 0;
      }
//Accroding to the out,input,the function  to set up a new function.
//the process of deal with data strucuture
//relationship:dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j];
//Boundary Conditions: filled:first one,the first row and the first col value.
//How to write the code,had solved.
//DP function,return int. enter a vector for search path.
//get the row and col number for travel
//create a new 2Dvector for stored the outs,init as 0
//filled first one ,the first row and the first col value.
//others use relationship to get.and return the results.
//conclusion: operator two vectors. 
//One stored the value,another for the outs.
//
//delcare the outs int, the input datastructure vector2D,the function name.  
      int minimumPathSum_DP_m1(vector<vector<int>>& grid){
		  //if grid empty
		  if(grid.empty()||grid[0].empty()) return 0;
		  //get the new one vector indext from the input one.
		  int m=grid.size();
		  int n=grid[0].size();
		  //cout<<"m: "<<m<<"  n:   "<<n<<endl;
		  //creat a new vector2D for outs,and init it.
		  vector<vector<int>> DP(m,vector<int>(n,0));
		  //call director
		  //printVector2D(dp);
		  //two vectors relation formula 
		  //first one ,first row,first col 
		  DP[0][0]=grid[0][0];
		  for(int i=1;i<m;i++) DP[i][0]=grid[i][0]+DP[i-1][0];//travel first col：left one
		  for(int j=1;j<n;j++) DP[0][j]=grid[0][j]+DP[0][j-1];//travel first row:up one
          //the common one relationship for 
		  for(int i=1;i<m;i++){
			  for(int j=1;j<n;j++){
				  DP[i][j] = min(DP[i-1][j],DP[i][j-1])+grid[i][j];
		      }
		  }
		  //get the last one for the outs.
		  return DP[m-1][n-1];
      }
	  //2D vector to stored 1D vector
     int minimumPathSum_DP_m2(vector<vector<int>>& grid){
		//if grid empty
		if(grid.empty()||grid[0].empty()) return 0;
		int m=grid.size();
		int n=grid[0].size();
		vector<int> DP(n,INT_MAX); 
		DP[0]=0;
		for(int i=0;i<m;++i){
			for(int j=0;j<n;++j){
				if(j==0) 
				   DP[j]+=grid[i][j];
				else
				   DP[j]=grid[i][j]+min(DP[j],DP[j-1]);
			}
			
		}
		 return DP[n-1];
      }
//print  printAnswer
    void printAnswer(vector<vector<int>>& grid,vector<vector<int>>& DP){
		int i=0;//define i for vector DP row
		int j=0;//define i for vector DP col
		cout<<"[0,0]"<<endl;
		while(i<grid.size() && j<grid[0].size()){
			if(i==grid.size()-1 && j==grid[0].size()-1){
				break;
			}
			if(i==grid.size()-1){
				cout<<"["<<i<<","<<++j<<"]"<<endl;
			}else if (j==grid[0].size()-1){
				cout<<"["<<++i<<","<<j<<"]"<<endl;
			}else if(DP[i+1][j]<DP[i][j+1]){
				cout<<"["<<++i<<","<<j<<"]"<<endl;
			}else{
				cout<<"["<<i<<","<<++j<<"]"<<endl;
			}
		}

		cout <<endl;
	}
//print vector2D
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
    vector<vector<int>> grid_test1{ { 1,3,1}, 
                        		{1,5,1}, 
                                {4,2,1} };
    vector<vector<int>> grid_test2{ {1,2,3}, 
                                {4,5,6} };
	vector<vector<int>> grid_test3 {{2,3},
	                                {1,5}};
    //self test ###################################################################
	clock_t begin = clock();
	cout<<"Hello polya,welcome to the programming world" <<endl;
	cout<<"===========================================" <<endl;
	cout<<"Please input element: 2Dvector " <<endl;

//main programming
    Solution sl;
	sl.printVector2D(grid_test3);
	cout<<"=================The result: ==========================" <<endl;
//##programming##############################
//###########################################
//recursion tail
    cout<<sl.minimumPathSum_recursion_m1(grid_test3)<<endl;
//
//DP
    //cout<<sl.minimumPathSum_DP_m1(grid_test2)<<endl;
	//print the vector2D
	//sl.printVector2D(grid_test1);
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
