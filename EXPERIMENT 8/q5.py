count=0
def prime_or_not(n):
    global count
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            return count
        else:
            continue

if count==2:
    print("prime")

else:
    print("Not prime")

n=int(input("Enter n:"))

prime_or_not(n)
