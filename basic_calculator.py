#A python code for a basic calculator

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
  
while True:
  print("A: Addition")
  print("S: Substraction")
  print("M: Multiplication")
  print("D: Division")
  print("E: Exit")
  
  print(" ")
  
  choice = input("Please enter your choice: ")
  
  print(" ")
  
  if choice == "a" or choice == "A":
      print("You have choosen Addition")
      print(" ")
      a = int(input("Please enter the first number: "))
      b = int(input("Please enter the second number: "))
      add(a,b)
  
  elif choice == "s" or choice == "S":
      print("You have chooosen Substraction")
      print(" ")
      a = int(input("Please enter your the first number: "))
      b = int(input("Please enter the second number: "))
      sub(a,b)
  
  elif choice == "m" or choice == "M":
      print("You have chooosen Multiplication")
      print(" ")
      a = int(input("Please enter your the first number: "))
      b = int(input("Please enter the second number: "))
      mul(a,b)
  
  elif choice == "d" or choice == "D":
      print("You have chooosen Division")
      print(" ")
      a = int(input("Please enter your the first number: "))
      b = int(input("Please enter the second number: "))
      div(a,b)
  
  elif choice == "e" or choice == "E":
      print("You have chooosen Exit")
      quit()
