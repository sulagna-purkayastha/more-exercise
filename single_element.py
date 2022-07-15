#  Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye



string_list = ["Empathy", "Empathy","hope", "Kindness", "Kindness", "Compassion","hope" ,"Humble", "Humble"]
i=0
count=0
new_list=[]
while i<len(string_list):
    a=string_list[i]
    j=1
    len=1-int(len(string_list))
    while j<len:
        if string_list[i]==string_list[j]:
            count=count+1
            if count>1:
                string_list.remove(string_list[j])
            j=j+1
    i=i+1
print(string_list)
        