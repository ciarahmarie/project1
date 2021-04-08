#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CCC 151 CS2
#Patayon, Ciarah Marie A.
"""
Fields :- ['idnum', 'name', 'year', 'gender', 'course']
1. Add a new student
2. Display list of students
3. Search a Student
4. Edit Student Data
5. Delete a Student
6. End
"""

import csv
student_datas = ['idnum', 'name', 'year', 'gender', 'course']
student_database = 'students.csv'


def options():
    print("Student Information System")
    print("Please input number of desired option: ")
    print("1. Add a new student")
    print("2. Display list of sudents")
    print("3. Search a Student")
    print("4. Edit Student Data")
    print("5. Delete a Student")
    print("6. End")


def add():
    print("Add Student Data")
    global student_datas
    global student_database

    student_data = []
    for field in student_datas:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Saved")
    input("Press any key to continue.....")
    return


def display():
    global student_datas
    global student_database

    print("--- List of Students ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_datas:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue........")


def search():
    global student_datas
    global student_database

    print("--- Search a Student ---")
    idnum = input("Enter id no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if idnum == row[0]:
                    print("----- Student Found -----")
                    print("Id#: ", row[0])
                    print("Name: ", row[1])
                    print("Year Level: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        else:
            print("Sorry the Id No. is invalid ")
    input("Press any key to continue.....")


def edit():
    global student_datas
    global student_database

    print("--- Edit Student Data---")
    idnum = input("Enter ID no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idnum == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_datas:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Sorry the ID No. you entered is invalid ")

    input("Press any key to continue.....")


def delete():
    global student_datas
    global student_database

    print("--- Delete a Student ---")
    idnum = input("Enter ID no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idnum != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID no. ", idnum, "deleted successfully")
    else:
        print("ID No. not found in our database")

    input("Press any key to continue......")

while True:
    options()

    choice = input("Please enter an integer for your desired choice: ")
    if choice == '1':
        add()
    elif choice == '2':
        display()
    elif choice == '3':
        search()
    elif choice == '4':
        edit()
    elif choice == '5':
        delete()
    else:
        break

print("closed")


# In[ ]:




