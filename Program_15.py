#Program to  display fibonacci sries .
num=int(input("Enter a number : "))
n1=0
n2=1
count=0
print(n1)
print(n2)
while (count<num) :
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    count+=1
