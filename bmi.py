def bmi(height, weight):
    print("height=" + str(height))
    print("weight=" + str(weight))

    bmi = weight / (height ** 2)
    print("BMI=" + str(bmi))
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 25:
        print("Normal")
    else:
        print("Overweight")

bmi(height=1.73, weight=57) 
