# Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek saath 
# multiply karke nikalta hai.


number= int(input("enter number: "))
i=1
factorial=1
while i<=number:
    factorial= factorial*i
    i=i+1
print(factorial)