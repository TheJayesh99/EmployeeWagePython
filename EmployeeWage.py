import math
import random
IS_PRESENT = 1
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8 

checkemp = random.randint(0,1)
if checkemp == IS_PRESENT:
    print(f"Employee is present and the wage is {WAGE_PER_HOUR * FULL_DAY_HOURS}rs")
else:
    print("Employee is absent")