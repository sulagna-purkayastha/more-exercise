# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. Ek aisa code likho jisse 
# aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye

string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
count=0
new_list=[]
while i<len(string_list):
    a=string_list[i]
    if a not in new_list:
        new_list.append(a)
    i=i+1
print(new_list)