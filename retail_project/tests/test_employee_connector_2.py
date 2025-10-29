from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec=EmployeeConnector()
ec.connect()
emp=Employee()
emp.EmployeeCode="EMP888"
emp.Name="Doraemon"
emp.Phone="0123456789"
emp.Email="doraemon@gmail.com"
emp.password="123"
emp.IsDeleted="0"
result =  ec.insert_one_employee(emp)
if result >0:
    print("Employee Inserted")
else:
    print("Employee Not Found")