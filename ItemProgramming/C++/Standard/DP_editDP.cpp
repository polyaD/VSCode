/************************************************************
#Copyright(C), 2021, polya Tech. Co.,Ltd.
#FileName:DP_fib.cpp
#Author:       
#contact:polyaluthor@gmail.com
#Description:     //
#Version:         //
  FunctionList:   //
    1. -------
#History:         //
  <author>  <time>  <version >  <desc strategy>
  polyad  2021/07/07 0.1   first build this moudle vetror and umordered_map
***********************************************************/
#include<iostream>
#include<vector>
#include<ctime>
using namespace std;
/*

*/
class Solution {
 public:
int min3(int a, int b, int c){
    a = a < b ? a : b;
    return a < c ? a : c;
}

int LevenshteinDis_m1(string s, int s_len, string t, int t_len){
    int cost;
    //
    if(s_len == 0)return t_len;
    if(t_len == 0)return s_len;
    //
    if(s[s_len - 1] == t[t_len - 1])cost = 0;
    else cost = 1;
    return min3(LevenshteinDis_m1(s, s_len - 1, t, t_len) + 1,
                LevenshteinDis_m1(s, s_len, t, t_len - 1) + 1,
                LevenshteinDis_m1(s, s_len - 1, t, t_len - 1) + cost);

}

int LevenshteinDP_m1(string s, string t){
    //levenshtein
    int dp[s.length()+1][t.length()+1];//d[i][j]
    for(int i = 0; i <= s.length(); i++)dp[i][0] = i;//
    for(int j = 1; j <= t.length(); j++)dp[0][j] = j;//
    for(int j = 0; j < t.length(); j++){
        for(int i = 0; i < s.length(); i++){
            if(s[i] == t[j])dp[i+1][j+1] = dp[i][j];//
            else dp[i+1][j+1] = min3(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1);
            //
        }
    }
    return dp[s.length()][t.length()];
}
};
/*
main function call processing
define a vector and a target value .
call class sum. and running test the ends.
*/
int main(int argc,  char** argv){
    string m = "kitadds";
    string n = "sitcdew";
    Solution s;
    clock_t start,finish;
    double totaltime;
    start=clock();
    cout<<"recursion: "<<s.LevenshteinDis_m1(m, m.length(), n, n.length())<<endl;
    finish=clock();
    totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
    cout<<"recursion running:  "<<totaltime<<"  time"<<endl<<endl;

    start=clock();
    cout<<"Dynamic Programming: "<<s.LevenshteinDP_m1(m, n)<<endl;
    finish=clock();
    totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
    cout<<"DP running "<<totaltime<<"  time"<<endl<<endl;
    return 0;

}

