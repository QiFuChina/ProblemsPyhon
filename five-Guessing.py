import random
# import random function
i = random.randint(0,101)
# set a random number as a secert number 

number =input("Input a number:")
# get a exact number from users
list=list+number
# create a list to store every numbers

#print(i)
#print(type(i))
#identify i and number


if number > str(i):
    print("This number is bigger than secert number")
elif number < str(i):
    print("This number is smaller than secert number")
else:
    print("This number is equal to secert number")

# those statments compare two values as same type and return different information