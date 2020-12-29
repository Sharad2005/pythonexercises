height=float(input("plese enter your height in foot: "))
weight=float(input("plese enter your weight in kg: "))
kg=weight*2.20462
inchs=height*12
Bmi=(kg/(inchs*inchs))*703
print("average Bmi:",round(Bmi,2))
if(Bmi<=18.5):
    print("you are underweight")
elif(Bmi>18.5 and Bmi<=24.9):
    print("you are normal weight")
elif(Bmi>24.9 and Bmi<=29.9):
    print("you are overweight")
else:
    print("you are obesity")