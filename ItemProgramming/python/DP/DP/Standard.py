#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#27_Remove_Element.py
#Last updated:2019.4.9
#Version: 0.1
#Purpose: Plus One from array
#Main logic principle:
#
#travel each element
#Usage:
#     example: python Standard.py -in 2,3,2,-1 -T 2
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
	parse.add_argument('-T','--target',type=str,help="input a target value ")
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
#base on the math of relationship
	def get_Remove_Element_m1(self):
		for element in self.arr[:]:
			if element in self.target:
				self.arr.remove(self.target)
		return len(self.arr)
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	target = args["target"]
	getArr = Solution(arr_m1,target)
	ar_m1 = getArr.get_Remove_Element_m1()
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

