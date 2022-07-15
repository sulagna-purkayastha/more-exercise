# Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain. 
# Dhang se divide hone ka matlab ki remainder 0 aata hai. Jaise 42 ek Harshad number hai kyunki 
# 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai

def my_func(n):
    i=0
    sum=0
    while i<len(n):
        a=n[i]
        sum=sum+int(a)
        i=i+1
    if int(n)%sum==0:
        print("True,Harshad no")
    else:
        print("False, not a Harshad no")
n=input("enter any no: ")
my_func(n)