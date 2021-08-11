#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#find_pivot_index.py
#Last updated:2019.4.8
#Version: 0.1
#Purpose: find_pivot_index
#Main logic principle:
#
#convert the math format  to  get the index of row of  pascal
#Usage:
#     example: python find_pivot_index.py -in 1,2,3,9
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
	parse.add_argument('-in','--input',type=str,help="input ready digits ")
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
	def get_Equilibrium_m1(self):
		total_sum = sum(self.arr)
		leftsum=0
		for i ,num in enumerate(self.arr):
			#for index i
			total_sum -=num
			if leftsum==total_sum:
				return i
			leftsum+=num
		return -1
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	arr_m1 = list(map(int,arr_m1))
	print(type(arr_m1))
#	arr_m1 =[-7, 1, 5, 2, -4, 3, 0]
	getArr = Solution(arr_m1)
	ar_m1 = getArr.get_Equilibrium_m1()
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

