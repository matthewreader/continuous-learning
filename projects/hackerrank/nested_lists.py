# Given the names and grades for each student in a class of students, store them
# in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])

    scores_sorted = sorted(list(set(score for name, score in grades)))
    second_highest_score = scores_sorted[1]

    names_output = []
    for name, score in grades:
        if score == second_highest_score:
            names_output.append(name)

    names_output.sort()
    for name in names_output:
        print(name)
