# write a programme that takes two numbers as input and displays their sum, difference, product and their quotient?
# write a programme that compires two intergers and print whether the first number is greater than,lessthan or equal to the second number
# write a programme that checks if the given number is between ten and twenty(20 incusive)
# write a programme that prints the squares of all intergers from one to ten using a loop



number_one=4
number_two=8
sum = number_one + number_two
print(f"sum:{sum}")

#2. comparisons
#greater than (>)(8>4)=true
#less than (<)(8<4)=false
#equal to (=)(8=4)=false 
#1. whrite a simple programme that asks a user their age if the user is above i8 print (Adult) you are gualified. if the user is lessthan i8 print you are not qualified
#2. we have folowing details and marks enter these details from the key board
#student name = Ritah li2
#student number = SEP23/BCS/14
#programming =78
# computer application = 55
# data science = 89 
# calculate the average mark and print the answer in 3 decimal places
 #3. whrite a programme that convert celcius temperature to fahrenheit.The programme should ask the user to enter the temp in celcious degrees and then displays the temperature converted to fananaheight
 #4. A cars miles per gallaton can be calculated with in the following formula MPG=milesDriven/gallons of GasUser.whrite a programme that asks a user for the number  of miles driven and gallons used . it should calculate the cars miles per _galons _used and display the results 
 
 
 
 #solution
 #No.1
age = int(input("Enter your age"))
age >=18 
print("you are an adult and qualified,")
age <=18
print("you are not qualified,") 

#No.2
student_name = input("Enter the student's name: ")
student_number = input("Enter the student' number: ")

programing_marks = int(input("Enter marks for programming: "))
data_science_marks = int(input("Enter marks for data science: "))
computer_applications_marks= int(input("Enter marks for computer applications: "))
total_marks = data_science_marks + computer_applications_marks  + programing_marks
number_of_subjects =3 
average = total_marks/number_of_subjects


print("\n---Student Details ---")
print(f"student_name: {student_name}")
print(f"student_number: {student_number}")
print(f"data_science_ marks: {data-science}")
print(f"computer_application_ marks: {computer_applications}")
print(f"The average mark for {data_science} ({computer_applications}) {programing} is: {average:.3f}")
print(f"The programing marks:{programingmarks}")

#No. 3
celcius = float(input("Enter temperature in celcius degrees: "))
fahrenheit = (celcius * 9/5) +32
print(f"{celcius}C is equal to {fahrenheit:.2f}F") 


#No. 4
MilesDriven = float(input("Enter the number of miles driven: "))
GallonsUsed = float(input("Enter the gallons of gas used: "))
MLG=miles_driven/gallons_of_gas_used
print




 

