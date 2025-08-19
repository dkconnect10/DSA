'''
================================================
Assignment-19: Simple problems on recursion
=================================================

Write a recursive function to calculate sum of first N natural numbers.

Write a recursive function to calculate sum of first N odd natural numbers.

Write a recursive function to calculate sum of first N even natural numbers.

Write a recursive function to calculate factorial of a number.

Write a recursive function to calculate sum of squares of first N natural numbers.

'''


def naturalnumber(n):
    try:
        if n==1:
            return 1
        return n+naturalnumber(n-1)                
    except Exception as e:
        print(str(e))    
        
def sumofOddnumber(n):
    try:
        if n==1:
            return 1
        return 2*n-1+sumofOddnumber(n-1)
    except Exception as e:
        return str(e)        

def sumofEvennumber(n):
    try:
        if n==1:
            return 2
        return 2*n+sumofEvennumber(n-1)
    except Exception as e:
        return str(e) 

def factN(n):
    try:
        if n==0:
            return 1
        return n*factN(n-1)                
    except Exception as e:
        print(str(e)) 
        
def sumofSquare(n):
    try:
        if n==1:
            return 1
        return n*n +sumofSquare(n-1)                
    except Exception as e:
        print(str(e))        
                
obj=naturalnumber(3)   
print(obj)   
obj=sumofOddnumber(3)
print(obj)  
obj=sumofEvennumber(3)
print(obj) 
obj=factN(5)
print(obj)
obj=sumofSquare(5)
print(obj)