# -*- coding: utf-8 -*- 

#   //// ////// ////   ////
#  //	  //   //_//  //
# ////   //   //  // ////

import pickle

def insertDictionaryToFile(d,file_):	
	pickle.dump(d,file_) 

def getDictionaryFromFile(file_):	
	return pickle.load(file_)

def insertWordToDictionary(d):
	k = raw_input("Insert key: ")
	v = raw_input("Insert value: ")
	if k not in d:
		d[k] = v
	else:
		print "Word is in dictionary already"

def showDictionary(d):
	for k,v in d.items():
		print k.ljust(20),"|",v

if __name__ == "__main__":
	dictionary = {}	
	while len(dictionary) < 2:
		insertWordToDictionary(dictionary)
	print "\n\nDictionary from memory:"
	showDictionary(dictionary)

	file_name = "dictionary.txt"
	output_file = open(file_name,'wb')
	insertDictionaryToFile(dictionary,output_file)
	output_file.close()

	pkl_file = open(file_name,'rb')
	print "\n\nDictionary from file:"
	dictionary = getDictionaryFromFile(pkl_file)	
	showDictionary(dictionary)
	pkl_file.close()