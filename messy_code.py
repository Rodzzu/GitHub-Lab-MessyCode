# this program add numbers and print the result but its really messy

def addNum(a, b): # function for handdling two-digit addition
  return a + b

def main():
  while True:
    
    try: # if user input the correct data type, print the answer, and escape the loop
      
      print("This is a simple adder program")

      numA = input("Enter first number: ")
      numB = input("Enter second number: ")

      sum = addNum(int(numA), int(numB))

      print("The sum is: ", sum) # Displays the sum
      break

    except ValueError: # otherwise, display an error message and prompt the user for input again
      print("Invalid input. Please enter a WHOLE NUMBER.\n")

main() # call the function at end