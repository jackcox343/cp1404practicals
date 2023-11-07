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
            display_projects(projects)
        elif choice == "f":
            date = input("Show projects that start after date (dd/mm/yy): ")
            start_date = datetime.strptime(date, "%d/%m/%y").date()
            filter_projects(projects, start_date)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            pass
        else:
            print("Invalid input")


def add_project(projects):
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(date, "%d/%m/%y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate:"))
    completion = int(input("Percentage complete: "))
    projects.append((Project(name, start_date, priority, cost_estimate, completion)))


def filter_projects(projects, start_date):
    filtered_dates = [project for project in projects if start_date > project.end_date]
    print(filtered_dates)


def display_projects(projects):
    print("Incomplete projects")
    incomplete_project = [project for project in projects if project.completion < 100]
    print(incomplete_project)
    print("Completed Projects")
    completed_project = [project for project in projects if project.completion == 100]
    print(completed_project)


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
