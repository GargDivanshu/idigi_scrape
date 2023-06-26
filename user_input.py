from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


batch_values = {
    "2015-2019": "15",
    "2016-2020": "16",
    "2017-2021": "17",
    "2018-2022": "18",
    "2019-2023": "19",
    "2020-2024": "20",
    "2021-2025": "21",
    "2022-2026": "22",
}

college_values = {
    "AIACTR": "AIACTR",
    "AMITY": "AMITY",
    "BMCEM": "BMCEM",
    "BPIT": "BPIT",
    "BVCOE": "BVCOE",
    "BMIET": "BMIET",
    "CBPGEC": "CBPGEC",
    "DITM": "DITM",
    "DITE": "DITE",
    "DTC": "DTC",
    "ADGITM": "ADGITM",
    "GBPGEC": "GBPGEC",
    "GNIT": "GNIT",
    "GTB4CEC": "GTB4CEC",
    "GTBIT": "GTBIT",
    "HMR": "HMR",
    "JIMS": "JIMS",
    "MAIT": "MAIT",
    "MSIT": "MSIT",
    "MSWAMI": "MSWAMI",
    "NPTI": "NPTI",
    "SBIT": "SBIT",
    "TIIPS": "TIIPS",
    "VIPS": "VIPS",
}

branch_values = {
    "CSE": "CSE",
    "CIV": "CIV",
    "ECE": "ECE",
    "EE": "EE",
    "EEE": "EEE",
    "ICE": "ICE",
    "IT": "IT",
    "MAE": "MAE",
    "ME": "ME",
    "MET": "MET",
    "PE": "PE",
    "TE": "TE",
    "CST": "CST",
    "ITE": "ITE",
    "CSECS": "CSECS",
    "AIML": "AIML",
    "IOT": "IOT",
    "AIDS": "AIDS"
}

def get_user_input():
    window = tk.Tk()
    window.title("User Input")
    
    # Create a label and dropdown menu for batch
    batch_label = ttk.Label(window, text="Batch:")
    batch_label.grid(row=0, column=0, padx=5, pady=5)
    batch_var = tk.StringVar()
    batch_dropdown = ttk.Combobox(window, textvariable=batch_var)
    batch_dropdown["values"] = list(batch_values.keys())
    batch_dropdown.grid(row=0, column=1, padx=5, pady=5)
    
    # Create a label and dropdown menu for college
    college_label = ttk.Label(window, text="College:")
    college_label.grid(row=1, column=0, padx=5, pady=5)
    college_var = tk.StringVar()
    college_dropdown = ttk.Combobox(window, textvariable=college_var)
    college_dropdown["values"] = list(college_values.keys())
    college_dropdown.grid(row=1, column=1, padx=5, pady=5)
    
    # Create a label and dropdown menu for branch
    branch_label = ttk.Label(window, text="Branch:")
    branch_label.grid(row=2, column=0, padx=5, pady=5)
    branch_var = tk.StringVar()
    branch_dropdown = ttk.Combobox(window, textvariable=branch_var)
    branch_dropdown["values"] = list(branch_values.keys())
    branch_dropdown.grid(row=2, column=1, padx=5, pady=5)
    
    # Create a label and entry field for enrollment key
    enrollment_key_label = ttk.Label(window, text="Enrollment Key:")
    enrollment_key_label.grid(row=3, column=0, padx=5, pady=5)
    enrollment_key_entry = ttk.Entry(window)
    enrollment_key_entry.grid(row=3, column=1, padx=5, pady=5)
    
    result = []

    def submit():
        batch = batch_values.get(batch_var.get())
        college = college_values.get(college_var.get())
        branch = branch_values.get(branch_var.get())
        enrollment_key = enrollment_key_entry.get()
        
        if not batch or not college or not branch or not enrollment_key:
            messagebox.showwarning("Incomplete Information", "Please fill in all the fields.")
        else:
            result.extend([batch, college, branch, enrollment_key])
            window.destroy()
    
    submit_button = ttk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
    
    window.mainloop()
    
    return result


input_data = get_user_input()

if len(input_data) == 4:
    batch, college, branch, enrollment_key = input_data
    print("Selected Values:")
    print("Batch:", batch)
    print("College:", college)
    print("Branch:", branch)
    print("Enrollment Key:", enrollment_key)
else:
    print("User input is incomplete.")
