from os import path
from time import strptime

team_size_to_type = {
    2: "duos",
    4: "quatuors"
}

root_directory = path.dirname(path.realpath(__file__))
assignment_type_to_grading_file = {
    "code": f"{root_directory}/samples/grading_file.txt",
    "report": f"{root_directory}/samples/grading_file_tp7.txt"
}


def get_sample_grading_file():
    assignment_type = input("Is it a 'code' assignment or a 'report'? ").strip()
    return assignment_type_to_grading_file[assignment_type]


def get_assignment_deadline():
    while True:
        deadline = input("What is the assignment deadline (yyyy-mm-dd hh:mm)? ")
        try:
            strptime(deadline, "%Y-%m-%d %H:%M")
            return deadline
        except:
            print("Incorrect datetime format.")


def get_assignment_subdirectories():
    subdirectories = input("What are the subdirectories to correct separated by space (ex: tp/tp6/pb1 tp/tp6/pb2)? ")
    return subdirectories.strip().split(" ")


def get_assignment_long_name():
    return input("What is the assignment long name (ex: Code final)? ")


def get_assignment_short_name():
    return input("What is the assignment short name (ex: tp6)? ")


def get_grading_directory(ensure_exists: bool = True):
    while True:
        directory = input("What is the grading directory? ")
        if ensure_exists:
            if path.isdir(directory):
                return directory
            else:
                print("The grading directory specified does not exist.")
        else:
            return directory


def get_group_number():
    return str(int(input("What is your group (ex: 1)? ")))


def get_team_type():
    team_size = int(input("Are you correcting teams of two (2) or four (4) members? "))
    return team_size_to_type[team_size]
