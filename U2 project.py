weight_list = []
height_list = []
age_list = []
gender_list = []
bmr_list = []

while True:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    age = int(input("Enter age (years): "))
    gender = input("Enter gender (male/female): ").strip().lower()

    if gender not in ["male", "female"]:
        print("Invalid gender input. Please enter 'male' or 'female'.")
        continue  # Skip to next iteration if invalid input

    weight_list.append(weight)
    height_list.append(height)
    age_list.append(age)
    gender_list.append(gender)

    # BMR calculation
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
        print("Gender is male")
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        print("Gender is female")

    bmr_list.append(bmr)

    again = input("Add another person? (yes/no): ").strip().lower()
    if again != "yes":
        break


for i in range(len(weight_list)):
    print("Person", i + 1, "data:")
    print("Weight:", weight_list[i], "kg")
    print("Height:", height_list[i], "cm")
    print("Age:", age_list[i], "years")
    print("Gender:", gender_list[i])
    print("Recommended Calorie Intake (BMR):", (bmr_list[i]), "Calories")