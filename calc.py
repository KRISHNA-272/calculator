#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(n1,n2):
  sum=n1+n2
  return sum
def subtract(n1,n2):
  minus=n1-n2
  return minus
def multiply(n1,n2):
  mult=n1*n2
  return mult
def divide(n1,n2):
  div=n1/n2
  return div
def expo(n1,n2):
  exp=n1**n2
  return exp
print("1.Add 2.Subtract 3.Multiplication 4.Division 5.Exponent")
print("Select your option: ")
n=int(input("Enter your choice: "))
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n==1:
  print("Sum is ",add(n1,n2))
elif n==2:
  print("Subtraction is ",subtract(n1,n2))
elif n==3:
  print("Multiplication is ",multiply(n1,n2))
elif n==4 :
  print("Division is ",divide(n1,n2))
elif n==5 :
  print("Exponent is :",expo(n1,n2))
else:
  print("Wrong choice :")


# In[ ]:




