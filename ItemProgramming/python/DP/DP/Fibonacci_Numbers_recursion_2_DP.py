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
#     example: python DP_Fibonacci_Numbers.py  
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
class Solution(object):
	def __init__(self,n):
		self.n = n
#base on the math of relationship: recursion
# A naive recursive solution
	def get_Fibo_m1(self,n):
		if n == 1 or n== 2:
			result = 1
		else:
				result =self.get_Fibo_m1(n-1) + self.get_Fibo_m1(n-2)
		return result
# A memoized solution
	def get_Fibo_meo_m1(self,n):
			#memo=""
			memo = [None] * (n + 1)
			return self.get_Fibo_meo_m1(n, memo)
# A bottom-up solution
	def fib_bottom_up(self,n):
		if n == 1 or n == 2:
			return 1
		bottom_up = [None] * (n+1)
		bottom_up[1] = 1
		bottom_up[2] = 1
		for i in range(3, n+1):
			bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
		return bottom_up[n]
#Call steps for ends
############################################################################
def call_main_steps():
	start = timeit.default_timer()
	#######################################################################
	args=get_args()
	arr_m1 = int(args["input"])
	#getArr = Solution(arr_m1)
	getArr = Solution(arr_m1)
	for i in range(1,arr_m1):
		ar_m1 = getArr.get_Fibo_m1(i)
		print(ar_m1)
	########################################################################
	stop = timeit.default_timer()
	print('\n#####################The spent time of whole process ################## \n', stop - start)
	start = timeit.default_timer()
	getArr2 = Solution(arr_m1)
	for i in range(1,arr_m1):
		ar_m2 = getArr2.fib_bottom_up(i)
		print(ar_m2)
	########################################################################
	stop = timeit.default_timer()
	print('\n#####################The spent time of whole process ################## \n', stop - start)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

