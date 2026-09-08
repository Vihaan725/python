'''Build a grade book that stores student names and scores in a dictionary. Your program calculates the class 
average, finds the top and bottom scorer, and lets the user look up any student's grade.
What you need to use
1.  dictionary      →  store at least 5 student name-score pairs
2.  for loop        →  to calculate the class average
3.  max() min()     →  to find the top and bottom scorer
4.  .get()          →  to look up a student by name
5.  input()         →  to let the user search for a student'''

student_scores = {"Eli": 92, "Max": 85, "James": 95, "Mason": 88, "George": 93}

for student in student_scores:
    total_scores = student_scores[student]

average = total_scores/5
print(average)
top_scorer = max(student_scores, key=student_scores.get)
print(top_scorer)
bottom_scorer = min(student_scores, key=student_scores.get)
print(bottom_scorer)
search_student = input("Enter student's name: ")
grade_of_student = student_scores.get(search_student)
print(grade_of_student)
