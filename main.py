from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

# Create database tables automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

# --- Department Endpoints ---
@app.post("/departments/", response_model=schemas.DepartmentResponse, status_code=status.HTTP_201_CREATED)
def create_department(dept: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_dept = db.query(models.Department).filter(models.Department.name == dept.name).first()
    if db_dept:
        raise HTTPException(status_code=400, detail="Department already exists")
    new_dept = models.Department(name=dept.name)
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

@app.get("/departments/", response_model=List[schemas.DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(models.Department).all()


# --- Employee Endpoints ---
@app.post("/employees/", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    # Check if email is already registered
    if db.query(models.Employee).filter(models.Employee.email == emp.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Check if department exists
    if not db.query(models.Department).filter(models.Department.id == emp.department_id).first():
        raise HTTPException(status_code=404, detail="Department not found")

    new_emp = models.Employee(**emp.model_dump())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@app.get("/employees/", response_model=List[schemas.EmployeeResponse])
def get_employees(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(models.Employee).offset(skip).limit(limit).all()

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@app.delete("/employees/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return None