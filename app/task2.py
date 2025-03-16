from typing import List, Dict, Set
from itertools import chain, combinations
import numpy as np

class Teacher:
    def __init__(self, name: str, age: int, email: str, subjects: List[str]):
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.last_name = name_parts[1] if len(name_parts) > 1 else ""
        self.age = age
        self.email = email
        self.can_teach_subjects = subjects  # List[str]
    
    def __str__(self):
        subjects_str = ", ".join(self.can_teach_subjects) if self.can_teach_subjects else "No subjects"
        return f"Teacher {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}, Can teach: {subjects_str}"

def create_schedule(subjects: Set, teachers:List[Teacher]):
    successed:List[Dict[str, Teacher]] = []

    all_subsets = chain.from_iterable(combinations(teachers, r) for r in range(len(teachers) + 1))

    for teachers_subset in all_subsets:
        subs = dict.fromkeys(subjects, None)
        for subject_name in subjects:
            if all(teacher for teacher in subs.values()):
                break 
            for teacher in teachers_subset:
                for teacher_subject in teacher.can_teach_subjects:
                    if not subs[subject_name] and subject_name == teacher_subject:
                        subs[subject_name] = teacher

        if all(teacher for teacher in subs.values()):
            successed.append(subs)

    teachers_min_val = np.inf
    choosen = None
    for single in successed:
        # fing for number of unique teachers is minimum
        unique_teachers_numb = len(set(single.values()))
        if(unique_teachers_numb < teachers_min_val):
            teachers_min_val = unique_teachers_numb
            choosen = single
    return choosen

def load_teachers():
    return [
        Teacher(
            "Олександр Іваненко", 45, "o.ivanenko@example.com", ["Математика", "Фізика"]
        ),
        Teacher("Марія Петренко", 38, "m.petrenko@example.com", ["Хімія"]),
        Teacher(
            "Сергій Коваленко",
            50,
            "s.kovalenko@example.com",
            ["Інформатика", "Математика"],
        ),
        Teacher(
            "Наталія Шевченко", 29, "n.shevchenko@example.com", ["Біологія", "Хімія"]
        ),
        Teacher(
            "Дмитро Бондаренко",
            35,
            "d.bondarenko@example.com",
            ["Фізика", "Інформатика"],
        ),
        Teacher("Олена Гриценко", 42, "o.grytsenko@example.com", ["Біологія"]),
    ]


if __name__ == "__main__":
    # Set of subjects
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Create a list of teachers
    teachers = load_teachers()

    # Call the schedule creation function
    schedule = create_schedule(subjects, teachers)

    def get_assigned_subjects(schedule: Dict[str, Teacher], teacher):
        return [subj for subj, tch in schedule.items() if teacher == tch ]

    # Output the schedule
    if schedule:
        print("Class schedule:")
        for teacher in set(schedule.values()):
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} years, email: {teacher.email}"
            )
            print(f" Teaches subjects: {', '.join(get_assigned_subjects(schedule, teacher))}\n")
    else:
        print("Unable to cover all subjects with available teachers.")
