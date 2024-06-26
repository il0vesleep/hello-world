lst=[]
for i in range (2,100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
p= int(input())
q= int(input())
n=p*q
f=(p-1)*(q-1)
m=0
for x in lst:
    if f % x !=0:
        e=x
        print("e",e)
        break
for da in lst:
    if da *e %f==1 and da!=e:
        d=da
        print(d)
        break
p1=int(input())
s=(p1**e)%n
a = (s**d)%n
print (p,q)
print (s,a)
