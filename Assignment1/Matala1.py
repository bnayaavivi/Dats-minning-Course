# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:37:31 2023

@author: USER
"""
# Q1
def my_func(x1,x2,x3):
    if x1+x2+x3==0:
        return "Not a number – denominator equals zero"
    if type(x1) is int or type(x2) is int or type(x3) is int:
        return "Error: parameters should be float"
    if type(x1) is not float or type(x2) is not float or type(x3) is not float:
        return None
    return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)

  
# Q2
def revword(string):
    string=string.lower()
    return string[::-1]

def countword():
    file=open("text.txt")
    listword=[]
    listgoodword=[]
    diction={}
    row=0
    for line in file:
        if row==0:
            row=1
            word=line.rstrip()
            continue
        line=line.rstrip().split()
        for wrd in line:
            listword.append(wrd)
    for word1 in listword:
        diction[revword(word1)]=diction.get(revword(word1), 0) + 1
    diction[word]=diction[word]+1
    return diction[word]    
print(countword())        
                

        
        