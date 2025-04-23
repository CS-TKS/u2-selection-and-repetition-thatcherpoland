weight_list = []
height_list = []
age_list = []
gender_list = []

while True:
    print("Enter details for the person")
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in centimeters: "))
    age = int(input("Enter age in years: "))
    gender = input("Enter gender (Male/Female): ").strip().lower()

    weight_list.append(weight)
    height_list.append(height)
    age_list.append(age)
    gender_list.append(gender)