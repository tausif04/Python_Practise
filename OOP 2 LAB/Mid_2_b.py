def find_highest_lowest_scores(student_data):
    highest_score=float('-inf')
    lowest_score=float('inf')
    highest_student=None
    lowest_student=None

    for student,data in student_data.items():
        for i in data['scores']:
            if i>highest_score:
                highest_score = i
                highest_student=student
            if i<lowest_score:
                lowest_score=i
                lowest_student=student


    return highest_score,highest_student,lowest_score,lowest_student

def average_score_each_student(student_data):
    for student,data in student_data.items():
        total_score=sum(data['scores'])
        avg=total_score/3
        print(f"Total number List :{data['scores']}")
        print(f"Average score of {student} is {avg:.2f}")
        
def unique_subject_list(student_data):
    unq_sub=set()
    for student,data in student_data.items():
        unq_sub.update(data['favourites'])
    return unq_sub
           
def common_subjects_list(student_data):
    common_sub=None
    for student,data in student_data.items():
        if common_sub is None:
            common_sub=data['favourites']
        else:
            common_sub=common_sub.intersection(data['favourites'])
    return common_sub

        
student_data={
    "Alice":{"scores":[85,86,78],"favourites":{"Math","Physics","Art of Living"}},
    "Bob":{"scores":[75,87,70],"favourites":{"Math","English","OOP"}},
    "Charlie":{"scores":[55,88,91],"favourites":{"OOP","Chemistry","Math"}},
    "David":{"scores":[78,42,85],"favourites":{"Physics","Chemistry","Math"}},
    "Eve":{"scores":[90,45,87],"favourites":{"Art of Living","Math","English"}}
}

highest_score,highest_student,lowest_score,lowest_student=find_highest_lowest_scores(student_data)
print(f"The student {highest_student} get the highest mark with mark-{highest_score}")
print(f"The student {lowest_student} get the lowest mark with mark-{lowest_score}")
average_score_each_student(student_data)

sub=unique_subject_list(student_data)
print(f"The set of unique subject is :{sub}")

common=common_subjects_list(student_data)
print(f"The set of common subject is {common}")