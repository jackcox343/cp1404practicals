from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Enter filename to load: ")
            load_project(filename)
        elif choice == "s":
            filename = input("Enter filename to save: ")

            save_projects(projects, filename)
        elif choice == "d":
            pass
        elif choice == "f":
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        else:
            print("Invalid input")


def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        for project in projects:
            out_file.write(f"{project}\n")


def load_project(filename):
    projects = []
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(",")
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d%m#y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


main()
