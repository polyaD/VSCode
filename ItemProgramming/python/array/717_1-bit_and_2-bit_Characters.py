#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
############################################################################
#Author:polya 
#Email:polyaluthor@gmail.com
#Last updated:2019.10.14
#Version: v.1.0 #first give a run 
#         v.1.1 #add  choose parameter
#Purpose: 717_1-bit_and_2-bit_Characters.py
#Main logic principle:
#whether the array is composed by two kinds of structure
#
#Usage:
#     example: python 717_1-bit_and_2-bit_Characters.py -l 1,0,0,1
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
	parse.add_argument('-u','--usage',help="usage: python $0  -l 1,0,0,1 ")
	parse.add_argument('-l','--in_list',type=str,help="input only 0 or 1 character split by , ")
	parse.add_argument('-out','--out_file',type=str,help="set out name of files: eg.select.txt ")
	args=parse.parse_args()
	return vars(args)
############################################################################
#
#
#Do somthing for data
############################################################################
class Solution():
	def __init__(self,bits):
		self.bits = bits
	#for test display
	def displayCheckInfo(self):
		for i_ter in self.bits:
			print(i_ter)
			if i_iter:
				return(-1)
	#	print(type(len(self.bits)))
	#"""
	def isOneBitCharacter(self):
		i = 0
		while i<(len(self.bits) - 1):
			i += int(self.bits[i]) + 1
		return i == len(self.bits)-1
	#"""
#
#
#check input 
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg
#Call steps for ends
############################################################################
def call_main_steps():
	args=get_args()
	#self test
	#bits =[1,1,1,0]
	bits =[1,0,0]
	print(bits)
	bitsChar = Solution(bits)
	bitsChar.display()
	bits_char=bitsChar.isOneBitCharacter()
	print(bits_char)
############################################################################
	#from out of  input
	if args['in_list']:
		#bits=args.in_list.split(",")
		bits=args['in_list'].split(",")
		print(type(bits))
		bitsChars = Solution(bits)
		bitsChars.display()
		bits_chars=bitsChars.isOneBitCharacter()
		print(bits_chars)
############################################################################
	#unit test
#
#main
############################################################################
if __name__=='__main__':
	call_main_steps()

