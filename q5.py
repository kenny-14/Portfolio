# Q5 Student Grade Analyser

names = [
    "Amara Nangolo",
    "Petrus Hamutenya",
    "Selma Nakamhela",
    "Johannes Shikongo",
    "Ndapewa Iita",
    "Maria Amutenya",
    "David Nghifike",
    "Anna Shipanga"
]

scores = [
    [78, 65, 82],
    [45, 52, 38],
    [91, 88, 94],
    [60, 71, 55],
    [33, 41, 29],
    [85, 79, 88],
    [55, 60, 48],
    [72, 68, 75]
]

def get_average(scores):
    return round(sum(scores) / len(scores), 1)

# 3. Function to assign grade
def get_grade(avg):
    if avg >= 80:
        return 'A'
    elif avg >= 65:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

def print_report(names, scores):
    total_avg = 0
    pass_count = 0

    print("STUDENT REPORT")
    print("--------------------------")

    for i in range(len(names)):
        first_name = names[i].split()[0]
        avg = get_average(scores[i])
        grade = get_grade(avg)

        print(first_name, "Avg:", avg, "Grade:", grade)

        total_avg += avg

        if grade != 'F':
            pass_count += 1

    class_avg = total_avg / len(names)

    print("--------------------------")
    print("Class Average:", round(class_avg, 1))
    print("Students Passed:", pass_count)

print_report(names, scores)