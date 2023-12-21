# # 1) class creation
# class Student:
# 	'''This class is about Student''' #documentation string 

# print(Student.__doc__)
# help(Student)



# #class and object creation
# class SuperMarket:
# 	'''This is my supermarket'''  #documentation string

# bread = SuperMarket()
# bread.brand = "ABC"  #brand of the bread is ABC
# bread.price = 25	#bread price is 25
# biscuit = SuperMarket()
# biscuit.brand = "PQR"
# biscuit.price = 10
# shampoo = SuperMarket()
# shampoo.brand = "XYZ"
# shampoo.price = 5
# rice = SuperMarket()
# rice.brand = "Seeragachamba"
# rice.price = 65

# print(biscuit.__dict__)


#Constructor:
class SuperMarket:
	'''This is my supermarket'''  #documentation string
	def	__init__(self,brand, price, discount=None):#formal parameters
		self.brand = brand
		self.price = price
		self.discount = discount
		#print("Check me Check me check me")
	
#self

bread = SuperMarket("ABC", 25, 25)		#actual parameters
print(bread.brand)
biscuit = SuperMarket("PQR", 10.50, 25)
shampoo = SuperMarket("XYZ", 5, 25)

rice = SuperMarket("Seeragachamba", 65)  #actual : 2
print(rice.discount)


