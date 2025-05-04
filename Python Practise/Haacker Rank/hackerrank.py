n=int(input())
record=[]

for i in range(n):
    l=[]
    name = input() 
    number = float(input()) 
    l.append(name)  
    l.append(number)
    record.append(l) 

scores = [x[1] for x in record]

unique_scores=sorted(set(scores))
if len(unique_scores)>1:
    second_low_score=unique_scores[1]

second_low_name=[x[0] for x in record if x[1]==second_low_score]
second_low_name.sort()
for name in second_low_name:
    print(name)
