# Python Basics
print("Udbhav Ojha")

#data types
number=66;
deci_num=5.66
charNum='a'
stringNum="Hey Buddy"
isTrue=True
subjectList=["Maths","English","Science","Social Science","Hindi","Sanskrit"]

print(number," is",type(number))
print(deci_num," is",type(deci_num))
print(charNum," is",type(charNum))
print(stringNum," is",type(stringNum))
print(isTrue," is",type(isTrue))
print(subjectList," is",type(subjectList))

# input
name=input("enter name")
age=int(input("enter age"))

print("Name:",name,"\nage:",age)

maths = int(input("Enter Marks in maths: "))
eng = int(input("Enter Marks in english: "))
comp = int(input("Enter Marks in computer science: "))
phy = int(input("Enter Marks in physics: "))
chem = int(input("Enter Marks in chemistry: "))


total = maths + eng + comp + phy + chem
avg = total / 5

# Display the results
print("Maths:", maths, "\nEnglish:", eng, "\nComputer Science:", comp, "\nPhysics:", phy, "\nChemistry:", chem)
print("-------------")
print("Total:", total, "\nAverage:", avg)


# range
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))

# loop
num=int(input("enter num for table:"))
for x in range(1,11):
    print( num,"x",x,":",x*num)

# Strings
firstName="Udbhav"
lastName="Ojha"
email='udbhavsbg@gmail.com'

details="""I am student of
Chandigarh University, pursuing MCA"""

print(firstName, lastName, email, details)

name="Udbhav Ojha"

for i in range(len(name)):
    print(name[i],end="");

# functions in string
password=input("enter password:")

if(password.isalpha()):
    print("Valid Password")
else:
    print("Invalid Password")

# lstrip() and rstring()
str= "   bcde   "

print(str.lstrip())
print(str.rstrip())
print(len(str))

# list

my_list=[1,4,2,5,6,9,10]
my_secondList=["Udbhav Ojha","22MCA20419",5,4,7.65]

print(my_list,"\n",my_secondList)

my_list = [1, 4, 2, 5, 6, 9, 10]
my_secondList = ["Udbhav Ojha", "22MCA20419", 5, 4, 7.65]

# Convert input to integer
item = int(input("Enter item to be deleted: "))

# Check if item is in the list before attempting to remove
if item in my_list:
    my_list.remove(item)
    print(f"{item} removed from the list.")
else:
    print(f"{item} not found in the list.")

print(my_list)


# sum of odd and even up to input numbers
number= int(input("Enter range:"))
evenSum=0;
oddSum=0;
for i in range(1,(number+1)):
    if(i%2 == 0):
        evenSum+=i;
    else:
        oddSum+=i;
print("Sum of even: {} and Sum of odd: {}".format(evenSum, oddSum))

listInput = []
length = int(input("Enter the length of the list: "))

for i in range(length):
    user_input = int(input(f"Enter element {i + 1}: "))
    listInput.append(user_input)

print("The list you entered is:", listInput)


for i in range(1, 10):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1))

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1))

for i in range(4, 0, -1):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1))


