"""
The purpose of the program was to create databases from python dictionaries. 
These nested dictionaries were able to create tables to store information and change the infromation inside based off user implementation.
The user has the option to use of the add, remove, update and print commands craeted from functions.
The program is run using a while loop.

"""
#Table 1: Students
students = {
    "student1": {
        "name": "sarah",
        "course": "physics",        
        "year": "freshman", 
        "grade": 85,
        "id-1":  101 
    },
    "student2" : {
        "name": "emily ",
        "course": "chemistry",        
        "year": "sophmore ",
        "grade": 95,
        "id-1" : 102
    }, 
    "student3": {
        "name": "henry",
        "course": "Math",        
        "year": "senior",
        "grade": 90,
        "id-1": 103 
    } ,
    "student4": {
        "name": "ethan",
        "course": "psychology",        
        "year": "junior",
        "grade": 75,
        "id-1": 104 
    }
          
}
#Table 2: Employees
employees = {
    "employee1": {
        "employeename": "luna",
        "age": 22,
        "job": "teacher",
        "personalty": "introvert",
        "id-2": 201
    },
    "employee2" : {
        "employeename": "lucas",
        "age": 25,
        "job": "researcher",
        "personalty": "extrovert",
        "id-2": 202
    },
    "employee3" : {
        "employeename": "julie",
        "age": 27,
        "job": "designer",
        "personalty": "introvert",
        "id-2": 203
    },
    "employee" : {
        "employeename": "blake",
        "age": 30,
        "job": "lawyer",
        "personalty": "ambivert",
        "id-2": 204
    },
}
#List of Command Words
stop_word = ["Quit", "Q"]
add_word = ["Add", "A"]
remove_word = ["Remove", "R" ]
print_word = ["Print", "P"]
update_word = ["Update", "U"]

#Function that removes a row of data from students table
def remove_student():
    if remove == "101":
        del students["student1"]
    elif remove == "102":
        del students["student2"]
    elif remove == "103":  
        del students["student3"]
    elif remove == "104":  
        del students["student4"]

#Function that removes a row of data from employees table
def remove_employee():
    if remove == "201":
        del employees["employee1"]
    elif remove == "202":
        del employees["employee2"]
    elif remove == "203":  
        del employees["employee3"]
    elif remove == "204":  
        del employees["employee4"]

#Function that adds data to students table
def add_students():
    n = input("enter a name: ")
    c = input("enter course: ")
    y = input("enter academic year: ")
    g = int(input("enter course grade: "))
    i = int(input("enter id number: "))
    new = dict(name = n, course = c, year = y, grade = g, id = i)
    print(new)
    students["student5"] = new
#print(students)

#Function that adds data to employees table
def add_employees():
    e = input('enter employee name: ')
    a = int(input("enter age: "))
    j = input("enter occupation: ")
    p = input("enter personlity type: ")
    i2 = int(input("enter id number: "))
    new2 = dict(employee_name = e, age = a, job = j, personality = p, id = i2)
    print(new2)
    employees["employee5"] = new2  

#Function that updates values of data from students table
def update_students(num):
    if num == "101":
        key = "student1"
    elif num == "102":
        key = "student2"
    elif num == "103":
        key = "student3"
    elif num == "104":
        key = "student4"

    column = input("enter column name: ")
    new_value = input("enter new value: ")

    if column == "name":
        students[key]["name"] = new_value
    if column == "course": 
        students[key]["course"] = new_value
    if column == "year":
        students[key]["year"] = new_value
    if column == "grade":
        students[key]["grade"] = new_value

#Function that updates values of data from employees table
def update_employees(num):
    if num == "201":
        key = "employee1"
    elif num == "202":
        key = "employee2"
    elif num == "203":
        key = "employee3"
    elif num == "204":
        key = "employee4"

    column = input("enter column name: ")
    new_value = input("enter new value: ")

    if column == "employeename":
        employees[key]["employeename"] = new_value
    if column == "age": 
        employees[key]["age"] = new_value
    if column == "job":
        employees[key]["job"] = new_value
    if column == "personality":
        employees[key]["personality"] = new_value

#Function that prints data from students table
def students_print():
    ask = input("do you want the whole table printed or a students record: ")
    if ask == "whole table": 
        print(students)
    elif ask == "student record":
        id = input("enter id")
        if id == "101":
            print(students["student1"])
        elif id == "102":
            print(students["student2"])
        if id == "103":
            print(students["student3"])
        if id == "104":
            print(students["student4"])

#Function that prints data from employees table
def employees_print():
    ask_e = input("do you want the whole table printed or an employee record: ")
    if ask_e == "whole table": 
        print(employees)
    elif ask_e == "employee record":
        id = input("enter id")
        if id == "201":
            print(employees["employee1"])
        elif id == "202":
            print(employees["employee2"])
        if id == "203":
            print(employees["employee3"])
        if id == "204":
            print(employees["employee4"])

#Ask user what commmand they would like to implemnts onto data tables: add, remove, update or print 
user_input = input("Would you like to add, remove, update or print from the data table: ")

#While loop that calls user defined functions based off user input
#Statement that calls on remove functions to remove from tables
while user_input not in stop_word:
    if user_input in remove_word:
        remove_table = input("Which table do you want to remove from: ")
        remove = input("What record ID do you want to remove: ")

        if remove == "101" or "102" or "103" or "104":
            remove_student()
            #print(students)
        elif remove == "201" or "201" or "203" or "204":
            remove_employee()
            #print(employees)
        else:
            print("ID number not valid. Try Again")
#Statement that calls on add functions to add to tables
    elif user_input in add_word:
        add_table = input("Which table do you want to add to: ")
        if add_table == "students":
            add_students()
            #print(students)
        elif add_table == "employees":
            add_employees()
            #print(employees)

#Statement that calls on update functions to update tables data
    elif user_input in update_word:
        update_table = input("Which table do you want to update: ")
        if update_table == "students":
            id_s = input("enter id number: ")
            update_students(id_s)
            #print(students)
        elif update_table == "employees":
            id_e = input("enter id number: ")
            update_employees(id_e)
            #print(employees)

#Statement that calls on print functions to print from tables
    elif user_input in print_word:
        print_table = input("Which table do you want to print: ")
        if print_table == "students":
            students_print()
        elif print_table == "employees":
            employees_print()

    user_input = input("\nWould you like to add, remove, update or print from the data table: ")

