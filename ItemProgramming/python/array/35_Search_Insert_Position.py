#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya 
#Email:polyaluthor@gmail.com
#Last updated:2019.10.16
#Version: 1.0 first
#need do: unit test, sort array
#Purpose: 35_Search_Insert_Position.py
#Main logic principle:
#
#
#Usage:
#     example: python 35_Search_Insert_Position.py
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
	def __init__(self,arr,target):
		self.nums=arr
		self.target=target
		#print(self.k)
	def displayShow(self):
		#for i_iter in self.digits:
		#	print(i_iter)
		print(self.nums)
	def searchInsert(self):
		n = len(self.nums)
		if n == 0 or self.target <= self.nums[0]: return 0
		if self.target > self.nums[n-1]: return n
		left, right = 0, n-1
		while left < right:
					mid = (left+right)//2
					if self.target == self.nums[mid]: return mid
					if self.target > self.nums[mid]: left = mid+1
					else: right = mid-1
		print(left)
		print(self.nums[left])
		if self.target > self.nums[left]: return left+1
		else: return left
#
#
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	start =datetime.datetime.now()
	#arr=[1,12,-5,-6,50,3,100,20,11]
	#arr=[9,2,1,2,1,9]
	arr=[1,1.5,3.5,6]
	target=4
#self test##################################
	ar=Solution(arr,target)
	ar_search=ar.displayShow()
	ar_search=ar.searchInsert()
	print("The index  of searchInsert  array: %s"%(ar_search))
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

