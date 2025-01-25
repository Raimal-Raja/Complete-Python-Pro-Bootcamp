height = float(input("Enter your height! "))
weight = float(input("Enter your weight! "))

bmi = weight / height ** 2

BMI = int(bmi)

if BMI < 18.5:
    print("You are underweight!")
    
elif BMI > 18.5 and BMI < 25:
    print(" You are normal weighted!")
    
elif BMI > 25 and BMI < 30:
    print("you are overweighted!")
    
elif BMI > 30 and BMI < 35:
    print("You are obese")
    
else:
    print("You are clincally obese")