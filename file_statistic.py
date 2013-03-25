# -*- coding: utf-8 -*-
import re

def countOfCharactersFromFile(file_):
	return len(file_.read())

def countOfWordsFromFile(file_):
	file_.seek(0,0)
	return len(re.split('[\W]+',file_.read()))

def countOfSentencesFromFile(file_):
	return len(file_.read())


file_name = "Lorem_ipsum.txt"
test_file_name = "test.txt"

input = open(test_file_name,"r")
print "Count of characters: ".ljust(25),countOfCharactersFromFile(input)
print "Count of words: ".ljust(25),countOfWordsFromFile(input)
