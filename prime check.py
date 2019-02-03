n = int(input("give integer for prime check:"))

i = 2
while i < n:
    if(n%i)== 0:
        print("its not a prime number")
        break
    i = i+1
else:
    print("its a prime number")