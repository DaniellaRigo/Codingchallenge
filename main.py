count = int(input ("How many numbers would you like to summerize?"))
sum = 0
for i in range (count):
  number = int(input (f"Enter number {i+1}"))
  sum = sum + number
print (f"\n The sum of the numbers is: {sum}")


count = int(input ("How many numbers would you like to summerize?"))
sum = 0
for i in range (count):
  sum += int(input (f"Enter number {i+1}: "))
  print (f"The sum is {sum}")