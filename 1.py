p= int(input())
q= int(input())
n=p*q
f=(p-1)*(q-1)
e=0
b=0
for i in range(2,f):
    if f % i == 1 and b ==0:
        e=i
        b=i
    elif (f % i == 1) and b !=0:
        b=i
p1=int(input())
s=(p1**e)%n
a = (s**b)%n
print(e,b)
print (p,q)
print (s,a)







