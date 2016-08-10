#This program prompts for metric weight and height and outputs the BMI.
pounds= float(input('Please enter weight in pounds: '))
inch= float(input('Please enter height in inches: '))
weight= pounds * 0.453592
height= inch * 0.0254
bmi= weight /(height**2)
print('BMI is :', round(bmi,7))
    
