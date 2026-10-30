#loops
#for
for i in range(1,11):
    print(i)

n=int(input())
for i in range(n-1,0,-1):
    print(i)


n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)
        

n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        print(i)
        
n=int(input())
sum1=0
for i in range(1,n+1):
    sum1=sum1+i
print(sum1)


n=int(input())
for i in range(1,11):
    print("5 x",i,"=",5*i)

a=int(input())
cube   =0
for i in range(1,a+1):
    cube=i**3
    print(cube)
    
a=int(input())
sum1=0
for i in range(1,a+1):
    if i%5==0 and i%3==0:
        sum1=sum1+i
print(sum1)

a=int(input())
sum1=0
for i in range(1,a+1):
    if i%2==0:
        sum1=sum1+i
print(sum1)

a=int(input())
c=1
for i in range(1,a+1):
    c*=i
print(c)

a=int(input())
for i in range(1,a+1):
    if a%i==0:
        print(i)

a=int(input())
sum1=0
for i in range(1,a):
    if a%i==0:
     sum1=sum1+i
if sum1==a:
  print("Perfect Number")

a=int(input())
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
if count==2:
  print("prime")
else:
   print("not prime")

#while
n=int(input())
a=0
b=1
while n>0:
    print(a,end=" ")

    a,b=b,a+b
    n-=1
    
n=int(input())
decimal=0
i=0
while n>0:
    r=n%10
    decimal+=r*(2**i)
    n//=10
    i+=1
print(decimal)


a=int(input())
sum1=0


n=int(input())
sum1=0
while n>0:
    r=n%10
    if(n%2==0):
        sum1+=r
        n//10
print(sum1)

n=int(input())
product=1
while n>0:
  r=n%10
  product=product*r
  n//=10
print(product)
  
n=int(input())
rev=0
while n>0:
  r=n%10
  rev=rev*10+r
  n//=10
print(rev)


n=int(input())
while n>=10:
    n//=10
print(n)

n=int(input())
c=0
while n==0:
  r=n%10
  c+=r
  n//=10
print(c)

n=int(input())
d=int(input())
c=0
while n>0:
    r=n%10
    if r==d:
        c=c+1
        n//=10
print(c)