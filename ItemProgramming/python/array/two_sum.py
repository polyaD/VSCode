#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#Last updated:2019.3.26
#Version: 0.1
#Purpose: two sum
#Main logic principle:
#
#
#Usage:
#     example:
############################################################################
"""
import os
import sys
import argparse
import pandas as pd
#
#
#Get Argv
#get ready parameters and out help inforamtion
#############################################################################
def get_args():
	parse=argparse.ArgumentParser(description='annot expression in one file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 1,2,3 ")
	parse.add_argument('-f','--file',type=str,help="input ready files ")
	parse.add_argument('-out','--out_file',type=str,help="set out name of files: eg.select.txt ")
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
	def twoSum(self):
		numbers={}
		for index,value in enumerate(self.arr):
			if value in numbers:
				return [numbers[value],index]
			numbers[self.target-value] = index
		return None
		
#
#
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	ar = [1,8,9,2,11]
	print(ar)
	twoSum_ar = Solution(ar,10)
	TS=twoSum_ar.twoSum()
	print(TS)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

