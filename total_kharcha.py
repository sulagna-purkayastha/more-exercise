# iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul 
# ka ek mahine ka kharcha nikalenge.

Number_of_students =int(input("enter Number of students: "))
Ek_student_ka_kharcha =int(input("enter Ek student ka kharcha: "))
total_kharcha= Number_of_students*Ek_student_ka_kharcha
if total_kharcha<=50000:
    print("Hum budget ke andar hain")
else:
    print("hum budget ke bahar hain")