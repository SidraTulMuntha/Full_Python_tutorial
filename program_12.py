n=int(input("Enter a number : "))
for i in range(2,10):
    if  n%i==0:
        prime=True
        break
if prime:    
        print("it is prime number")
        
else:
        print("it is not a prime number")    
