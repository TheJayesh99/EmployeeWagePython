import random
IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8 
PART_TIME_HOURS = 4

empAttendence = {
    IS_PRESENT_FULL_DAY :
    f"Employee is present for full time and the wage is {WAGE_PER_HOUR * FULL_DAY_HOURS}rs",
    IS_PRESENT_PART_TIME:
    f"Employee is present for part time and wage is {WAGE_PER_HOUR * PART_TIME_HOURS}rs",
    IS_ABSENT:
    f"Employee is absent"
    }

checkEmp = random.randint(0,2)
print(empAttendence.get(checkEmp))