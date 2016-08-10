# This program reads a 3 (decimal) digit positive integer,
#and print the sum of its digits.

number=int(input('Please enter a 3 digit positive integer: '))
n = abs(number)
total = 0
while n>=1:
    total += (n % 10)
    n = n // 10

print ('The sum of its digits is ' , total)
