#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input("Enter Hours:")
print("Amount of hours worked: ", hrs)
rate_per_hour = input("Enter rate per hour")
print("Working rate per hour: ", rate_per_hour)
try:
    h = float(hrs)
    rph= float(rate_per_hour)
except:
    print("Enter numeric value only")
    quit()
n = h-40.0 #Overtime 
gross_pay = h*rph #for the hours worked up to 40 hours
new_gross_pay_rate = 40*rph + (1.5*n*rph) #for all hours worked above 40 hours
if h <= 0:
    print("Invalid hour entered")
elif h <= 40:
    print("The gross pay is ",gross_pay)
else:
    print("The gross pay is ",new_gross_pay_rate)
