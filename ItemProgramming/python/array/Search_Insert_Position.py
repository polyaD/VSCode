#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#Plus One
#Last updated:2019.4.8
#Version: 0.1
#Purpose: Search_Insert_Position
#Main logic principle:
#
#
#Usage:
#     example: python Search_Insert_Position.py -in 2,3,2 -T 3
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
#usage:python Search_Insert_Position.py -in 2,3,4 -T 10
#############################################################################
def get_args():
	parse=argparse.ArgumentParser(description='leetcode test file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 1,2,3 ")
	parse.add_argument('-in','--input',type=str,help="input ready files ")
	parse.add_argument('-T','--target',type=str,help="input target value ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data
############################################################################
class Solution:
	def __init__(self,arr,target):
		self.arr = arr
		self.target = target
#base on list attribute
	def get_Search_Insert_Position_m1(self):
		if( len(self.arr) == 0 ):return 0
		if self.target in self.arr:
					#print(self.arr.index(self.target))
					return(self.arr.index(self.target))
		else:
			for i in range(len(self.arr)):
					if(self.arr[i] >= self.target):
						return i
			return len(self.arr)
#base on the binary search characters
	def get_Search_Insert_Position_m2(self):
		size = len(self.arr)
		#if self.target >self.arr[]
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	target = args["target"]
	arr_m1 = list(map(int,arr_m1))
	target = int(target)
	#print(type(arr_m1))
#	arr_m1 =[-7, 1, 5, 2, -4, 3, 0]
	getArr = Solution(arr_m1,target)
	ar_m1 = getArr.get_Search_Insert_Position_m1()
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

