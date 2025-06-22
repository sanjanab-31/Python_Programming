class Emp:
    def __init__(self):
        print("Welcome to the Employee details")
    def empdetails(self):
        print("Empname:","SANJU")
        print("Empid:","1234")
        print("Salary:","10000")
    
class Manager(Emp):
    def __init__(self):
        print("Welcome to the Manager details")

    def Mandetails(self):
        print("Managername:","SASI")
        print("Managerid:","5678")
        print("Salary:","20000")


m=Manager()
m.Mandetails()
m.empdetails()