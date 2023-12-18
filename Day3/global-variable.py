num1 = 10  # Define first number as a global variable
num2 = 5  # Define second number as a global variable

def add():
  """
  Function to add num1 and num2, storing the result in a global variable called 'result'
  """
  global result
  result = num1 + num2
  return result

def subtract():
  """
  Function to subtract num2 from num1, storing the result in a global variable called 'result'
  """
  global result
  result = num1 - num2
  return result

# Add the numbers
add()
print("Addition:", result)  # Print the addition result

# Subtract the numbers
subtract()
print("Subtraction:", result)  # Print the subtraction result