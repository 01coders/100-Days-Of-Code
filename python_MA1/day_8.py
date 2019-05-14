'''
Created on Tue May 14 2019
author: @Manoj Athreya A
'''
import re
class Employee:
    counter=1000
    def __init__(self, employeename, typeofemployee,telephoneno,skillset): #Constructor
        self.__employeeid=Employee.counter
        self.__employeename=employeename
        self.__typeofemployee=typeofemployee
        self.__telephoneno=telephoneno
        self.__skillset=skillset
        Employee.counter+=1

  
    
    def getemployeeId(self):
        return self.__employeeid
    def getemployeename(self):
        return self.__employeename
    def gettypeofemployee(self):
        return self.__typeofemployee
    def gettelephoneno(self):
        return self.__telephoneno
    def getskillset(self):
        return self.__skillset
    def validatetelephoneno(self):
        if re.match('1[0-9]{9}', str(self.__telephoneno)):
            return True
        return False


class Salary:
    basicpay=5000
    def calculatesalary(self):
        return Salary.basicpay



class PermanentEmployee(Employee, Salary):
    def __init__(self,employeename, typeofemployee,  telephoneno, skillset, yearsofexperience):
        super().__init__(employeename, typeofemployee, telephoneno, skillset) #superclass constructor
        self.__yearsofexperience=yearsofexperience
        self.__allowance=0
        self.__salary=0
        
    def validatetypeofemployee(self): 
        if re.match('[pP]',self.gettypeofemployee()) :
            return True
        return False
    
    def calculatesalary(self):
        if self.validatetelephoneno():
            if self.validatetypeofemployee():
                if self.__yearsofexperience>=5 and self.__yearsofexperience <10:
                    self.__allowance=0.05*super().calculatesalary()
                elif self.__yearsofexperience>=10 and self.__yearsofexperience<15:
                    self.__allowance=0.1*super().calculatesalary()
                else:
                    self.__allowance=0.2*super().calculatesalary()
                self.__salary=super().calculatesalary()+self.__allowance
                return self.__salary
            else:
                print("Employee is not permanent employee")
        else:
            print("Tele Phone number is not valid")
        


class Consultant(Employee, Salary):
    def __init__(self, employeename, typeofemployee, telephoneno, skillset, noofhours):
        super().__init__(employeename, typeofemployee, telephoneno, skillset) #superclass constructor
        self.noofhours=noofhours
        self.payrateperhour=0
        self.consultantfee=0

    def caculatesalary(self):
        if self.validatetelephoneno():
            if self.gettypeofemployee().upper()=='C':
                if self.getskillset()=="JEE":
                    self.payrateperhour=500
                elif self.getskillset()=="MS":
                    self.payrateperhour=350
                else:
                    self.payrateperhour=250
                self.consultantfee=super().calculatesalary()+self.payrateperhour
                return self.consultantfee
            else:
                print("Employee is not a consultant")
        else:
            print("Phone number is not valid")
        

#Project Class

class Project:
    counter=5000
    def __init__(self):
        self.__projecttechnology=["JEE", "MS"]
        self.__projectid = "P"+str(Project.counter)
    def allocateproject(self, employee): #aggregation with Employee class
        eligible=""
        if employee.gettypeofemployee().upper()=='C' or employee.gettypeofemployee().upper()=='P':
            if employee.getskillset() in self.__projecttechnology:
                eligible="You are allocated to Project id: P"+str(Project.counter)
                Project.counter+=1
            else:
                eligible="You do not have the required skillset"
        else:
            eligible="You are not a valid employee"
        return eligible

    


e1 = PermanentEmployee("John", 'P', "1111111111L", "MS", 10)
print("Employee number:", e1.getemployeeId())
print("Salary:", e1.calculatesalary())
e2 = PermanentEmployee("Mary",'p', "9999999999L", "MS", 5)
print("Employee number:", e2.getemployeeId());
print("Salary:", e2.calculatesalary());
e3 = PermanentEmployee("Veena",'c', "1999999999L", "MS", 5);
print("Employee number:", e3.getemployeeId());
print("Salary:", e3.calculatesalary());
c1 = Consultant("Joe", 'C', "1111111111L", "JEE", 12);
print("Employee number:",c1.getemployeeId());
print("Salary:",c1.caculatesalary());
c2 = Consultant("Tom", 'p', "1111111111L", "JEE", 12);
print("Employee number:", c2.getemployeeId());
print("Salary:", c2.caculatesalary());
p = Project ();
print("Project Id: ", p.allocateproject(e1))
p1 = Project ()
print("Project Id: ", p1.allocateproject(c1));
p2 = Project();
print("Project Id: ", p2.allocateproject(e3));
