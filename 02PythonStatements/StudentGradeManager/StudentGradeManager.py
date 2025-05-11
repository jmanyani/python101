# Step 1: Define immutable course info using tuple
course_info = ('Math 101', 'Fall 2025')

# Step 2: Create a list of students with scores
students = [
    {'name': 'Alice', 'scores': [88, 92, 79]},
    {'name': 'Bob', 'scores': [90, 91, 95]},
    {'name': 'Charlie', 'scores': [65, 70, 60]},
    {'name': 'Alice', 'scores': [88, 92, 79]}  # Intentional duplicate to test set
]

# Step 3: Use set to get unique student names
unique_names = set()
for student in students:
    unique_names.add(student['name'])

print("Unique Students:", unique_names)

# Step 4: Write student grades to file
with open('grades_report.txt', 'w+') as file:
    file.write(f"Course: {course_info[0]} | Term: {course_info[1]}\n")
    file.write("Student Grade Report:\n")
    file.write("======================\n")

    for student in students:
        name = student['name']
        avg_score = sum(student['scores']) / len(student['scores'])

        # Use if-elif-else for grading
        if avg_score >= 90:
            grade = 'A'
        elif avg_score >= 80:
            grade = 'B'
        elif avg_score >= 70:
            grade = 'C'
        else:
            grade = 'D'

        file.write(f"{name}: Avg = {avg_score:.2f}, Grade = {grade}\n")

# Step 5: Read the file and print line-by-line
print("\n--- Report from File ---")
for line in open('grades_report.txt'):
    print(line.strip())
