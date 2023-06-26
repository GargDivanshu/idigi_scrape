from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from tqdm import tqdm
from user_input import get_user_input
from user_data import get_user_data
import pymysql

# def create_db_connection():
#     host = 'divanshu'
#     user = 'divanshu'
#     password = 'divanshu'
#     database = 'idigizen'

#     connection = pymysql.connect(host=host, user=user, password=password, database=database)
#     print("Database connection established.")
#     return connection



def scrape_table_data(batch, college, branch):
    url = f"https://www.ipuranklist.com/ranklist/btech?batch={batch}&sem=0&college={college}&shift=0&branch={branch}"
    print(f"Scraping data from {url}...")
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    
    # Navigate to the URL
    driver.get(url)
    
    # Wait for the table to load (you may need to adjust the wait time)
    time.sleep(10)
    
    # Find all rows in the table
    rows = driver.find_elements(By.CSS_SELECTOR, "tr.ng-star-inserted")
    
    progress_bar = tqdm(total=len(rows), desc="Scraping")
    
    # Iterate over the rows and extract the desired data
    data = []
    for row in rows:
        enrollment_no = row.find_element(By.CSS_SELECTOR, "td.limit-char").text
        name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        marks = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        total_marks = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) span.outof").text
        gpa = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
        rank = row.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
        
        # Append the data to the list
        data.append([enrollment_no, name, marks, total_marks, gpa, rank])
      
        progress_bar.update(1)
    
    # Close the WebDriver
    driver.quit()
    
    progress_bar.close()
    
    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(data, columns=["Enrollment No.", "Name", "Marks", "Total Marks", "GPA", "Rank"])
    
    # Save the DataFrame as a CSV file
    csv_filename = f"table_data_{batch}_Overall_{college}_both_{branch}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Table data saved to {csv_filename}.")

# batch, college, branch, enrollment_key = "", "", "", ""
input_data = get_user_input()
# print(batch, college, branch, enrollment_key)
if input_data != ():
    batch, college, branch, enrollment_key = input_data
    # Call scrape_table_data with the user input
    print(batch, college, branch, enrollment_key)
    print("hello")
    # scrape_table_data(batch, college, branch)
    get_user_data(batch, college, branch, enrollment_key)


