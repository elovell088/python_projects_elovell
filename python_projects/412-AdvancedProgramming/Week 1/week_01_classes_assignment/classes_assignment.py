#IT 412 - Eric Lovell - Classes Assignment#
from classes.collect import *
from classes.student import *
from classes.instructor import *


#--START PROGRAM--#

#List that will hold all the student ane instructor values
college_records = []
#Flag that allows user to terminate program
program_running = True
while program_running:
    #Instantiate object from Collect class and begin collecting information
    collect_info = Collect()
    name = collect_info.collect_name()
    email = collect_info.collect_email()
    type = collect_info.collect_type()
    id = collect_info.collect_id(type)
    #Conditions to collect information specific to student or instructor and append to college records list
    if type == 'student':
        program = collect_info.collect_program()
        student = Student(name, email, id, type, program)
        college_records.append(student)
    else:
        degree = collect_info.collect_degree()
        institution = collect_info.collect_institution()
        instructor = Instructor(name, email, id, type, degree, institution)
        college_records.append(instructor)
    #Ask user if they want to view all collected information from an indivudal (previous entry) 
    collect_info.queryName(college_records)

    #Ask user if they would like to make another entry - if not, print all entries in college records list
    user_continue = input("Would you like to make another entry? (Y/N): ")
    if user_continue == 'n':
        collect_info.cleanOutput(college_records)
        program_running = False
