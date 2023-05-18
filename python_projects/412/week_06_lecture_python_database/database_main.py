#IT 412 - Eric Lovell - Working with python and database servers lecture

from classes.database_access import DB_Connect

#Connect to database
my_db = DB_Connect('root', '', 'python_projects')

#INSERT Statement Example **COMMENT OUT AFTER INITIAL RUN**
my_db.executeQuery("INSERT INTO course_info (course_discipline, course_number, course_title) VALUES ('IT', '650', 'Software Principles')")
my_db.conn.commit()

#UPDATE Statement Example *COMMENT OUT BEFORE RUNNING THE INSERT STATEMENT EXAMPLE**
my_db.executeQuery("UPDATE course_info SET letter_grade='A-', course_gpa='3.7' WHERE course_id='2'")
my_db.conn.commit()

#SELECT Statement Example **OUTPUTS DATA IN TUPLE
query_result = my_db.executeSelectQuery("SELECT * FROM course_info")
print(query_result)

#Working with the query result example
for record in query_result:
    print(record[0])
    print(record[1])
    print(record[2])
    print(record[3])
    print(record[4])
    print(record[5])

#Returning data as a list of dictionary items **RUN AFTER ADDING THE CURSORCLASS ATTRIBUTE IN database_access.py**
query_result = my_db.executeSelectQuery("SELECT * FROM course_info")
print(query_result)

#Modified for loop to output dictionary results **WILL ONLY WORK AFTER ADDING CURSORCLASS ATTRIBUTE IN database_access.py**
for record in query_result:
    print(record["course_id"])
    print(record["course_discipline"])
    print(record["course_number"])
    print(record["course_title"])
    print(record["letter_grade"])
    print(record["course_gpa"])
