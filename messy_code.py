
#Function to add two numbers
def addnumb(a,b):
  try: #Implement Error handling
    return int(a + b)
  except ValueError:
    print("Please Input Valid numbers")

  #Function to excecute the program
def main():
  firstNumber=input(("enter first number: "))
  secondNumber=input(("enter second number: "))
  result=addnumb(firstNumber, secondNumber)
  print(f"the sum is : {result}")

print("This is a simple adder program")
main()