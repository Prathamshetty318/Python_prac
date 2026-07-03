name = "Pratham"
age = 22
learning_python = True
#print ("My name is", name, "and I am", age, "years old.", "I am learning Python:", learning_python)

#print (type(name))
#print (type(age))
#print (type(learning_python))

#print(f"My name is {name} my age is {age}")

fav_song = "Is there someone else"
fav_ProgLang = ".net"
Sal_goal ="un ginat aandha paisa"

#print(f"My favourite song is {fav_song}, my favourite programming language is {fav_ProgLang} and my salary goal is {Sal_goal}")

a= 20
b= 6
#print("The sum of a and b is", a+b)
#print("The difference of a and b is", a-b)
#print("The product of a and b is", a*b)
#print("The division of a and b is", a/b)
#print("The floor division of a and b is", a//b)
#print("The modulus of a and b is", a%b)
#print("The exponent of a and b is", a**b)

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#fav_Prog_lang = input("Enter your favourite programming language: ")

#print(f"Hello {name}, you are {age} years old.")
#print (age + 5)


#print("Hello",name)
#print(f"you are {age} years old")
#print(f"your favourite programming language is {fav_Prog_lang}")
#print(f"next year you will be {age +1} year old")

age =22
salary = 100000

"""print (age == 22)
print (age != 22)
print (age > 22)
print (age < 22)
print (age >= 22)
print (age <= 22)

print (age > 18 and salary > 10000)
print  (age > 18 and salary > 110000)
print  (age > 18 or salary > 110000)
print (not(age>18))"""

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

if age < 0:
    print("Invalid age.")
elif age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

