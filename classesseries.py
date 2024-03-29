#<#<<<<<< HEAD


class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@company.com'
       
       Employee.num_of_emps += 1
    def fullname(self):
       return '{} {}'.format(self.first, self.last)   
   
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)   
         
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test' , 'Ueser' , 60000)

print(Employee.num_of_emps)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# test





#=======


from calendar import weekday



class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@company.com'
       
       Employee.num_of_emps += 1
    def fullname(self):
       return '{} {}'.format(self.first, self.last)   
   
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)   
    @classmethod
    def set_raise_amount(cls, amount):
         cls.raise_amount = amount
         
class Developer(Employee):
       pass
    
dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

#print(dev_1.email)
#print(dev_2.email)
       
  # @classmethod
   # def from_string(cls, emp_str):
      #   first, last, pay =emp_str.split('-')
       #  return cls(first, last, pay)
         
    #@staticmethod
    #def is_workday(day):
     #   if day.weekday() == 5 or day.weekday() ==6:
      #     return False   
       # return True
     
#Employee.set_raise_amount(1.05)  
         
#emp_1 = Employee('Corey', 'Schafer', 50000)
#emp_2 = Employee('Test' , 'Ueser' , 60000)



#import datetime
#my_date = datetime.date(2016, 7, 11)

#print(Employee.is_workday(my_date))

#test to see if it changes.
##>>>>>>> c537467fb1fcfabaa9733ce5ab13b0312b678d95
