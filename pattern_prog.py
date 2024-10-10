n=int(input("enter the rows:"))
#print("*"*n)
for j in range(n):    #using for loop
   print('*',end="") 
     
print("simple sqare pattern in python--)")
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("INCREASING TRAINGLE PATTERN:---)")
n=int(input("enter the rows:"))
for i in range(n):
   for j in range(i+1):
     print("*",end=" ")
   print() 
   
print("DECREASING TRAINGLE PATTERN:---)")
n=int(input("enter the rows:"))
for i in range(n):
   for j in range(i,n):
     print("*",end=" ")
   print() 
   
print("RIGHT SIDE TRIANGLE:-)")
n=int(input("enter the row:"))
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")    
    print()   
    
print("right side triangle while incresing space first follwed by decreasing star :---)")
n=int(input("enter the row:"))
for i in range (n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")    
    print()