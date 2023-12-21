# types of variable

# 1) Instance
# 2) class (static variable)
# 3) local



class SuperMarket:
	'''This is my supermarket'''  
	manufacturer = 'Muthu Supermarket'          #manufacturer,marketer => class or static varibles
	marketer = 'MSM'
	
	def	__init__(self,x, y, z=None):
		self.brand = x                          # self.brand,self.price,self.discount => instance variables
		self.price = y
		self.discount = z
	

bread = SuperMarket("ABC", 25, 25)		
print(bread.brand)
print(SuperMarket.manufacturer)
print(SuperMarket.marketer)

class calc:
	def add(self,n1,n2):                             # n1 ,n2 => local variables
		print(n1+n2)
		
c=calc()
c.add(3,4)
