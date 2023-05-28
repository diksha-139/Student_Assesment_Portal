from enum import Enum
import os
from constants import FILE_ASSESSMENTS,FILE_STUDENTS

class Choice(Enum):
    ADD = "A"
    INSERT = "I"
    SEARCH = "S"
    QUIT = "Q"



msg="""
========================================================
Welcome to the Student Assesment Management System
<Add> Enter A to add the details of a student
<Insert> Enter I to insert assignment marks of a student
<Search> Enter S to search assessment marks of a student
<Q> Enter Q to quit 
========================================================
"""

def display(text=""):
    print(text)
    
def display_details(data,text="The details of the student are as follows: "):
    print("Thank you !")
    print(text)
    for k,v in data.items():
        print(f"{k} : {v}")

def take_input(display_text=""):
    """
    Takes user input along with an option to display a text
    """
    user_input = input(display_text)
    return user_input

def write_file(file_name,data):
    mode ="w"
    if os.path.isfile(file_name):
        mode ="a"
    
    with open(file_name,mode) as f:
        f.write(",".join(data)+"\n")

    print(f"The record has been succefully added to {file_name} file.")

def read_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name,"r") as f:
            data = f.read()
        return data.strip().split("\n")

def ask_yes_no(text):
    user_choice = input(text)
    if user_choice == "Y":
        return True
    elif user_choice == "N":
        return False
    else:
        ask_yes_no("Please Enter the correct choice(Y/N) .")


def add():
    while True:    
        student_id = take_input("Please Enter the Student Id: ")
        student_name = take_input("Please Enter the Student Name: ")
        course = take_input("Please Enter the Course: ")

        data ={
            "student_id" : student_id,
            "student_name": student_name,
            "course": course
        }

        display_details(data)

        write_file(FILE_STUDENTS,data.values())
        
        user_input = ask_yes_no("Do you want to Enter Details for other Student? (Y/N) = ")

        if not user_input:
            break


def search():
    while True:

        student_id = take_input("Please Enter the Student Id whose assesment marks you want to search: ")
        student_records = read_file(FILE_STUDENTS)
        assessment_records = read_file(FILE_ASSESSMENTS)

        students_dict={}

        assessments_dict={}

        

        for record in student_records:
            students_dict[record.split(",")[0]] = record.split(",")


        if student_id in students_dict:
            data={
                "student_id":student_id,
                "Student_name":students_dict[student_id][1],
                "Course":students_dict[student_id][2]
            }
            display_details(data,"The Student has been found...")

            print("{:<20} {:<25} {:<12}".format("Subject Code","Assessment Number","Marks"))

            for assessment_record in assessment_records:

                if student_id in assessments_dict:
                    assessments_dict[student_id].append(assessment_record.split(","))
                else:
                    assessments_dict[assessment_record.split(",")[0]] = [assessment_record.split(",")]



            assessment_data = assessments_dict.get(student_id,[])
                
            for data in assessment_data:
                print("{:<20}{:<25}{:<12}".format(*data[1:]))

        else:
            print("Record Not Found")

        user_input = ask_yes_no("Do you want to search Assesment marks for another student : (Y/N)= ")

        if not user_input:
            break
            

def insert():
    while True:    
        student_id = take_input("Please Enter the Student Id: ")
        subject_code = take_input("Please Enter the Subject Code : ")
        assesment_number = take_input("Please Enter the Assesment Number: ")
        marks = take_input("Please Enter the Marks: ")

        data ={
            "student_id" : student_id,
            "subject_code": subject_code,
            "assesment_number": assesment_number,
            "marks": marks
        }

        display_details(data)
        write_file(FILE_ASSESSMENTS,data.values())
        user_input = ask_yes_no("Do you want to Enter marks for another Assesments? (Y/N) = ")

        if not user_input:
            break


def main():
    display(msg)
    user_input = take_input()
    try:
        if Choice(user_input) == Choice.ADD:
            add()
            return True
        elif Choice(user_input) == Choice.INSERT:
            insert()
            return True
        elif Choice(user_input) == Choice.SEARCH:
            search()
            return True
        elif Choice(user_input) == Choice.QUIT:
            print("You get out of the portal... ")
            return False
    except ValueError as v:
        print(v)
        print("Invalid Choice ,Please choose from available options...")
        return True
    except Exception as e:
        print(e)
        return False
        




if __name__=="__main__":
    while True:
        if not main():
            break
    

    

