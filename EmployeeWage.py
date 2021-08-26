import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8 
PART_TIME_HOURS = 4

class CompanyEmpWage:
    
    def __init__(self, company):

        self.wage_per_hour = company.get("wage_per_hour")
        self.number_of_working_days = company.get("number_of_working_days")
        self.work_hrs_per_month = company.get("work_hrs_per_month")
        self.company_name = company.get("company_name")
    
    def set_total_wage(self,total_wage):

        self.total_wage =  total_wage
    
    def __str__(self) -> str:

        return f"Company = {self.company_name},Total Emp Wage = {self.total_wage}"

class EmployeeWageBuilder:

    def __init__(self):

        self.company_array = []

    def add_employee(self, company):

        self.company_array.append(CompanyEmpWage(company))

    calculate_daily_wage = lambda emp_hrs,wage_per_hour : emp_hrs * wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_emp):

        emp_attendence = {
            IS_PRESENT_FULL_DAY : FULL_DAY_HOURS,
            IS_PRESENT_PART_TIME: PART_TIME_HOURS,
            IS_ABSENT: 0
            }
        return emp_attendence.get(check_emp)

    def calculate_employee_salary(self, employee):

        working_days = 0
        total_working_hours = 0
        total_wage = 0 
        while(working_days < employee.number_of_working_days and total_working_hours < employee.work_hrs_per_month):
            check_emp = random.randint(0,2)
            emp_hrs = EmployeeWageBuilder.check_emp_working_hours(check_emp) 
            total_working_hours += emp_hrs
            working_days += 1
            total_wage += EmployeeWageBuilder.calculate_daily_wage(emp_hrs, employee.wage_per_hour)
        return total_wage
    
    def calculate_employee_wage(self):

        for employee in self.company_array:
            total_wage = self.calculate_employee_salary(employee)
            CompanyEmpWage.set_total_wage(employee, total_wage)

def get_company_data():

    try:
        wage_per_hour = int(input("Enter the wage_per_hour\n"))
        number_of_working_days = int(input("Enter the number_of_working_days\n"))
        work_hrs_per_month = int(input("Enter the work_hrs_per_month\n"))
        company = input("Enter the company\n")
        if not company.isalpha() :
            print("Invalid Company Name")
            return None
        #setting data in employee details dictionary
        employee_details_dict = {}
        employee_details_dict["wage_per_hour"] = wage_per_hour
        employee_details_dict["number_of_working_days"]= number_of_working_days
        employee_details_dict["work_hrs_per_month"] = work_hrs_per_month
        employee_details_dict["company_name"] = company
        return employee_details_dict

    except Exception as e:
        print("Invalid details re-enter the data")
        return None


if __name__ == "__main__":

    print("Welcome to Employee Wage Builder")
    emp_wage = EmployeeWageBuilder()
    try:
        num_of_companies = int(input("Enter the number of Companies you want to add : \n"))
        count_company = 1

        while (count_company <= num_of_companies):
            print(f"Details for Company {count_company}")
            company = get_company_data()
            if company:
                count_company += 1
                emp_wage.add_employee(company)

        emp_wage.calculate_employee_wage()
        employees = "\n".join(str(company_data) for company_data in emp_wage.company_array)
        print(employees)
        
    except Exception as e:
        print("Entered value is invalid")