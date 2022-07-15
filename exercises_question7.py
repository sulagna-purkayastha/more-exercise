# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne jisme inn 
# dono lists ke woh item hone chaiye ho dono list mein aa rahe hain.

list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new=list1+list2
i=0
list=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            list.append(list1[i])
        j=j+1
    i=i+1
print(list)     