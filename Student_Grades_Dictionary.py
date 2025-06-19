#collect the names and scores for 5 students
names_and_scores = input("Enter the names and scores of 5 students, separated by a hyphen: ")
names_and_scores = names_and_scores.split(', ')

student_dict = {}

for student in names_and_scores:
    name, score = student.split(" - ")
    student_dict[name] = int(score)

#Find the highest score    
def highest_scorer():
    highest_value = 0
    top_student = ""
    for key in student_dict:
        if student_dict[key] > highest_value:
            highest_value = student_dict[key]
            top_student = key
            
    return f"Highest scorer: {top_student} - {highest_value}"
        
#Calculate the average score        
def average_score():
    return f"Average score: {sum(student_dict.values()) / len(student_dict)}"
    
#print the students by scores
def student_list():
    print("\n----Students----")
    for student in student_dict:
        print(f"{student} -> {student_dict[student]}")
    return

#sort the students
def sort_students():
    return sorted(student_dict.items(), key=lambda x: x[1])
    
print(sort_students())