
# Import module
import array

# 1️⃣ Students and Marks

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [78, 45, 62, 90, 55]  # integers

# Compute totals, average, min, max
total_marks = sum(marks)
average_marks = total_marks / len(marks)
min_marks = min(marks)
max_marks = max(marks)


# 2️⃣ Boolean Threshold Check
threshold = 60
status = (average_marks > threshold) and (max_marks > 80)  # compound boolean


# 3️⃣ Seating Plan as List

exam_list = ["Seat1-Alice", "Seat2-Bob", "Seat3-Charlie", "Seat4-David"]
print("Original List:", exam_list)

# Add a new element
exam_list.append("Seat5-Eve")

# Remove a student starting with 'B'
exam_list = [s for s in exam_list if not s.split('-')[1].startswith('B')]

# Sort list
exam_list.sort()
print("Modified & Sorted List:", exam_list)


# 4️⃣ Seating Plan as Array

marks_array = array.array('i', marks[:4])  # fixed-size numeric subset
sum_array = sum(marks_array)
sum_list_subset = sum(marks[:4])
print("\nArray elements:", marks_array)
print("Sum of array:", sum_array)
print("Sum of list subset:", sum_list_subset)
print("Array sum equals list sum?", sum_array == sum_list_subset)

# 5️⃣ Dictionaries for Exam Records


exam_dict_list = [
    {"ID": 1, "Name": "Alice", "Marks": 78},
    {"ID": 2, "Name": "Bob", "Marks": 45},
    {"ID": 3, "Name": "Charlie", "Marks": 62},
    {"ID": 4, "Name": "David", "Marks": 90},
]

# Update record: add 5 marks to Charlie
for record in exam_dict_list:
    if record["Name"] == "Charlie":
        record["Marks"] += 5

# Delete record: remove Bob
exam_dict_list = [record for record in exam_dict_list if record["Name"] != "Bob"]

# Compute total marks from dictionary
total_dict_marks = sum(record["Marks"] for record in exam_dict_list)


# 6️⃣ 2D Seating Plan Array

rows, cols = 2, 3


seating_plan = [[None for _ in range(cols)] for _ in range(rows)]
seat_number = 1
for student in students:
    assigned = False
    for i in range(rows):
        for j in range(cols):
            if seating_plan[i][j] is None:
                seating_plan[i][j] = f"{seat_number}-{student}"
                seat_number += 1
                assigned = True
                break
        if assigned:
            break


# 7️⃣ Formatted String Report

report_title = "=== Exam Sitting Plan Report ==="
summary_totals = f"Total Marks (List): {total_marks}, Min: {min_marks}, Max: {max_marks}"
summary_average = f"Average Marks: {average_marks:.2f}, Status: {'Above Standard' if status else 'Below Standard'}"
summary_dict_total = f"Total Marks (Dictionary): {total_dict_marks}"

# 8️⃣ Display Everything

print("\n" + report_title)
print("\nSeating Plan (Seat-Student):")
print(seating_plan)
print("\n" + summary_totals)
print(summary_average)
print(summary_dict_total)