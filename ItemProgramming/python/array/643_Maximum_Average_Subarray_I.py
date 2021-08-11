#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya 
#Email:polyaluthor@gmail.com
#Last updated:2019.time
#Version: 1.0 first
#need do: unit test
#Purpose: 643_Maximum_Average_Subarray_I
#Main logic principle:
#
#
#Usage:
#     example: python 643_Maximum_Average_Subarray_I.py
############################################################################
"""
import os
import sys
import datetime
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
	def __init__(self,arr,k):
		self.arr=arr
		self.k=k
		#print(type(self.arr))
		#print(self.k)
	def findMaxAverage(self):
		print(type(self.arr))
	#	"""
		#print(self.k)
		#su slice.su to store the sum of k element, slice steps,move one steps
		su=0
		largest = float('-inf')
		for i,num in enumerate(self.arr):
		#	print(num)
	#		print(str(i)+"  current")
			su+=num
	#		print(str(self.k)+"  slice window")
	#		print(str(i-self.k)+"  remove")
			if i>=self.k:
				su-=self.arr[i-self.k]
			if i>=self.k-1:
				largest=max(su,largest)
				#print(largest)
		return float(largest)/self.k
	#	 """
#
#
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	start =datetime.datetime.now()
	arr=[1,12,-5,-6,50,3,100,20,11]
	k=4
	#print(k)
#self test##################################
	ar=Solution(arr,k)
	ar_ends=ar.findMaxAverage()
	print("The max average of k array: %s"%(ar_ends))
	print("Hello polya,welcome to the programming world")
	end=datetime.datetime.now()
	#print("The programming running time : "+str(end-start))
	print('Running time: %s Seconds'%(end-start))
	print("The programming finished time : "+str(end))
#input from out############################
#unit test ################################ 
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

