print("0 : Sunday")
print("1 : Monday")
print("2 : Tuesday")
print("3 : Wednesday")
print("4 : Thursday")
print("5 : Friday")
print("6 : Saturday")

current_day = int(input("Enter your current day number: "))
Day_After =  int(input("Enter number of the before day: "))

result_day = (current_day-Day_After)%7

if result_day == 0:
    print("Sunday")
elif result_day == 1:
    print("Monday")
elif result_day == 2:
    print("Tuesday")
elif result_day == 3:
    print("Wednesday")
elif result_day == 4:
    print("Thursday")
elif result_day == 5:
    print("Friday")
else:
    print("Saturday")

