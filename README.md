# Employee Management RESTful API Service

A modular, scalable backend RESTful API built with **Python**, **FastAPI**, and **SQLAlchemy** to manage departments and employee records with relational persistence, structured schema validation, and interactive documentation.

---

## Key Features

- **CRUD Operations:** Full lifecycle management for Department and Employee resources.
- **Relational Persistence:** One-to-Many relational schema mapping (`Department` $\rightarrow$ `Employees`) via SQLAlchemy ORM with foreign key constraints.
- **Strict Payload Validation:** Enforced request body sanitization and field constraints using **Pydantic schemas** to eliminate malformed payloads.
- **Security & Integrity:** Parameterized queries via ORM routines to mitigate SQL injection vulnerabilities.
- **Structured Error Handling:** Return of standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, and `422 Unprocessable Entity`).
- **Automated Documentation:** Auto-generated interactive Swagger UI and OpenAPI specifications.

---

## Tech Stack

- **Backend Framework:** FastAPI
- **Language:** Python 3.10+
- **Database & ORM:** SQLite / MySQL, SQLAlchemy
- **Data Validation:** Pydantic
- **Testing & Exploration:** Swagger UI, Postman

---

## Project Structure

```text
├── database.py       # Database engine, session maker, and Base setup
├── models.py         # SQLAlchemy ORM relational models
├── schemas.py        # Pydantic schemas for request and response validation
├── main.py           # Application entry point & RESTful route controllers
├── requirements.txt  # Project dependencies
└── README.md
---

## API Endpoints Overview

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **POST** | `/departments/` | Create a new department | `201 Created` |
| **GET** | `/departments/` | Retrieve all departments | `200 OK` |
| **POST** | `/employees/` | Add a new employee linked to a department | `201 Created` |
| **GET** | `/employees/` | Retrieve paginated employees with department details | `200 OK` |
| **GET** | `/employees/{id}` | Retrieve specific employee by ID | `200 OK` |
| **DELETE** | `/employees/{id}` | Remove employee record | `204 No Content` |

---

## Getting Started Locally

### 1. Clone the repository
```bash
git clone [https://github.com/shivamsingh-0509/employee-management-api.git](https://github.com/shivamsingh-0509/employee-management-api.git)
cd employee-management-api
### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
```bash
pip install -r requirements.txt
### 4. Run the application
```bash
uvicorn main:app --reload --port 8080
Access the interactive API documentation at:
- **Swagger UI:** `http://127.0.0.1:8080/docs`
