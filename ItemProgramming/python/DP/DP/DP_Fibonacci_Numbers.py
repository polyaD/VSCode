#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#DP_Fibonacci_Numbers.py
#Last updated:2019.4.10
#Version: 0.1
#Purpose: DP_Fibonacci_Numbers.py
#Main logic principle:
#
#test DP algorithm
#Usage:
#     example: python DP_Fibonacci_Numbers.py -in 10
############################################################################
"""
import os
import sys
import argparse
import pandas as pd
import timeit
import math
#
#Get Argv
#get ready parameters and out help inforamtion
#############################################################################
def get_args():
	parse=argparse.ArgumentParser(description='annot expression in one file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 10 ")
	parse.add_argument('-in','--input',type=int,help="input an int ")
	#parse.add_argument('-T','--target',type=str,help="input a target value ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data 
############################################################################
class Solution:
	#def __init__(n):
	#	n = n
#base on the math of relationship: recursion
	def get_Fibo_m1(self,n):
		if n <= 1:
			return n
		else:
			get_Fibo = self.get_Fibo_m1(n-1) + self.get_Fibo_m1(n-2)
			return get_Fibo
#base on DP
	def get_Fibo_m2(self,n):
		FiboArr = [0,1]
		while len(FiboArr) <n+1:
			FiboArr.append(0)
		if n <=1:
			return n
		else:
			if FiboArr[n-1] ==0:
				FiboArr[n-1] =self.get_Fibo_m2(n-1)
			if FiboArr[n-2] ==0:
				FiboArr[n-2] = self.get_Fibo_m2(n-2)
		FiboArr[n] = FiboArr[n - 2] + FiboArr[n - 1] 
		return FiboArr[n]
#Call steps for ends
############################################################################
def call_main_steps():
	start = timeit.default_timer()
	#######################################################################
	args=get_args()
	arr_m1 = args["input"]
	#target = args["target"]
	getArr = Solution()
	for i in range(0,arr_m1):
		ar_m1 = getArr.get_Fibo_m2(i)
		print(ar_m1)
	########################################################################
	stop = timeit.default_timer()
	print('\n#####################The spent time of whole process ################## \n', stop - start)
	start = timeit.default_timer()
	for i in range(0,arr_m1):
		ar_m2 = getArr.get_Fibo_m2(i)
		print(ar_m2)
	########################################################################
	stop = timeit.default_timer()
	print('\n#####################The spent time of whole process ################## \n', stop - start)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

