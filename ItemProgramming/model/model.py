


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya 
#Email:polyaluthor@gmail.com
#Last updated:2019.10.17
#Version: 1.0 first
#need do: unit test
#Purpose: 26.Remove_duplicates_from_sorted_array.py
#Main logic principle:
#
#
#Usage:
#     example: python 26.Remove_duplicates_from_sorted_array.py
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
	parse.add_argument('-in','--in_list',type=str,help="input ready files ")
	parse.add_argument('-out','--out_file',type=str,help="set out name of files: eg.select.txt ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data
############################################################################
class Solution:
	def __init__(self,arr):
		self.nums=arr
		#print(self.k)
	def displayShow(self):
		#for i_iter in self.digits:
		#	print(i_iter)
		print(self.nums)
	def len_re_duplicate(self):
		return  len(set(self.nums))
	def len_re_duplicate_m1(self):

		return  len(1)
#
#
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	start =datetime.datetime.now()
	#arr=[1,12,-5,-6,50,3,100,20,11]
	#arr=[9,2,1,2,1,9]
	arr=[1,1,3,5,6,6,6.7]
#self test##################################
	ar=Solution(arr)
	ar_len=ar.displayShow()
	ar_len=ar.len_re_duplicate()
	print("The index  of searchInsert  array: %s"%(ar_len))
	print("\n\n============================================================")
	print("Hello polya,welcome to the programming world")
	end=datetime.datetime.now()
	#print("The programming running time : "+str(end-start))
	print('The programming running time: %s Seconds'%(end-start))
	print("The programming finished time : "+str(end))
	print("============================================================")
#input from out############################
#unit test ################################ 
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

