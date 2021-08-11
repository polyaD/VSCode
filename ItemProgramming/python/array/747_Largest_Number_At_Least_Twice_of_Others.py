#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#747_Largest_Number_At_Least_Twice_of_Others.py
#Last updated:2019.4.9
#Version: 0.1
#Purpose: find the largest number 
#Main logic principle:
#
#travel each element
#Usage:
#     example: python 747_Largest_Number_At_Least_Twice_of_Others.py -in 3,6,5,10,20
############################################################################
"""
import os
import sys
import argparse
import pandas as pd
import math
#
#Get Argv
#get ready parameters and out help inforamtion
#############################################################################
def get_args():
	parse=argparse.ArgumentParser(description='annot expression in one file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 1,2,3 ")
	parse.add_argument('-in','--input',type=str,help="input ready files ")
#	parse.add_argument('-T','--target',type=str,help="input a target value ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data
############################################################################
class Solution:
	def __init__(self,arr):
		self.arr = arr
#base on the math of relationship
	def get_Largest_Number_At_Least_Twice_of_Others_m1(self):
		maxIndex = 0
		for i in range(0,len(self.arr)):
			if(self.arr[i]>self.arr[maxIndex]):
				maxIndex = i
		for i in range(0,len(self.arr)):
			if (maxIndex != i and self.arr[maxIndex] < (2 * self.arr[i])):
				return -1
		return maxIndex
#sort data and find the index by api
	def get_Largest_Number_At_Least_Twice_of_Others_m2(self):
		arr_copy = self.arr[:]
		if(len(self.arr)==1): return 0
		else:
			self.arr.sort()
			if self.arr[-1] >= self.arr[-2]*2 :
				return arr_copy.index(self.arr[-1])
			else:
				return -1
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	arr_m1 = list(map(int,arr_m1))
	getArr = Solution(arr_m1)
	ar_m1 = getArr.get_Largest_Number_At_Least_Twice_of_Others_m1()
	print(ar_m1)
	ar_m2 = getArr.get_Largest_Number_At_Least_Twice_of_Others_m2()
	print(ar_m2)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

