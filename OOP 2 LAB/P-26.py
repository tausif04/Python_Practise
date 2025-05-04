students_scores = {
    'Tausif': 85,
    'Mursalin': 92,
    'Rafi': 78,
    'Shahariar': 95,
    'Ishtaque': 88
}

max_score_student = max(students_scores,key=students_scores.get)

print(f"The student with the highest score is {max_score_student} with a score of {students_scores[max_score_student]}.")
