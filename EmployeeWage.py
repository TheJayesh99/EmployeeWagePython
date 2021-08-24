import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8 
PART_TIME_HOURS = 4

def  calculateEmployeeWage(wagePerHour ,numberOfWorkingDays,workHrsPerMonth,company):
    empAttendence = {
        IS_PRESENT_FULL_DAY : FULL_DAY_HOURS,
        IS_PRESENT_PART_TIME: PART_TIME_HOURS,
        IS_ABSENT: 0
        }

    workingDays = 0
    totalWorkingHours = 0

    while(workingDays < numberOfWorkingDays and totalWorkingHours < workHrsPerMonth):
        checkEmp = random.randint(0,2)
        totalWorkingHours = totalWorkingHours + empAttendence.get(checkEmp)
        workingDays = workingDays + 1

    totalWage = totalWorkingHours * wagePerHour
    print(f"{totalWorkingHours} \t {workingDays}")
    print(f"Employee total wage for Company {company} is {totalWage}")

calculateEmployeeWage(20,20,100,"Dmart")
calculateEmployeeWage(30,25,110,"Jio")