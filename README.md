# Employee Management RESTful API Service

A modular, scalable backend RESTful API built with **Python**, **FastAPI**, and **SQLAlchemy** to manage departments and employee records with relational persistence, structured schema validation, and interactive documentation.

## Key Features

- **CRUD Operations:** Full lifecycle management for Department and Employee resources.
- **Relational Persistence:** One-to-Many relational schema mapping (`Department` -> `Employees`) via SQLAlchemy ORM with foreign key constraints.
- **Strict Payload Validation:** Enforced request body sanitization and field constraints using **Pydantic schemas** to eliminate malformed payloads.
- **Security & Integrity:** Parameterized queries via ORM routines to mitigate SQL injection vulnerabilities.
- **Structured Error Handling:** Return of standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, and `422 Unprocessable Entity`).
- **Automated Documentation:** Auto-generated interactive Swagger UI and OpenAPI specifications.

## Tech Stack

- **Backend Framework:** FastAPI
- **Language:** Python 3.10+
- **Database & ORM:** SQLite / MySQL, SQLAlchemy
- **Data Validation:** Pydantic
- **Testing & Exploration:** Swagger UI / Interactive OpenAPI Docs

## Project Structure

```text
employee-management-api/
├── database.py       # Database engine, session maker, and Base setup
├── models.py         # SQLAlchemy ORM models
├── schemas.py        # Request and response validation
├── main.py           # Application entry point and API routes
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## API Endpoints Overview

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| POST | `/departments/` | Create a department | 201 Created |
| GET | `/departments/` | Retrieve all departments | 200 OK |
| POST | `/employees/` | Add an employee linked to a department | 201 Created |
| GET | `/employees/` | Retrieve paginated employees with department details | 200 OK |
| GET | `/employees/{id}` | Retrieve an employee by ID | 200 OK |
| DELETE | `/employees/{id}` | Delete an employee by ID | 204 No Content |

## Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/shivamsingh-0509/employee-management-api.git
cd employee-management-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn main:app --reload
```

### 5. Open the API documentation

Visit http://127.0.0.1:8000/docs in your browser.
