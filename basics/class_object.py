# # 1) class creation
# class Student:
# 	'''This class is about Student''' #documentation string 

# print(Student.__doc__)
# help(Student)



#class and object creation
class SuperMarket:
	'''This is my supermarket'''  #documentation string

bread = SuperMarket()
bread.brand = "ABC"  #brand of the bread is ABC
bread.price = 25	#bread price is 25
biscuit = SuperMarket()
biscuit.brand = "PQR"
biscuit.price = 10
shampoo = SuperMarket()
shampoo.brand = "XYZ"
shampoo.price = 5
rice = SuperMarket()
rice.brand = "Seeragachamba"
rice.price = 65

print(biscuit.__dict__)
