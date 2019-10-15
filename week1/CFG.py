#!/usr/bin/env python3
""" NLP HW Language Generation CFG """
# # -*- coding: utf-8 -*-
__author__ = "Maria Diaz"

import sys 
import re

def randsent():
	file_name = sys.argv[1]+".txt"
	num_sentences = int(sys.argv[2])
	
	print(file_name)
	print(num_sentences)
	# matches non white space  ,  or new lines 
	#alltypes = re.findall(r'\S+|\n',f.read())

