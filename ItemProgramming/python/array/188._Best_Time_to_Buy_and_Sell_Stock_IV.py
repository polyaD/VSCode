#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya polyaluthor@gmail.com
#188._Best_Time_to_Buy_and_Sell_Stock_IV.py
#Last updated:2019.4.16
#Version: 0.1
#Purpose: 188._Best_Time_to_Buy_and_Sell_Stock_IV.py
#Main logic principle:
#
#travel each element
#Usage:
#     example: python 188._Best_Time_to_Buy_and_Sell_Stock_IV.py -in 1,2,3,4,5 -kt 2
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
	parse=argparse.ArgumentParser(description='annot  in one file')
	parse.add_argument('-u','--usage',help="usage: python $0  -in 1,2,3 ")
	parse.add_argument('-in','--input',type=str,help="input ready files ")
	parse.add_argument('-kt','--k_time',type=int,help="input k time  ")
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
#profit DP
	def get_maxProfit(self,k,prices):
		if k <= 0 or not prices: return 0
		N = len(prices)
		if k >= N:
			sum = 0
			for i in range(1, N):
				if prices[i] > prices[i - 1]:
					sum += prices[i] - prices[i - 1]
			return sum
		g = [0] * (k + 1)
		l = [0] * (k + 1)
		for i in range(N - 1):
			diff = prices[i + 1] - prices[i]
			for j in range(k, 0, -1):
				l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
				g[j] = max(l[j], g[j])
		return g[-1]
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	arr_m1 = args["input"].split(",")
	k_times = args["k_time"]
	arr_m1 = list(map(int,arr_m1))
	getArr = Solution(arr_m1)
	ar_m1 = getArr.get_maxProfit(k_times,arr_m1)
	print(ar_m1)
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

