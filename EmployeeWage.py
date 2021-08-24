import random
IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8 
PART_TIME_HOURS = 4
TOTAL_WORKING_DAYS = 20 

empAttendence = {
    IS_PRESENT_FULL_DAY : WAGE_PER_HOUR * FULL_DAY_HOURS,
    IS_PRESENT_PART_TIME: WAGE_PER_HOUR * PART_TIME_HOURS,
    IS_ABSENT: 0
    }

totalWage = 0
for i in range(TOTAL_WORKING_DAYS):
    checkEmp = random.randint(0,2)
    totalWage = totalWage + empAttendence.get(checkEmp)

print("Employee total wage is ",totalWage)