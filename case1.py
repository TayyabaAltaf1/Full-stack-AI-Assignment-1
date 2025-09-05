#Q1: Celsius to Fahrenheit
# Q1: Write a program that converts a temperature from Celsius to Fahrenheit.
# Formula: Fahrenheit = (Celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


#Q2: Area of Rectangle 
# Q2: Calculate Area of a Rectangle 
length = float(input("Enter length of rectangle: ")) 
width = float(input("Enter width of rectangle: ")) 
area = length * width 
print("Area of rectangle:", area)


#Q3: Compound Interest
# Q3: Calculate Compound Interest
# Formula: CI = P * (1 + R/100)**T - P
# where P = principal, R= rate, T= time
		
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = int(input("Enter Time (years): "))
CI = P * (1 + R/100)**T - P
print("Compound Interest:", CI)



#Q4 Perimeter of rectangle
# Q4 perimeter of a rectangle - Take length and width as input and calculate the perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter  = 2 * (length + width)
print("perimeter of rectangle:", perimeter)


#Q5 Average of three numbers
# Q5 Average of three numbers - input three numbers and print their average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average:", average)


#Q6 Square and cube
# Q6 square and cube of a number - Ask the user for a number and display its square and cube
num = float(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)


#Q7 Distribute candies
#Q7 distribute items equally  - You have n candies and k students. 
#  
#how many candies each student gets 
#how many are left
n = int(input("Enter number of candies: "))
k = int(input("Enter number of students: "))
each = n // k
left = n % k
print("Each student gets:", each, "candies")
print("candies left:", left)


#Q8 Profit or loss
#Q8 calculate profit or loss
#Input cost price and selling price. Display either: 
#Profit and amount, or 
#Loss and amount, or 
#No Profit No Loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit:", sp -cp)
elif cp > sp:
    print("Loss:", cp - sp)
else: 
    print("No Profit No Loss")    


#Q9 Total Marks and percentage
# Q9 Total marks, percentage, and average
#Input marks of 5 subjects. Print: 
# Total marks 
# Percentage 
# Average
marks = []
for i in range(5) :
    m = float(input(f"Enter marks for subject {i+1}: ")) 
    marks.append(m)
total = sum(marks)
percentage = (total / (5 * 100)) * 100
average = total / 5

print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Average Marks:", average)


#Q10 Salary calculator
#  Q10 salary calculator
#Input basic salary. Calculate: 
# HRA = 20% of basic 
# DA = 15% of basic 
# Total Salary = Basic + HRA + DA
basic = float(input("Enter basic salary: "))
hra = 0.20 * basic
da = 0.15 * basic
total_salary = basic + hra + da

print("HRA:", hra)
print("DA", da)
print("Total Salary", total_salary)


#Q11 Age in months and days
# Q11: Age in months and days
#Input your age in years. Calculate and print age in: 
# Months 
# Days (approximate)
years = int(input("Enter your age in years: "))
months = years * 12
days = years * 365 # approx
print("Age in Months:", months)
print("Age in Days:", days)



#Q12 Currency converter
# Q12 currency converter (USD to PKR)
#Input amount in USD. Convert using a fixed exchange rate.
usd = float(input("Enter amount in USD: "))
rate = 280  # Fixed exchange rate example
pkr = usd * rate
print("Amount in PKR:", pkr)



#Q13 Sum of first N natural numbers
# Q13 sum of first n natural numbers
#Input a number n, calculate sum of first n natural numbers. 
#Formula: sum = n * (n + 1) / 2

n = int(input("Enter a number: "))
total = n * (n + 1) // 2
print("sum of first", n, "numbers:", total)


#Q14 Percentage of correct answers
#Q14 percentage of correct answers
#Input total questions and correct answers, and calculate the percentage score.
total = int(input("Enter total number of questions: "))
correct = int(input("Enter correct answers: "))
percentage = (correct / total) * 100
print("Percentage Score:", percentage, "%")


#Q15 speed, distance, time
# speed , distance, and time
#Input distance and time, and calculate speed.
distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hours): "))
speed = distance / time
print("speed:", speed, "km/h")


#Q16: Body mass index
#Q16 calculate BMI
#Input weight (kg) and height (m), then calculate: 
#BMI = weight / (height ** 2)
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print("BMI:", bmi)



#Q 17 convert minutes to hours
#  Q17 convert minutes to hours and minutes
#Input number of minutes and convert to hours and remaining minutes. 
#Example: 130 minutes → 2 hours 10 minutes
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining = minutes % 60 
print(f"{minutes} minutes = {hours} hours {remaining} minutes")