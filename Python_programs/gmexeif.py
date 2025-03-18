from datetime import datetime

current_time = datetime.now()
print(current_time)
print(type(current_time))
current_hour = datetime.now().hour
current_day = datetime.now().day
print(current_hour,type(current_hour))
print(current_day)
current_hour = 20
if current_hour >= 5 and current_hour < 12:
    print("GM")
elif current_hour >=12 and current_hour <17:
    print("GA")
elif current_hour >= 17 and current_hour <21:
    print("GE")
else:
    print("GN")