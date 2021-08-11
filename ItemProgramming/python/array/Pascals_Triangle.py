#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#Pascals_Triangle
#Last updated:2019.4.8
#Version: 0.1
#Purpose: Pascals_Triangle
#Main logic principle:
#
#convert the math format  to  get the index of row of  pascal
#Usage:
#     example: python Pascals_Triangle.py -in 5
############################################################################
"""
import os
import sys
import argparse
import pandas as pd
import math
#
#
#Get Argv
#get ready parameters and out help inforamtion
#############################################################################
def get_args():
	parse=argparse.ArgumentParser(description='annot expression in one file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 1,2,3 ")
	parse.add_argument('-in','--input',type=int,help="input ready files ")
	#parse.add_argument('-out','--out_file',type=str,help="set out name of files: eg.select.txt ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data
############################################################################
class Solution:
	def __init__(self,index):
		if index<1:
			index=1
		self.index = index-1
#base on the math of relationship
	def getRow_m1(self):
		res = [1] +[0]*self.index
		print(type(res))
		for i in range(self.index):
			res[0] =1
			for j in range(i+1,0,-1):
				res[j] = res[j]+res[j-1]
		return res
#base on the math and get the index directly
#algorithm: data structure,stored data,Steps maniplate the data structure
#math is response for solve the problems.
#algorithm convert the math format to ends
#
	def getRow_m2(self):
		rep =[]
		res =[1]
		#print(res)
		rep.append(res)
		for i in range(1,self.index+1):
			res = [1] +[res[i]+res[i+1] for  i in range(len(res)-1)]+[1]
			#print(res)
			rep.append(res)
		return rep
#
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	get_in = args["input"]
	getIndex = Solution(get_in)
	ar_m1 = getIndex.getRow_m1()
	ar_m2 = getIndex.getRow_m2()
	#print(type(ar))
	#print(ar_m1)
	for i in ar_m2:
		print(i)
	#print(ar_m2)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

