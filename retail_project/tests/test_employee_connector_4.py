from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec=EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID=7

result =  ec.delete_one_employee(emp)
if result >0:
    print("Employee Deleted Successfully")
else:
    print("Employee Not Found")