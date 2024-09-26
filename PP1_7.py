'''
    Lesson: Booleans
    Author: Karcihan Satheskishan
    Date Creatd: Sept 25, 2024
    Date Last Modified: Sept 25, 2024
'''
def q1():
  bool1 = True
  print(bool1)

def q2():
  num=int(input("Input an integer: "))
  bool1=(num > 5)
  print(bool1)

def q3():
  letter=input("Input the letter a: ")
  bool1=("a" == letter)
  print(bool1)

def q4():
  word=input("Input a word earlier in the dictionary than google: ")
  bool1=("google" > word)
  print(bool1)

def q5():
  num1=int(input("Input an integer: "))
  num2=int(input("Input another integer: "))
  bool1=(num1*num2 > 40)
  print(f"Your numbers multiplied together are greater than 40: {bool1}")

#Do edit the code below
#Comment the lines below when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''