import pickle_lab
import re

class Dictionary:
	def __init__(self,input_file,output_file):		
		self.input_file = input_file
		self.output_file = output_file

	def findExistingsWordsInDictionary(self,dictionary):
		self.input_file.seek(0,0)
		text_from_input_file = self.input_file.read()
		list_of_words = re.findall('[a-zA-Z0-9]+',text_from_input_file)
		
		for k in dictionary.keys():	
			if k in list_of_words:
				self.output_file.write(dictionary[k] + "\n")

		print "Wrote to file ",output_file.name
		output_file.seek(0,0)
		print output_file.read()
		
		

	
if __name__ == "__main__":		
	input_file = open("test.txt","r")
	output_file = open("finded_words.txt","w+")		
	d = Dictionary(input_file,output_file)

	dictionary_file = open("dictionary.txt","rb")
	dictionary = pickle_lab.getDictionaryFromFile(dictionary_file)

	d.findExistingsWordsInDictionary(dictionary)

		