n = int(input("enter a number: "))
if n== 0:
    print( "it is neither positive nor negative ")
elif n > 0:
    print( "it is a positive integer ")
else:
    print( "it is a negative integer ")

if n % 2== 0:
    print("it is an even number")
else:
    print("it is an odd number")

i = 2
while i < n:
    if(n%i)== 0:
        print("its not a prime number")
        break
    i = i + 1
else:
    print("its a prime number")

a = 2
while a < n:
    if(a**2)== n:
        print("its a perfect square")
        break
    a = a + 1
else:
    print("it is not a perfect square")

b = 2
while b < n:
    if(b**3)== n:
        print("its a perfect cube")
        break
    b = b + 1
else:
    print("it is not a perfect cube")






