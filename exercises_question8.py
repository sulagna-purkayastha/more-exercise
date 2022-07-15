# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements hone 
# chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone 
# chaiye.

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=list1+list2
i=0
new=[]
while i<len(new_list):
    a=new_list[i]
    if a not in new:
        new.append(a)
    i=i+1
print(new)