# program to print the normal words

print("hello, this is code with harry");
print("this is rozy, ur love");

# program to print  twinkle twinkle  little start 


print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')




'''This is multiline strings'''

# this is singleline strings

# I love koding

# the library in python which can talk  

import pyttsx3
engine = pyttsx3.init()
engine.say (""" A dream-chaser from Nepal with a passion for tech 
Learning AI, coding, and business """)
engine.runAndWait()

import os

# specify the directory you want to list 

directory_path = '/'

# list all the directories in the specified path

contents = os.listdir(directory_path)

# print each file and directory name 

for item in contents:
 
    print(item)

#Use of variable in python, variable is the container which stores the value 

a = 1

b = 7

name = "harry"

print (a+b)

print(name)

a = 1 #this is a integer

b = 2.44 #this is a floating point number 

c = "Yudeen" #this is a variable 

d = False # this is a boolean variable 

e = None #this is a none variable 


