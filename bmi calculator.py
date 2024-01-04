h=float(input("Enter your height in meters: "))
w=float(input("Enter your Weight in Kg: "))
bmi=w/(h*h)
print("BMI Calculated is:  ",bmi)
 
if(bmi>0):
    if bmi>=16.0 and bmi<18.5:
        print("Underweight")
    elif bmi>=18.5 and bmi<25.0:
        print("Normal")
    elif bmi>=25.0 and bmi<40.0:
        print("Overweight")
else :
    print("Invalid height or weight")