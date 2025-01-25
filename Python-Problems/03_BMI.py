#BMI Body Mass Index

weight = float(input('Enter your weight in Kilograms! '))
height = float(input('enter your height in Meters! '))

bmi = weight/ height ** 2

BMI = int(bmi)
print(BMI)