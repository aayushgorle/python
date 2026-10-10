Temp = int(input("Enter Tempreture: "))

if Temp <= 0 :
    print("Tempreture below Zero - Freezing")
if 0 < Temp <= 30 :
    print("Tempreture is Normal")
if 31 <= Temp <= 60:
    print("Tempreture is rising warm")
if 61 <= Temp:
    print("Tempreture is critical")