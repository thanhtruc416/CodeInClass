from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec=EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID=7
emp.EmployeeCode="K23416"
emp.Name="k23416"
emp.Phone="0123456789"
emp.Email="k23416@gmail.com"
emp.password="789"
emp.IsDeleted="0"
result =  ec.update_one_employee(emp)
if result >0:
    print("Employee Inserted")
else:
    print("Employee Not Found")