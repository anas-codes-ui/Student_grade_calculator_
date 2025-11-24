from datetime import datetime
tracker = {"students": {}}
def calculate_grade(p):
    if p >= 90: return "A+"
    if p >= 80: return "A"
    if p >= 70: return "B"
    if p >= 60: return "C"
    if p >= 50: return "D"
    return "F"
def input_int(prompt, min_value=None):
    while True:
        try:
            v = input(prompt).strip()
            if v == "": 
                print("Enter a value.")
                continue
            n = int(v)
            if min_value is not None and n < min_value:
                print(f"Enter a number >= {min_value}.")
                continue
            return n
        except ValueError:
            print("Invalid number, try again.")
        except KeyboardInterrupt:
            print("\nCancelled.")
            return None
def input_str(prompt):
    try:
        s = input(prompt).strip()
        if s == "":
            print("Input cannot be empty.")
            return input_str(prompt)
        return s
    except KeyboardInterrupt:
        print("\nCancelled.")
        return None
def add_student():
    name = input_str("Enter student name: ")
    if name is None: return
    subjects = input_int("Number of subjects: ", min_value=1)
    if subjects is None: return
    marks = {}
    for i in range(subjects):
        sub = input_str(f"Subject {i+1} name: ")
        if sub is None: return
        while True:
            m_raw = input(f"Marks for {sub}: ").strip()
            try:
                if m_raw == "":
                    print("Enter marks.")
                    continue
                m = float(m_raw)
                if m < 0:
                    print("Marks cannot be negative.")
                    continue
                marks[sub] = m
                break
            except ValueError:
                print("Invalid marks, enter a number (e.g., 78 or 78.5).")
            except KeyboardInterrupt:
                print("\nCancelled.")
                return
    total = sum(marks.values())
    percentage = round(total / subjects, 2)
    grade = calculate_grade(percentage)
    tracker["students"][name] = {"marks": marks, "percentage": percentage, "grade": grade, "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    print(f"Student '{name}' added with percentage {percentage}% and grade {grade}.")
def view_all():
    if not tracker["students"]:
        print("No students yet.")
        return
    for n, d in tracker["students"].items():
        print(f"\n{n}")
        print_student(d)
def print_student(d):
    for s, m in d["marks"].items():
        print(f"{s}: {m}")
    print("Percentage:", d["percentage"])
    print("Grade:", d["grade"])
    print("Added on:", d.get("added_on","-"))
def view_student():
    name = input_str("Enter name: ")
    if name is None: return
    if name not in tracker["students"]:
        print("Student not found.")
        return
    print_student(tracker["students"][name])
def class_summary():
    if not tracker["students"]:
        print("No data.")
        return
    percentages = [d["percentage"] for d in tracker["students"].values()]
    highest = max(percentages)
    lowest = min(percentages)
    average = round(sum(percentages)/len(percentages), 2)
    toppers = [n for n,d in tracker["students"].items() if d["percentage"] == highest]
    print("Class Summary")
    print("Total students:", len(percentages))
    print("Highest percentage:", highest, "by", ", ".join(toppers))
    print("Lowest percentage:", lowest)
    print("Class average:", average)
def delete_student():
    name = input_str("Enter name to delete: ")
    if name is None: return
    if name in tracker["students"]:
        del tracker["students"][name]
        print(f"Deleted {name}.")
    else:
        print("Not found.")
def menu():
    try:
        while True:
            print("\n1. Add Student")
            print("2. View All Students")
            print("3. View Single Student")
            print("4. Class Summary")
            print("5. Delete Student")
            print("6. Exit")
            c = input("Choose: ").strip()
            if c == "1": add_student()
            elif c == "2": view_all()
            elif c == "3": view_student()
            elif c == "4": class_summary()
            elif c == "5": delete_student()
            elif c == "6": break
            else: print("Invalid choice.")
    except KeyboardInterrupt:
        print("\nExiting.")
if __name__ == "__main__":
    menu()
