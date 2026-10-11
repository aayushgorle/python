import math
Name = str(input("Enter Name: "))
p = int(input("Enter Principal: "))
r = int(input("Enter Annual Interest  Rate: "))
n = int(input("Enter Compound Frequency per year: "))
t = int(input("Enter Period in years: "))

a = p*(1 + (r/(100*n)))**(n*t)
Interest = a - p

print(round(a, 2))
print(round(Interest, 2))
