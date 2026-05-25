# 🧑‍💼 Employee CRUD Application (FastAPI + Streamlit + MySQL)

This is a full-stack CRUD (Create, Read, Update, Delete) project built using:

- ⚡ FastAPI (Backend API)
- 🎨 Streamlit (Frontend UI)
- 🐬 MySQL (Database)
- 🐍 Python (Core language)

---

# 📌 Features

- Add Employee
- View All Employees
- Update Employee Details
- Delete Employee
- Real-time API communication between Streamlit and FastAPI

---

# 🏗️ Project Structure


project/

│

├── main.py # FastAPI backend

├── app.py # Streamlit frontend

└── README.md


---

# ⚙️ Technologies Used

- FastAPI
- Streamlit
- MySQL
- Requests (API calls)
- Pandas

---

# 🚀 Setup Instructions

## 1. Clone the project
```bash
git clone <your-repo-link>
cd project

2. Install dependencies
pip install fastapi uvicorn mysql-connector-python streamlit requests pandas

3. Setup MySQL Database

Create database:

CREATE DATABASE CRUD_Using_API;

Create table:

CREATE TABLE CRUD_API (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100)
);

4. Run FastAPI Backend
uvicorn main:app --reload

Backend runs at:

http://localhost:8000

5. Run Streamlit Frontend
streamlit run app.py

📡 API Endpoints
➕ Add Employee

POST /add_emp
📄 Get All Employees

GET /get_emps
🔍 Get Employee by ID

GET /get_employee_detail/{emp_id}

✏️ Update Employee
PUT /update_employee/{emp_id}

❌ Delete Employee
DELETE /delete_emp/{emp_id}

📸 UI Preview
Streamlit dashboard for CRUD operations
Table view using Pandas DataFrame
Interactive forms for update and add operations

🧠 Learning Outcomes

REST API development using FastAPI
Frontend development using Streamlit
Database integration with MySQL
Full-stack Python project structure


👨‍💻 Author
Jeegari Thirumal