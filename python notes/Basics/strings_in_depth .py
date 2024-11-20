#1. strings are array like structured
#arrays in python are lists
#example 
#marks = [90,60,70]
#in arrays the first indez is at zero
#index (Accessing characters[])
name = "Nazifa"
print(name[0])
print(name[5])

#2. looping through strings
# Here we use keywords
# example
for character in name:
    print(character)
address = "Kamokya"
for character in address:
    print(character)
    
#3. Slicing in strings[:]
#This is the accessing of the range of characters in a string
#example
name = "Nazifa"
print(name[1:6])#azifa
print(name[1:5])#azif
print(name[0:3])#Naz
print(name[ :4])#Nazi
message = "Hello"        
print(message[0:3])

#negative index slice
#example message="hello"
print(message[-1])#o
print(message[-1:-5])#space
print(message[-1:-4])#space
print(message[-5:-3])#he
print(message[-4: ])
print(message[4:])

#4. f string{}
# Here we embedde variables in carry brackets {} while printing and it automatically casts the variables
name = "Nazifa"
age ="20"  
weight = 55.845
print("my name is" + name " my age is "+ str(age))
print(f"my name is {name} and I'm {20} years old and I weigh {weight : 1f}")
totalCost =3000000
print(f"A new shoe is at {totalCost:,}") 

#5. string methods 
#1.lengh #len()
#it is all about the number of characters
#upper case andd lower case 
#Here we use (.and ())
name="Nazifa\nNawamwena\n"
print(len())
print(name.upper())
address = "FromKamokya"
print(len(address))

# 6. Escape sequences(\)
#Here we back slash
name ="nazifa\nNawamwena\n"  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      )
