from retail_project.connectors.employee_connector import EmployeeConnector

ec=EmployeeConnector()
ec.connect()
em=ec.login("putin@gmail.com","123")
if em==None:
    print("Login Failed")
else:
    print("Login Succeeded")
    print(em)

print ("List")
ds=ec.get_all_employees()
print (ds)
for emp in ds:
    print(emp)
id=3
emp=ec.get_detail_infor(id)
if emp==None:
    print("Employee Not Found")
else:
    print("Employee Found",id)
    print("Employee Detail",emp)