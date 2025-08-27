#  Student Management System (Flask + MySQL)

A simple **2-tier web application** built using **Flask (Python)** and **MySQL**.  
This project demonstrates CRUD operations: Add, View, Edit, and Delete student records.

-----------------------------------------------------------------------------------------

## Features:
- Add new students with name, email, and course
- View all students in a table
- Edit student details
- Delete student records
- HTML templates rendered with Flask (Jinja2)
- MySQL as backend database

-----------------------------------------------------------------------------------

##  Installation & Setup:

### 1. Clone Repository:

git clone https://github.com/iam-vinodkumar/python-flask-app.git


cd python-flask-app

2. Setup Virtual Environment:
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

3. Install Dependencies:
pip install -r requirements.txt

4. Configure MySQL:

Install MySQL Server & Workbench.

Create database and table:

CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(50) NOT NULL
);

3.Update app.py with your MySQL root username and password:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'studentdb'

5. Run Flask App:
python app.py


Visit: 👉 http://127.0.0.1:5000

Architecture Diagram:

This is a 2-tier architecture:

+-------------------+        +-------------------+
|   Web Browser     | <----> | Flask App (app.py)|
| (User Interface)  |  HTTP  |  Python Backend   |
+-------------------+        +-------------------+
                                     |
                                     | SQL Queries
                                     v
                             +-------------------+
                             |  MySQL Database   |
                             |  studentdb        |
+-------------------+        +-------------------+

**Dependencies:**

Flask

Flask-MySQLdb (or mysqlclient)

Install via:

pip install flask flask-mysqldb

**License:**

This project is licensed under the MIT License.
Feel free to fork and enhance

Contributions:

Pull requests are welcome. Please fork the repo and submit a PR with improvements.
