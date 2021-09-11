def factorial(n):

    if n==0 or n==1:
       return 1
    else:
        return n*factorial(n-1)
n=input("number : ")
n=int(n)

f=factorial(n)
print(f)       
