from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """This function is main for project management program"""
    projects = load_project(FILENAME)
    is_running = True
    while is_running:
        print(MENU)
        choice = input(">>> ").lower()
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
            filter_projects(date, projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            projects = update_project(projects)
        else:
            print("Thank you for using custom-built project management software.")
            is_running = False


def filter_projects(date, projects):
    """This function filter project by the date"""
    after_date = datetime.strptime(date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > after_date:
            print(f"{project}")


def update_project(projects):
    """This functions modifies selected project line"""
    for i, project in enumerate(projects):
        print(f"{i}  {project}")
    project_choice = int(input("Project Choice: "))
    selected_project = projects[project_choice]
    print(selected_project)
    if project_choice < len(projects):
        projects = projects[project_choice]
        new_completion = input("New Percentage: ")
        if new_completion:
            projects.completion = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            projects.priority = int(new_priority)
    return projects


def add_project(projects):
    """This function adds new projects"""
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate:"))
    completion = int(input("Percentage complete: "))
    projects.append((name, start_date, priority, cost_estimate, completion))


def display_projects(projects):
    """This function displays project"""
    print("Incomplete projects")
    for project in projects:
        if project.completion < 100:
            print(f"{project}")
    print("Completed Projects")
    for project in projects:
        if project.completion == 100:
            print(f"{project}")


def save_projects(filename, projects):
    """This function writes project to file"""
    with open(filename, 'w') as out_file:
        for project in projects:
            out_file.write(
                f"{project.name} \t{project.start_date}\t {project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def load_project(filename):
    """This function loads project"""
    projects = []
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            line = line.strip()
            parts = line.split("\t")
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


if __name__ == "__main__":
    main()
