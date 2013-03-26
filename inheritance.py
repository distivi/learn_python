# -*- coding: utf-8 -*- 

class Shape(object):	
	def __init__(self, color):
		super(Shape, self).__init__()		
		self.color = color

	def square(self):
		print "Square is: "		

class Rectanlge(Shape):	
	width = 0.0
	height = 0.0

	def __init__(self, color, width, height):		
		super(Rectanlge,self).__init__(color)
		self.width = width
		self.heigth = height

		

	def square(self):
		super(Rectanlge,self).square()
		print self.height * self.width
		
		

s = Shape("green")
print s.color
s.square()

rect = Rectanlge("Red",12,32)
print rect.color
print rect.height

