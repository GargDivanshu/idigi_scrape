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
