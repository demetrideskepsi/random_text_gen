import random
import time
import re

"""
generate random length words of random strings
	all letters
	all numbers
	letters and numbers
	letters and symbols
	numbers and symbols
	letters, numbers, and symbols

make regex rule that reads in and gives the best possible fake word
spit out word at type rate already tested

"""
# all letters
alpha = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h',
         'H','i','I','j','J','k','K','l','L','m','M','n','N','o','O',
         'p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w',
         'W','x','X','y','Y','z','Z']
# all numbers
numeric = ['0','1','2','3','4','5','6','7','8','9']
# all special characters
special = ['!','#','$','%','&','(',')','*','+','-','.',':',';','<','=',
           '>','?','@','[','^','_','{','|','}','~']
# punctuation
punc = ['!','.',',',';',':','?']

def run():
	length = line_length()
	line(length)
	print()

"""

		case 2:
			output = words_numbers()
		case 3:
			output = words_symbols()
		case 4:
			output = numbers_symbols()
		case 5:
			output = words_numbers_symbols()
"""


# regex word filter
# can't have more than 2 consonance in a row
# 

# defines the length of the line
def line_length():
	line_length = random.randint(1,20)
	return line_length

# runs a line
def line(length):
	for i in range(0,length):
		punc = random.randint(0,3)
		pick = random.randint(0,1)
		time_interval = random.uniform(0,.3)
		time.sleep(time_interval)
		match pick:
			case 0:
				words()
			case 1:
				numbers()

		
		if punc == 1:
			punctuation()
			print('',end=' ',flush=True)
		print('',end=' ',flush=True)

def punctuation():
	time_interval = random.uniform(0.001,.1)
	time.sleep(time_interval)
	random_punc = random.randint(0,len(punc)-1)
	print(punc[random_punc],end='',flush=True)

def words():
	length = random.randint(1,10)
	for i in range(0,length-1):
		time_interval = random.uniform(0.001,.1)
		time.sleep(time_interval)
		random_letter = random.randint(0,len(alpha)-1)
		print(alpha[random_letter],end='',flush=True)

def numbers():
	length = random.randint(1,10)
	for i in range(0,length-1):
		time_interval = random.uniform(0.001,.1)
		time.sleep(time_interval)
		random_number = random.randint(0,len(numeric)-1)
		print(numeric[random_number],end='',flush=True)

def words_numbers():
	pass

def words_symbols():
	pass

def numbers_symbols():
	pass

def words_numbers_symbols():
	pass


for i in range(0,30):
	run()
#run()
#line(12)

"""
SOURCES:

https://stackoverflow.com/questions/68444335/why-does-print-with-end-doesnt-appear-until-new-line

"""