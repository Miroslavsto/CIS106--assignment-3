def calculate_exam_points():
    last_name = input("Enter your last name: ")
    midterm_score = float(input("Enter your midterm exam score: "))
    final_exam_score = float(input("Enter your final exam score: "))

    total_exam_points = (0.40 * midterm_score) + (0.60 * final_exam_score)

    print(f"Student: {last_name}")
    print(f"Total Exam Points: {total_exam_points:.2f}")

calculate_exam_points()
