
import datetime

print("Check if it's Tuesday")

today = datetime.datetime.today()
dayOfWeek = today.weekday()

if dayOfWeek == 1:
  print("It is Tuesday")
elif dayOfWeek == 3:
  print("It's Wednesday")
else: 
  print("It's not Tuesday")
