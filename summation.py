# Write a program that finds 
# the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
# Your function only needs to return the result,
# what is shown between parentheses in the example below i
# s how you reach that result and it's not part of it, see the sample tests.

def summation(num):
  sum = 0
  i = 0
  while i <= num:
    sum = sum + i 
    i +=1
  return sum 