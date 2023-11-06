from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"


def main():
    load_project(FILENAME)


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
