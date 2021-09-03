def unique_student_ids(students_english_int=input(),
                       students_english_list=list(map(int, input().split())),
                       students_french_int=input(),
                       students_french_list=list(map(int, input().split()))):
    """
    Args:
        students_english_int: Number of students in the list passed to students_english_list
        students_english_list: A list containing student IDs as integers
        students_french_int: Number of students in the list passed to students_french_list
        students_french_list: A list containing student IDs as integers
    Returns:
        int: The number of unique student from the union of students_english_list and students_french_list
    """
    students_english_set = set(students_english_list)
    students_french_set = set(students_french_list)
    return len(students_english_set.union(students_french_set))


if __name__ == '__main__':
    print(unique_student_ids())
