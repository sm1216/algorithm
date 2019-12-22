#!/usr/bin/python


#####################################
#####################################
#palindrome1
#####################################
####################################

name=input("enter name  ")
palindrome=name[::-1]
if name == palindrome:
   print("its a palindrome",palindrome)
else:
   print("not a palindrome")
