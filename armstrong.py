num = int(input("Enter a number: "))
n=len(str(num))
# Input: 407
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# Output: 407 is an Armstrong number
   

   
# An Armstrong number (also known as a narcissistic number, plenary number, or plus perfect number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits in the number itself.

# For example, let's consider the number 153:

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153