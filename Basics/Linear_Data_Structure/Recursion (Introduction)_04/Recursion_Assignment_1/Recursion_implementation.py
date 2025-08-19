
#=================================================================================
#📘 Assignment-18: Simple problems on recursion
#=================================================================================

'''
1. Write a recursive function to print first N natural numbers.

2. Write a recursive function to print first N natural numbers in reverse order.

3. Write a recursive function to print first N odd natural numbers.

4. Write a recursive function to print first N even natural numbers.

5. Write a recursive function to print first N odd natural numbers in reverse order.

6. Write a recursive function to print first N even natural numbers in reverse order.
'''



def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")

def printNreverse(n):
    if n>0:
        print(n,end=" ")
        printNreverse(n-1)

def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(n*2-1,end=" ")

def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(n*2,end=" ")
        
def printNOddReverse(n):
    if n>0:
        print(n*2-1,end=" ")
        printNOddReverse(n-1)

def printNEvenReverse(n):
    if n>0:
        print(n*2,end=" ")
        printNEvenReverse(n-1)
                

                
printN(10) 
print("") 
printNreverse(10)      
print("")
printNOdd(10)
print("")
printNEven(10)
print("")
printNOddReverse(10)
print("")
printNEvenReverse(10)
print("")


