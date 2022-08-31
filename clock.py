time_now=float(input("please enter time now"))
alarm_set=float(input("please enter the number of hours to wait for the alar"))
print("the time will be:", (time_now+alarm_set)%24)
