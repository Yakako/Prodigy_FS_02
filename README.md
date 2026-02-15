# Task02_FS - Employee Management System

## Overview

**Employee Management System** is a web application built with **Flask** that allows administrators to perform CRUD (Create, Read, Update, Delete) operations on employee records. The system includes secure user authentication to protect sensitive employee data.

The application uses a clean, modern design with **gradient backgrounds**, responsive forms, and a structured dashboard.

---

## Features

- **Secure Login and Authentication**  
  Admin users can log in and access protected routes. Unauthorized access is blocked.

- **Employee CRUD Operations**  
  - **Create:** Add new employees with details like Name, Email, Department, Position, and Salary.  
  - **Read:** View all employee records in a styled table.  
  - **Update:** Edit existing employee information.  
  - **Delete:** Remove employee records safely.

- **Flash Messages**  
  Provides feedback for actions like login errors, record added, updated, or deleted.

- **Modern UI**  
  Uses a gradient background, styled forms, buttons, and tables for a user-friendly interface.

---

## Tech Stack

- **Backend:** Python 3.9, Flask  
- **Database:** SQLite (via SQLAlchemy)  
- **Authentication:** Flask-Login  
- **Password Hashing:** Flask-Bcrypt  
- **Frontend:** HTML, CSS (custom styling)  

---

## Folder Structure


Task02_FS/
├── app.py # Main Flask application
├── models.py # Database models (User, Employee)
├── templates/ # HTML templates
│ ├── login.html
│ ├── dashboard.html
│ ├── employees.html
│ ├── add_employee.html
│ └── edit_employee.html
├── static/ # CSS and other static assets
│ └── style.css
├── requirements.txt # Python dependencies
└── README.md


---

# Author
- Name: Pruonh Kimliya
- Email: kimliyapruonh@gmail.com
