#-----------------------
#Title: Chapter 1 tasks
#Page: 12
#Date: 06/05/25
#-----------------------

#Question 1:
age=5
print("Age:", age, "\nWhat a great age!")
print()

#Question 2:
num1=9.81
num2=3.14

sum=num1+num2
difference=num1-num2
product=num1*num2

print("Sum:", sum, "\nDifference:", difference, "\nProduct:", product)
print()

#Question 3:
num1 #9.81
num2 #3.14

average=sum/2
r1=(num1/num2-num1//num2)*num2
#r1=(3.1242-3)*3.14
r2=(num2/num1-num2//num1)*num1

print("Average:", average)

print("Remainder after 9.81/3.14:", r1)
print("Remainder after 3.14/9.81:", r2)

print("Average squared:", average**2)
print()

#Question 4:
Fahrenheit=87
Celsius=(5/9)*(Fahrenheit-32)
Celsius=round(Celsius, 0)

print("Degrees Fahrenheit:", Fahrenheit)
print("Degrees Celsius:", Celsius)
print()

#Question 5:
distance=14401 #Kilometers
mile=1.60935 #km
price=900 #900 euro per mile

noMiles=distance/mile
Cost=price*noMiles

print("Distance in km:", distance, "km")
print("Distance in miles:", round(noMiles, 2), "miles")
print()

#Question 6
r=3 #metres
h=5 #metres
pi=3.14
totalLiquid=21342 #m^3

Volume=pi*(r**2)*h
Num=totalLiquid/Volume

print("Total Volume of Liquid:", totalLiquid)
print("Volume of cylinder:", Volume, "m^3")
print("Number of cylinders needed to move the water:", round(Num, 0))
print()

#Question 7
wEarth=80 #kg
wMoon=0.165*wEarth

print("Weight on Earth:", wEarth, "kg")
print("Weight on Moon:", wMoon, "kg")
print()

#Question 8
lengthGarden=50 #metres
widthGarden=30
lengthHouse=15
widthHouse=10

areaGarden=(lengthGarden*widthGarden-lengthHouse*widthHouse) 
time=areaGarden/2 #seconds

print("Area of garden:", round(areaGarden, 2), "m^2")
print("Time:", round(time/60, 2), "minutes")
