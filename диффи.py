g=int(input("Введите g "))
p=int(input("Введите p "))
a=int(input("Введите a "))
b=int(input("Введите b "))
A=(g**a)%p
B=(g**b)%p
ka=(A**b)%p
kb=(B**a)%p
k=(g**(a*b))%p
print("Ключ А ", ka,)
print("Ключ Б ", kb)
print("Общий ключ ", k)
