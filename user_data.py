from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_user_data(batch, college, branch, enrollment_key):
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()

    course = "btech"
    data = []
    mainData = []
    
    # Scrape data for each semester
    for sem in range(0, 9):
        url = f"https://www.ipuranklist.com/ranklist/{course}?batch={batch}&sem={sem}&college={college}&shift=0&branch={branch}"
        print(f"Scraping data from {url}...")
        driver.get(url)

        # Wait for the table to load (you may need to adjust the wait time)
        time.sleep(2)

        # Find the row containing the user data
        row = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, f"//tr[contains(.,'{enrollment_key}')]"))
        )
        
        # Find the toggle element
        time.sleep(2)
        
        # Extract user data for the current semester
        enrollment_no = row.find_element(By.CSS_SELECTOR, "td.limit-char").text
        name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text

        try:
            marks = WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(3)"))
            ).text
        except NoSuchElementException:
            marks = "N/A"  # If marks not found, assign a default value
        
        total_marks = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) span.outof").text
        gpa = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
        rank = row.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text

        # Print user data for the current semester
        print("User Data:")
        print("Enrollment No.:", enrollment_no)
        print("Name:", name)
        print("Marks:", marks)
        print("Total Marks:", total_marks)
        print("GPA:", gpa)
        print("Rank:", rank)
        mainData.append({"enrollment_key": enrollment_key, "Name": name, "sem":sem, "marks": marks, "total marks": total_marks, "gpa": gpa, "rank": rank})
        
        # Click on the table data to open the modal
        row.click()

        # Wait for the modal to appear (you may need to adjust the wait time)
        time.sleep(2)

        # Get the modal dialog
        modal = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
        
        try:
            parent_div = modal.find_element(By.XPATH, "//div[contains(span/text(), 'Show paper IDs')]")
            
            toggle = parent_div.find_element(By.CSS_SELECTOR, "label.switch")
            print("Parent div found")
            print("Toggle found")
            toggle.click()
            # Check if the "Paper ID" element is present
        except NoSuchElementException:
            print("Toggle element not found")
            sem+=1
            continue

        # Find the table rows inside the modal for the current semester
        tbody = modal.find_element(By.CSS_SELECTOR, "tbody.tbody")
        table_rows = tbody.find_elements(By.CSS_SELECTOR, "tr.ng-star-inserted")
        
        # Extract the data for the current semester
        # table_rows = WebDriverWait(driver, 7).until(
        #               EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.ng-star-inserted"))
        #                )
        
#         table_rows = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr"))
# )

# Extract the data for the current semester
        for row in table_rows:
            paper_id = WebDriverWait(row, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td:nth-child(1)"))
    ).text
            subject = WebDriverWait(row, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td:nth-child(2)"))
    ).text
            marks = WebDriverWait(row, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td:nth-child(3)"))
    ).text

    # Append the data to the list
            data.append({"enrollment_key": enrollment_key, "Name": name, "sem": sem, "Paper Id" : paper_id, "subject": subject, "marks": marks})
            print("Paper ID:", paper_id)
            print("Subject:", subject)
            print("Marks:", marks)
        # Close the modal dialog for the current semester
            # Close the modal dialog for the current semester
    driver.find_elements(By.CSS_SELECTOR, ".close")[0].click()

# Wait for the modal to close
    WebDriverWait(driver, 7).until_not(
               EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
)


    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(mainData)

    # Save the DataFrame to a CSV file
    df.to_csv("user_data.csv", index=False)
    df2.to_csv("user_data2.csv", index=False)

    # Close the WebDriver
    driver.quit()