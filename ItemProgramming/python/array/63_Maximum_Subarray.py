#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#Maximum_Subarray.py
#Last updated:2019.4.8
#Version: 0.1
#Purpose: Plus One from array
#Main logic principle:
#
#convert the math format  to  get the index of row of  pascal
#Usage:
#     example: python Maximum_Subarray.py -in 2,3,2,-1
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
	def get_Maximum_Subarray_m1(self):
		max_ending_here = max_so_far = self.arr[0]
		for x in self.arr[1:]:
			max_ending_here = max(x, max_ending_here + x)
			max_so_far = max(max_so_far, max_ending_here)
		return max_so_far
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	arr_m1 = list(map(int,arr_m1))
	print(type(arr_m1))
#	arr_m1 =[-7, 1, 5, 2, -4, 3, 0]
	getArr = Solution(arr_m1)
	ar_m1 = getArr.get_Maximum_Subarray_m1()
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

