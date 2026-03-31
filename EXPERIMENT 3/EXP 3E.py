#w.a.p to input mark of 5 subjects and then find total , average and percentage each subject 50 , percentage >= 90 and <=100 grade O , >=80 and <=90 grade E , >=70 and <=80 grade A , >=60 and <=70 grade B , >=50 and <= 60 grade C,>=40 and <=50 grade D , >=30 and <=40 grade F.
# Program to input marks of 5 subjects and calculate total, average, percentage, and grade
# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} (out of 50): "))
    marks.append(mark)  
# Calculate total, average, and percentage
total_marks = sum(marks)
average_marks = total_marks / 5
percentage = (total_marks / 250) * 100
# Determine grade based on percentage
if 90 <= percentage <= 100:
    grade = 'O'
elif 80 <= percentage < 90:
    grade = 'E'
elif 70 <= percentage < 80:
    grade = 'A'
elif 60 <= percentage < 70:
    grade = 'B'
elif 50 <= percentage < 60:
    grade = 'C'
elif 40 <= percentage < 50:
    grade = 'D'
elif 30 <= percentage < 40:
    grade = 'F'
else:
    grade = 'Fail'
# Display the results
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage)
print("Grade:", grade)