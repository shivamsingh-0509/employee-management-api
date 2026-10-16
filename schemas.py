from pydantic import BaseModel, EmailStr
from typing import Optional, List

# --- Department Schemas ---
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


# --- Employee Schemas ---
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    salary: float
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None

class EmployeeResponse(EmployeeBase):
    id: int
    department: Optional[DepartmentResponse] = None

    class Config:
        from_attributes = True