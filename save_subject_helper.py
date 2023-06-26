import pandas as pd
import pymysql
from config import schoolId


def save_subject_data(subject):
    # Establish a database connection
    connection = pymysql.connect(
        host='divanshu',
        user='divanshu',
        password='divanshu',
        database='idigizen'
    )
    
    try:
        # Create a cursor object
        cursor = connection.cursor()
        
        # Check if the subject already exists
        query = "SELECT * FROM subject WHERE name = %s AND schoolId = %s"
        cursor.execute(query, (subject, schoolId))
        existing_subject = cursor.fetchone()
        
        if existing_subject:
            print("Subject already exists in the backend.")
        else:
            # Subject does not exist, insert the subject data
            insert_query = "INSERT INTO subject (name, schoolId) VALUES (%s, %s)"
            cursor.execute(insert_query, (subject, schoolId))
            connection.commit()
            print("Subject data saved successfully!")
        
    except Exception as e:
        print("Error:", e)
        
        # Rollback the transaction if an error occurs
        connection.rollback()
    
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()




def get_subject_id_from_database(subject):
    # Connect to the database
    connection = pymysql.connect(
        host='divanshu',
        user='divanshu',
        password='divanshu',
        database='idigizen'
    )

    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query to retrieve the subject ID
        query = f"SELECT id FROM subject WHERE name = '{subject}'"
        cursor.execute(query)

        # Fetch the subject ID
        subject_id = cursor.fetchone()[0]

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return subject_id
    except Exception as e:
        print("Error:", str(e))
        # Handle the error as per your requirement
        return None



def add_exam_type_to_database(type, subject_id, semester, rollup, subject, total_marks):
    # Connect to the database
    connection = pymysql.connect(
        host='divanshu',
        user='divanshu',
        password='divanshu',
        database='idigizen'
    )

    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Insert the exam type into the "examtype" table
        query = "INSERT INTO examtype (type, subjectId, semester, rollup, type, description, totalMarks) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (type, int(subject_id), semester, rollup, subject, subject, int(total_marks))  # Convert total_marks to int
        cursor.execute(query, values)

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Exception as e:
        # Handle the error as per your requirement
        print("Error:", str(e))

