weight_list = []
height_list = []
age_list = []
gender_list = []

while True:
   weight = float(input("Enter weight (kg): "))
   height = float(input("Enter height (cm): "))
   age = int(input("Enter age (years): "))
   gender = input("Enter gender (male/female): ").strip().lower()

   weight_list.append(weight)
   height_list.append(height)
   age_list.append(age)
   gender_list.append(gender)

   if gender == "male":
       print("Gender is male")
   elif gender == "female":
       print("Gender is female")
   else:
       print("Invalid gender input")

   again = input("Add another person? (yes/no): ").strip().lower()
   if again != "yes":
       break



