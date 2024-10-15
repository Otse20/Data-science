#Write a Python program that prints the sum of all odd numbers between 1 and 50 using a for loop.

sum_odd = 0
for i in range (1,51):
  if i % 2 !=0:
    sum_odd +=i

  print(sum_odd)
