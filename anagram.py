"""
@author: chaithu
"""
a=input("Enter string :")
b=input("Enter string to char :")

a=a.lower()
b=b.lower()

if(sorted(a)==sorted(b)):
    print("entered string is Anagram")
else:
    print("Not an Anagram")