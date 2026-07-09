# import pyttsx3

# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say(" I will speak this text nikhil bishnoi vinit vinitvinitvinitvinitvinitvinit sarika sarika")
# engine.runAndWait()


# from turtle import *

# setposition(-60, 0)
# speed(0)
# bgcolor('black')

# colors = ['orange', 'white']
# pensize(2)

# for i in range(150):
#     color(colors[i % 2])
#     rt(i)
#     circle(90, i)
    
#     up()
#     fd(i + 50)
#     down()
    
#     rt(90)
#     fd(98)
#     fd(i - 65)

# hideturtle()
# done()


# import os
# directory_path = '/'
# contents = os.listdir(directory_path)
# for item in contents:
#     print(item)
   

# a = int(input("enter the number"))
# b = int(input("enter the number"))
# print("total no " , a + b)

# a = int(input("enter the number"))
# b = int(input("enter the number"))
# print(a % b)

 
# i = input("enter a word")
# print(type(i))


# i= int(input("enter a number 1:"))
# j = int(int(input("enter a number 2: ")))
# print(i> j)
# print(i+j/2)
# print(i*i)


# i = "nikhil"
# j = i[-3:-1]
# print(j)

# print(len("herry"))
# text = "nikhil"
# print(text.startswith("ni"))
 

# print("rusesv sosov srer s \"boy\" ")

# a = input("enter a name:")
# print(f"good afternoon {a}")

# letter = ''' MY NAME IS <|name|>.my birthday |<date|> '''
# print(letter.replace("<|name|>","nikhil").replace("<|date|>" , "19 september"))


# name = "nikhil is a good boy and  "
# print(name.find("  "))


# name = "nikhil is a good boy  and  "
# print(name.replace("  " , "   "))

#-------------------list------------------


# list_first = ["apple", "ram",  7, True]
# print(list_first[3])
# list_first[0] ="sham"
# print(list_first)
# print(list_first.pop(2))
# print(list_first)
# list_first.insert(2, "bishnoi")
# print(list_first)
# list_first.remove()
# print(list_first)


# nums= [1,2,3,4]
# nums.append(5)
# print(nums)
# nums.insert(5,6)
# print(nums)
# nums.remove(5)
# print(nums)

# a = (1,2,4)
# print(type(a))
# print(sum(a))
# print(a[::-1])



# s = {}
# print(type(s))



fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Positive indexing
print(f"First: {fruits[0]}")
print(f"Third: {fruits[2]}")

# Negative indexing
print(f"Last: {fruits[-1]}")
print(f"Second last: {fruits[-2]}")

# Slicing [start:end:step]
print(f"First 3: {fruits[:3]}")
print(f"From index 2: {fruits[2:]}")
print(f"Every 2nd: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")
print(f"Middle items: {fruits[1:4]}")