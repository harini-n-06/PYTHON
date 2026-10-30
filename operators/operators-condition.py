#odd or even
a=13
if a%2==0:
    print("even")
else:
    print("odd")

#average marks
a=int(input("enter subject 1 marks:"))
b=int(input("enter subject 2 marks:"))
c=int(input("enter subject 3 marks:"))
d=int(input("enter subject 4marks:"))
e=int(input("enter subject 5 marks:"))
average=(a+b+c+d+e)/5
print("{:.3f}".format(average))

#input in single line function
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    