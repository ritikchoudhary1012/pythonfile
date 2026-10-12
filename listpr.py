employees = [
    {"id": 101, "name": "Rohit Sharma", "salary": 55000, "department": "IT", "role": "Software Developer"},
    {"id": 102, "name": "Priya Verma", "salary": 62000, "department": "HR", "role": "HR Manager"},
    {"id": 103, "name": "Aman Patel", "salary": 48000, "department": "Finance", "role": "Accountant"},
    {"id": 104, "name": "Neha Singh", "salary": 70000, "department": "IT", "role": "Data Analyst"},
    {"id": 105, "name": "Vikas Gupta", "salary": 58000, "department": "Marketing", "role": "Marketing Executive"},
    {"id": 106, "name": "Sneha Jain", "salary": 75000, "department": "IT", "role": "Team Lead"},
    {"id": 107, "name": "Arjun Mehta", "salary": 52000, "department": "Sales", "role": "Sales Executive"},
    {"id": 108, "name": "Kavya Sharma", "salary": 65000, "department": "Finance", "role": "Financial Analyst"},
    {"id": 109, "name": "Rahul Yadav", "salary": 45000, "department": "Support", "role": "Support Executive"},
    {"id": 110, "name": "Anjali Patel", "salary": 80000, "department": "IT", "role": "Project Manager"}
]


for user in employees:
    if user['department'].lower() ==  "it":
        if user["salary"] >= 50000 :   
            increment = (user["salary"] * 5) / 100
            user["salary"] = increment + user["salary"]
        else:
            increment = (user["salary"] * 10) / 100
            user["salary"] = increment + user["salary"]

print(employees)
