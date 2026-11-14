# adult_bmi_calculator.py


age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
while age <= 0 or weight <= 0 or height <= 0:
    print("Invalid input. Please enter positive values for age, weight, and height.")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
  


if age < 18:
    print("BMI calculation is not applicable for individuals under 18 years old.")
else:
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi}")
    if bmi < 18.5:
        print("(نقص الوزن)")
    elif 18.5 <= bmi < 25:
        print("(وزن صحي)")
    elif 25 <= bmi < 30:
        print("زيادة في الوزن (زيادة الوزن)")    
    elif 30 <= bmi < 35:
        print("سمنة مفرطة (الدرجة الأولى)")
    elif 35 <= bmi < 40:
        print("سمنة مفرطة (الدرجة الثانية)")
    elif bmi >= 40:
        print("سمنة مفرطة (الدرجة الثالثة)")
    else:
        print("Invalid BMI value")