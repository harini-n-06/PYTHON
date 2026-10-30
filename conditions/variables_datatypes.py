#variables and datatypes
print("Hello World")

x=("HARINI")
print(x)

y=19
z=("thanjavur")
print(x,y,z,sep="_")   

a=10
b=20
print(a,b,sep="-")

#swap two numbers
print(a,b)
swap=a
a=b
b=swap
print(a,b)

c=int(input())
d=float(input())
e=input()
f=bool(input())
print(c,d,e,f)
#type
age=10
print(type(age))
#add two input
g=23
h=24
print(g+h)


i=float(25)
print(type(i))


j="2425"
j=int(j)
print(j+5)

# ARITHMETIC_OPERATOR
k=5
l=10
print(k+l)
print(k-l)
print(k*l)
print(k/l)

print(k//l)

print(k%l)


m=int(input())
if m>9 and m<100:
  print("last digit of m is",m%10)

n=int(input())
print(n**2)
print(n**3)


length=int(input())
breath=int(input())
area=length*breath
perimeter=2*(length+breath)
print(area)
print(perimeter)


o=int(input())
p=int(input())
if o==p:
    print("o and p are equal")
else:
    print("o and p are not equal")


q=int(input())
r=int(input())
if q>r:
    print(q)
else:
    print(r)


s=int(input())
if s<=10 and s>=50:
    print("s is in the range of 10 to 50")
else:
    print("s is not in the range of 10 to 50")


t=int(input())
u=int(input())
v=int(input())
if t>u and t>v:
    print(t)
elif u>v:
    print(u)
else:
    print(v)


w=int(input())
x=int(input())
print(w==x)
print(w!=x)
print(w<x)


y=int(input())
print(y>10 and y<100)
print(y%3==0 and y%5==0)
print(y%3==0 or y%5==0)
print(y!=0)

z=int(input())
z+=5
print(z)
z-=7
print(z)
z*=3
print(z)
z//=3
print(z)
z%=5
print(z)
z**=3
print(z)
z/=4
print(z)


    








