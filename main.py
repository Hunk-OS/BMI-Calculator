while True:

    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in Kilograms: "))

        BMI = weight / round(height**2)
        r_BMI = round(BMI, 3)

        if BMI < 18.5:
            print(f"Your BMI is {r_BMI} and you are UNDERWEIGHT")
        elif BMI < 25:
            print(f"Your BMI is {r_BMI} and you are NORMAL WEIGHT")
        elif BMI < 30:
            print(f"Your BMI is {r_BMI} and you are slightly OVERWEIGHT")
        elif BMI < 35:
            print(f"Your BMI is {r_BMI} and you are OBESE")
        else:
            print(f"Your BMI is {r_BMI}, You are clincally OBESE")

        break # Exits the loop if the inputs are valid

    except ValueError:
        print("Please enter valid numeric values for height and weight.")
 
