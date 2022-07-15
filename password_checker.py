# Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password 
# strong hai.

password= input("enter password: ")
i=0
while i<len(password):
    if len(password)>=6 and len(password)<=16 :
        if "$" in password:
            if "2" in password or "8" in password:
                if "A" in password or "Z" in password:
                    print("Strong Password")
                    break
    i=i+1
else:
    print("Weak Password")
