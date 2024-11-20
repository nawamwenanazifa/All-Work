#naming conventions

# 1. snake case(_)
#must have an underscore
student_name = "Nazifa"
student_reg_number ="2024/DSC/OO86/SS"
student_age = 20
course_unit ="computer science"
student_height = 155
print(student_name)
print(student_age)
print(course_unit)
print(student_reg_number)
print(student_height)

#2. Camel case
#The first letter of the first word is in lower case and the first letter of the word is in upper case
#example
studentName = "Nazifa"
studentRegNum = "2024/DSC/0086/SS"

#3. pascal case(no space)
# All words must start with a capital letter
#example 
StudentName = "Nazifa"
TotalMark = 70

#string concatenations
#use of a coma (,) and plus (+)
#we can not join a string to an int
print("my name is",student_name, ' and my age is',student_age)

#type casting
print("my name is " +student_name + ' and my height is ' + str(student_height))