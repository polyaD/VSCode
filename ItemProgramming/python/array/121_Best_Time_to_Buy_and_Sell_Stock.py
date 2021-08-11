#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#121_Best_Time_to_Buy_and_Sell_Stock.py
#Last updated:2019.4.9
#Version: 0.1
#Purpose: 121_Best_Time_to_Buy_and_Sell_Stock
#Main logic principle:
#
#travel each element
#Usage:
#     example: python 121_Best_Time_to_Buy_and_Sell_Stock.py -in 3,6,5,10,20
      usage:   python 121_Best_Time_to_Buy_and_Sell_Stock.py -in 7,1,5,3,6,4
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
#base on dynamic
	def get_Best_Time_to_Buy_and_Sell_Stock_m1(self):
		if len(self.arr) <= 1:return 0
		buy_price = self.arr[0]
		max_profit =0
		for i in range(1,len(self.arr)):
			buy_price = min(buy_price, self.arr[i])
			max_profit = max(max_profit, self.arr[i] - buy_price)
		return max_profit
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	arr_m1 = list(map(int,arr_m1))
	getArr = Solution(arr_m1)
	ar_m1 = getArr.get_Best_Time_to_Buy_and_Sell_Stock_m1()
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

