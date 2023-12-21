# types of methods

# 1) Instance method
# 2) class method
# 3) static method


# #Instance Methods
# class student:
#     def __init__(self,name,marks) -> None:
#         self.name=name
#         self.total=marks

#     def display(self):                                #instance method
#         print("Hi ",self.name)

# s1=student("Siva",550)
# s1.display()




# #class method
# class student:
#     noOfHolidays=10

#     @classmethod                                      #class method
#     def display_holidays(cls,branch):       
#         print("In the ",branch," branch has holidays :",cls.noOfHolidays,)

# student.display_holidays("Research")


#static method

class calculator:                       
    @staticmethod                                       #static method
    def add(n1,n2):
        print("total: ",n1+n2)

calculator.add(10,20)