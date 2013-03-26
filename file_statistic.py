# -*- coding: utf-8 -*-
import re
# http://docs.python.org/2/library/re.html
# http://habrahabr.ru/post/60369/

def countOfCharactersFromText(text):	
	return len(text)

def countOfWordsFromText(text):	
	#return len(len(re.split('[\W]+',text)))	
	words = re.findall('[a-zA-Z0-9]+',text)	
	return len(words)	

def countOfSentencesFromText(text):
	normal_text = re.sub('\.{1,}','.',text)
	sent = re.split('\.',normal_text)	
	return len(sent)

if __name__ == "__main__":
	file_name = "Lorem_ipsum.txt"
	test_file_name = "test.txt"

	input = open(file_name,"r")
	text = input.read()
	input.close()
	print "Count of characters: ".ljust(25),countOfCharactersFromText(text)
	print "Count of words: ".ljust(25),countOfWordsFromText(text)
	print "Count of sentences: ".ljust(25),countOfSentencesFromText(text)
