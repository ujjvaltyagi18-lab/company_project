from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from .model import Address, Company, Employee, Salary, Tax, Course, Seat, Student, Registration, Discount, Penality, Fees, Payment, Certification, Placement, Package, Batch, Attendance, Assignment, Result, Inquiry
from .database import get_session


app=FastAPI()


@app.post("/Address/")
def create_Address(address: Address, session: Session=Depends(get_session)):
  session.add(address)
  session.commit()
  session.refresh(address)
  return address

@app.get("/Address/")
def get_Address(session: Session=Depends(get_session)):
  address= session.exec(select(Address)).all()
  return address

@app.get("/Address/{address_id}")
def get_Address_by_id(address_id: int, session: Session=Depends(get_session)):
  address= session.get(Address, address_id)
  return address

@app.delete("/Address/{address_id}", status_code=204)
def delete_Address_by_id(address_id: int, session: Session=Depends(get_session)):
  address = session.get(Address, address_id)
  if not address:
    raise HTTPException(status_code=404, detail="Address not found")
  session.delete(address)
  session.commit()
  return {"detail": f"Address {address_id} deleted"}

@app.delete("/Address", status_code=204)
def delete_Address(session: Session=Depends(get_session)):
  address = session.exec(select(Address)).all()
  for address in address:
    session.delete(address)
    session.commit()
  return {"detail": "All address deleted"}

@app.put("/Address/")
def update_Address(data: Address, session: Session=Depends(get_session)):
  address=session.exec(select(Address)).all()
  if not address:
    raise HTTPException(sstatus_code=404, detail="Address not found")
  update_data=data.dict(exclude_unset=True)
  for a in address:
    for key, value in update_data.items():
      setattr(a, key, value)
  session.commit()

  for a in address:
    session.refresh(a)
  return a

@app.put("/Address/{address_id}")
def update_Address(address_id: int, data: Address, session: Session=Depends(get_session)):
  address= session.get(Address, address_id)
  if not address:
    raise HTTPException(status_code=404, detail="address not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(address, key, value)
  session.commit()
  session.refresh(address)
  return address



@app.post("/Company/")
def create_Address(company: Company, session: Session=Depends(get_session)):
  session.add(company)
  session.commit()
  session.refresh(company)
  return company

@app.get("/Company/")
def get_Company(session: Session=Depends(get_session)):
  company= session.exec(select(Company)).all()
  return company

@app.get("/Company/{company_id}")
def get_Company_by_id(company_id: int, session: Session=Depends(get_session)):
  company= session.get(Company, company_id)
  return company

@app.delete("/Company/{company_id}", status_code=204)
def delete_Company_by_id(company_id: int, session: Session=Depends(get_session)):
  company = session.get(Company, company_id)
  if not company:
    raise HTTPException(status_code=404, detail="Company not found")
  session.delete(company)
  session.commit()
  return {"detail": f"Company {company_id} deleted"}

@app.delete("/Company", status_code=204)
def delete_Company(session: Session=Depends(get_session)):
  company = session.exec(select(Company)).all()
  for company in company:
    session.delete(company)
    session.commit()
  return {"detail": "All Company deleted"}

@app.put("/Company/")
def update_Company(data: Company, session: Session=Depends(get_session)):
  company=session.exec(select(Company)).all()
  if not company:
    raise HTTPException(sstatus_code=404, detail="Company not found")
  update_data=data.dict(exclude_unset=True)
  for c in company:
    for key, value in update_data.items():
      setattr(c, key, value)
  session.commit()

  for c in company:
    session.refresh(c)
  return c

@app.put("/Company/{company_id}")
def update_Company(company_id: int, data: Company, session: Session=Depends(get_session)):
  company= session.get(Company, company_id)
  if not company:
    raise HTTPException(status_code=404, detail="Company not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(company, key, value)
  session.commit()
  session.refresh(company)
  return company


@app.post("/Employee/")
def create_Employee(employee: Employee, session: Session=Depends(get_session)):
  session.add(employee)
  session.commit()
  session.refresh(employee)
  return employee

@app.get("/Employee/")
def get_Employee(session: Session=Depends(get_session)):
  employee= session.exec(select(Address)).all()
  return employee

@app.get("/Employee/{employee_id}")
def get_Employee_by_id(employee_id: int, session: Session=Depends(get_session)):
  employee= session.get(Employee, employee_id)
  return employee

@app.delete("/Employee/{employee_id}", status_code=204)
def delete_Employee_by_id(employee_id: int, session: Session=Depends(get_session)):
  employee= session.get(Employee, employee_id)
  if not employee:
    raise HTTPException(status_code=404, detail="Employee not found")
  session.delete(employee)
  session.commit()
  return {"detail": f"Employee {employee_id} deleted"}

@app.delete("/Employee", status_code=204)
def delete_Employee(session: Session=Depends(get_session)):
  employee= session.exec(select(Employee)).all()
  for employee in employee:
    session.delete(employee)
    session.commit()
  return {"detail": "All Employee deleted"}

@app.put("/Employee/")
def update_Employee(data: Employee, session: Session=Depends(get_session)):
  employee=session.exec(select(Employee)).all()
  if not employee:
    raise HTTPException(sstatus_code=404, detail="Employee not found")
  update_data=data.dict(exclude_unset=True)
  for e in employee:
    for key, value in update_data.items():
      setattr(e, key, value)
  session.commit()

  for e in employee:
    session.refresh(e)
  return e

@app.put("/Employee/{employee_id}")
def update_Employee(employee_id: int, data: Employee, session: Session=Depends(get_session)):
  employee= session.get(Employee, employee_id)
  if not employee:
    raise HTTPException(status_code=404, detail="Employee not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(employee, key, value)
  session.commit()
  session.refresh(employee)
  return employee


@app.post("/Salary/")
def create_Salary(salary: Salary, session: Session=Depends(get_session)):
  session.add(salary)
  session.commit()
  session.refresh(salary)
  return salary

@app.get("/Salary/")
def get_Salary(session: Session=Depends(get_session)):
  salary= session.exec(select(Salary)).all()
  return salary

@app.get("/Salary/{salary_id}")
def get_Salary_by_id(salary_id: int, session: Session=Depends(get_session)):
  salary= session.get(Salary, salary_id)
  return salary

@app.delete("/Salary/{salary_id}", status_code=204)
def delete_Salary_by_id(salary_id: int, session: Session=Depends(get_session)):
  salary= session.get(Salary, salary_id)
  if not salary:
    raise HTTPException(status_code=404, detail="Salary not found")
  session.delete(salary)
  session.commit()
  return {"detail": f"Salary {salary_id} deleted"}

@app.delete("/Salary", status_code=204)
def delete_Salary(session: Session=Depends(get_session)):
  salary= session.exec(select(Salary)).all()
  for salary in salary:
    session.delete(salary)
    session.commit()
  return {"detail": "All Salary deleted"}

@app.put("/Salary/")
def update_Salary(data: Salary, session: Session=Depends(get_session)):
  salary=session.exec(select(Salary)).all()
  if not salary:
    raise HTTPException(sstatus_code=404, detail="Salary not found")
  update_data=data.dict(exclude_unset=True)
  for s in salary:
    for key, value in update_data.items():
      setattr(s, key, value)
  session.commit()

  for s in salary:
    session.refresh(s)
  return s


@app.put("/Salary/{salary_id}")
def update_Salary(salary_id: int, data: Salary, session: Session=Depends(get_session)):
  salary= session.get(Salary, salary_id)
  if not salary:
    raise HTTPException(status_code=404, detail="Salary not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(salary)
  session.commit()
  session.refresh(salary)
  return salary


@app.post("/Tax/")
def create_Tax(tax: Tax, session: Session=Depends(get_session)):
  session.add(tax)
  session.commit()
  session.refresh(tax)
  return tax

@app.get("/Tax/")
def get_Tax(session: Session=Depends(get_session)):
  tax= session.exec(select(Tax)).all()
  return tax

@app.get("/Tax/{tax_id}")
def get_Tax_by_id(tax_id: int, session: Session=Depends(get_session)):
  tax= session.get(Tax, tax_id)
  return tax

@app.delete("/Tax/{tax_id}", status_code=204)
def delete_Tax_by_id(tax_id: int, session: Session=Depends(get_session)):
  tax= session.get(Tax, tax_id)
  if not tax:
    raise HTTPException(status_code=404, detail="Tax not found")
  session.delete(tax)
  session.commit()
  return {"detail": f"Tax {tax_id} deleted"}

@app.delete("/Tax", status_code=204)
def delete_Tax(session: Session=Depends(get_session)):
  tax= session.exec(select(Tax)).all()
  for tax in tax:
    session.delete(tax)
    session.commit()
  return {"detail": "All Tax deleted"}

@app.put("/Tax/")
def update_Tax(data: Tax, session: Session=Depends(get_session)):
  tax=session.exec(select(Tax)).all()
  if not tax:
    raise HTTPException(sstatus_code=404, detail="Tax not found")
  update_data=data.dict(exclude_unset=True)
  for t in tax:
    for key, value in update_data.items():
      setattr(t, key, value)
  session.commit()

  for t in tax:
    session.refresh(t)
  return t

@app.put("/Tax/{tax_id}")
def update_Tax(tax_id: int, data: Tax, session: Session=Depends(get_session)):
  tax= session.get(Tax, tax_id)
  if not tax:
    raise HTTPException(status_code=404, detail="Tax not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(tax)
  session.commit()
  session.refresh(tax)
  return tax


@app.post("/Course/")
def create_Course(course: Course, session: Session=Depends(get_session)):
  session.add(course)
  session.commit()
  session.refresh(course)
  return course

@app.get("/Course/")
def get_Course(session: Session=Depends(get_session)):
  course= session.exec(select(Course)).all()
  return course

@app.get("/Course/{course_id}")
def get_Course_by_id(course_id: int, session: Session=Depends(get_session)):
  course= session.get(Course, course_id)
  return course

@app.delete("/Course/{course_id}", status_code=204)
def delete_Course_by_id(course_id: int, session: Session=Depends(get_session)):
  course= session.get(Course, course_id)
  if not course:
    raise HTTPException(status_code=404, detail="Course not found")
  session.delete(course)
  session.commit()
  return {"detail": f"Course {course_id} deleted"}

@app.delete("/Course", status_code=204)
def delete_Course(session: Session=Depends(get_session)):
  course= session.exec(select(Course)).all()
  for course in course:
    session.delete(course)
    session.commit()
  return {"detail": "All Course deleted"}

@app.put("/Course/")
def update_Course(data: Course, session: Session=Depends(get_session)):
  course=session.exec(select(Course)).all()
  if not course:
    raise HTTPException(sstatus_code=404, detail="Course not found")
  update_data=data.dict(exclude_unset=True)
  for c in course:
    for key, value in update_data.items():
      setattr(c, key, value)
  session.commit()

  for c in course:
    session.refresh(c)
  return c

@app.put("/Course/{course_id}")
def update_Course(course_id: int, data: Course, session: Session=Depends(get_session)):
  course= session.get(Course, course_id)
  if not course:
    raise HTTPException(status_code=404, detail="Course not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(course)
  session.commit()
  session.refresh(course)
  return course



@app.post("/Seat/")
def create_Seat(seat: Seat, session: Session=Depends(get_session)):
  session.add(seat)
  session.commit()
  session.refresh(seat)
  return seat

@app.get("/Seat/")
def get_Seat(session: Session=Depends(get_session)):
  seat= session.exec(select(Seat)).all()
  return seat

@app.get("/Seat/{seat_id}")
def get_Seat_by_id(seat_id: int, session: Session=Depends(get_session)):
  seat= session.get(Seat, seat_id)
  return seat

@app.delete("/Seat/{seat_id}", status_code=204)
def delete_Seat_by_id(seat_id: int, session: Session=Depends(get_session)):
  seat= session.get(Seat, seat_id)
  if not seat:
    raise HTTPException(status_code=404, detail="Seat not found")
  session.delete(seat)
  session.commit()
  return {"detail": f"Seat {seat_id} deleted"}

@app.delete("/Seat", status_code=204)
def delete_Seat(session: Session=Depends(get_session)):
  seat= session.exec(select(Seat)).all()
  for seat in seat:
    session.delete(seat)
    session.commit()
  return {"detail": "All Seat deleted"}

@app.put("/Seat/")
def update_Seat(data: Seat, session: Session=Depends(get_session)):
  seat=session.exec(select(Seat)).all()
  if not seat:
    raise HTTPException(sstatus_code=404, detail="Seat not found")
  update_data=data.dict(exclude_unset=True)
  for s in seat:
    for key, value in update_data.items():
      setattr(s, key, value)
  session.commit()

  for s in seat:
    session.refresh(s)
  return s

@app.put("/Seat/{seat_id}")
def update_Seat(seat_id: int, data: Seat, session: Session=Depends(get_session)):
  seat= session.get(Seat, seat_id)
  if not seat:
    raise HTTPException(status_code=404, detail="Seat not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(seat)
  session.commit()
  session.refresh(seat)
  return seat


@app.post("/Student/")
def create_Student(student: Student, session: Session=Depends(get_session)):
  session.add(student)
  session.commit()
  session.refresh(student)
  return student

@app.get("/Student/")
def get_Student(session: Session=Depends(get_session)):
  student= session.exec(select(Student)).all()
  return student

@app.get("/Student/{student_id}")
def get_Student_by_id(student_id: int, session: Session=Depends(get_session)):
  student= session.get(Student, student_id)
  return student

@app.delete("/Student/{student_id}", status_code=204)
def delete_Student_by_id(student_id: int, session: Session=Depends(get_session)):
  student= session.get(Student, student_id)
  if not student:
    raise HTTPException(status_code=404, detail="Student not found")
  session.delete(student)
  session.commit()
  return {"detail": f"Student {student_id} deleted"}

@app.delete("/Student", status_code=204)
def delete_Student(session: Session=Depends(get_session)):
  student= session.exec(select(Student)).all()
  for student in student:
    session.delete(student)
    session.commit()
  return {"detail": "All Student deleted"}

@app.put("/Student/")
def update_Student(data: Student, session: Session=Depends(get_session)):
  student=session.exec(select(Student)).all()
  if not student:
    raise HTTPException(sstatus_code=404, detail="Student not found")
  update_data=data.dict(exclude_unset=True)
  for s in student:
    for key, value in update_data.items():
      setattr(s, key, value)
  session.commit()

  for s in student:
    session.refresh(s)
  return s

@app.put("/Student/{student_id}")
def update_Student(student_id: int, data: Student, session: Session=Depends(get_session)):
  student= session.get(Student, student_id)
  if not student:
    raise HTTPException(status_code=404, detail="Student not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(student)
  session.commit()
  session.refresh(student)
  return student


@app.post("/Registration/")
def create_Registration(registration: Registration, session: Session=Depends(get_session)):
  session.add(registration)
  session.commit()
  session.refresh(registration)
  return registration

@app.get("/Registration/")
def get_Registration(session: Session=Depends(get_session)):
  registration= session.exec(select(Registration)).all()
  return registration

@app.get("/Registration/{registration_id}")
def get_Registration_by_id(registration_id: int, session: Session=Depends(get_session)):
  registration= session.get(Registration, registration_id)
  return registration

@app.delete("/Registration/{registration_id}", status_code=204)
def delete_Registration_by_id(registration_id: int, session: Session=Depends(get_session)):
  registration= session.get(Registration, registration_id)
  if not registration:
    raise HTTPException(status_code=404, detail="Registration not found")
  session.delete(registration)
  session.commit()
  return {"detail": f"Registration {registration_id} deleted"}

@app.delete("/Registration", status_code=204)
def delete_Registration(session: Session=Depends(get_session)):
  registration= session.exec(select(Registration)).all()
  for registration in registration:
    session.delete(registration)
    session.commit()
  return {"detail": "All Registration deleted"}

@app.put("/Registration/")
def update_Student(data: Registration, session: Session=Depends(get_session)):
  registration=session.exec(select(Registration)).all()
  if not registration:
    raise HTTPException(sstatus_code=404, detail="Registration not found")
  update_data=data.dict(exclude_unset=True)
  for r in registration:
    for key, value in update_data.items():
      setattr(r, key, value)
  session.commit()

  for r in registration:
    session.refresh(r)
  return r

@app.put("/Registration/{registration_id}")
def update_Registration(registration_id: int, data: Registration, session: Session=Depends(get_session)):
  registration= session.get(Registration, registration_id)
  if not registration:
    raise HTTPException(status_code=404, detail="Registration not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(registration)
  session.commit()
  session.refresh(registration)
  return registration


@app.post("/Discount/")
def create_Discount(discount: Discount, session: Session=Depends(get_session)):
  session.add(discount)
  session.commit()
  session.refresh(discount)
  return discount

@app.get("/Discount/")
def get_Discount(session: Session=Depends(get_session)):
  discount= session.exec(select(Discount)).all()
  return discount

@app.get("/Discount/{discount_id}")
def get_Discount_by_id(discount_id: int, session: Session=Depends(get_session)):
  discount= session.get(Discount, discount_id)
  return discount

@app.delete("/Discount/{discount_id}", status_code=204)
def delete_Discount_by_id(discount_id: int, session: Session=Depends(get_session)):
  discount= session.get(Discount, discount_id)
  if not discount:
    raise HTTPException(status_code=404, detail="Discount not found")
  session.delete(discount)
  session.commit()
  return {"detail": f"Discount {discount_id} deleted"}

@app.delete("/Discount", status_code=204)
def delete_Discount(session: Session=Depends(get_session)):
  discount= session.exec(select(Discount)).all()
  for discount in discount:
    session.delete(discount)
    session.commit()
  return {"detail": "All Discount deleted"}

@app.put("/Discount/")
def update_Discount(data: Discount, session: Session=Depends(get_session)):
  discount=session.exec(select(Discount)).all()
  if not discount:
    raise HTTPException(sstatus_code=404, detail="Discount not found")
  update_data=data.dict(exclude_unset=True)
  for d in discount:
    for key, value in update_data.items():
      setattr(d, key, value)
  session.commit()

  for d in discount:
    session.refresh(d)
  return d

@app.put("/Discount/{discount_id}")
def update_Discount(discount_id: int, data: Discount, session: Session=Depends(get_session)):
  discount= session.get(Discount, discount_id)
  if not discount:
    raise HTTPException(status_code=404, detail="Discount not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(discount)
  session.commit()
  session.refresh(discount)
  return discount


@app.post("/Penality/")
def create_Penality(penality: Penality, session: Session=Depends(get_session)):
  session.add(penality)
  session.commit()
  session.refresh(penality)
  return penality

@app.get("/Penality/")
def get_Penality(session: Session=Depends(get_session)):
  penality= session.exec(select(Penality)).all()
  return penality

@app.get("/Penality/{penality_id}")
def get_Penality_by_id(penality_id: int, session: Session=Depends(get_session)):
  penality= session.get(Penality, penality_id)
  return penality

@app.delete("/Penality/{penality_id}", status_code=204)
def delete_Penality_by_id(penality_id: int, session: Session=Depends(get_session)):
  penality= session.get(Penality, penality_id)
  if not penality:
    raise HTTPException(status_code=404, detail="Penality not found")
  session.delete(penality)
  session.commit()
  return {"detail": f"Penality {penality_id} deleted"}

@app.delete("/Penality", status_code=204)
def delete_Penality(session: Session=Depends(get_session)):
  penality= session.exec(select(Penality)).all()
  for penality in penality:
    session.delete(penality)
    session.commit()
  return {"detail": "All Penality deleted"}

@app.put("/Penality/")
def update_Penality(data: Penality, session: Session=Depends(get_session)):
  penality=session.exec(select(Penality)).all()
  if not penality:
    raise HTTPException(sstatus_code=404, detail="Penality not found")
  update_data=data.dict(exclude_unset=True)
  for p in penality:
    for key, value in update_data.items():
      setattr(p, key, value)
  session.commit()

  for p in penality:
    session.refresh(p)
  return p

@app.put("/Penality/{penality_id}")
def update_Penality(penality_id: int, data: Penality, session: Session=Depends(get_session)):
  penality= session.get(Penality, penality_id)
  if not penality:
    raise HTTPException(status_code=404, detail="Penality not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(penality)
  session.commit()
  session.refresh(penality)
  return penality


@app.post("/Fees/")
def create_Fees(fees: Fees, session: Session=Depends(get_session)):
  session.add(fees)
  session.commit()
  session.refresh(fees)
  return fees

@app.get("/Fees/")
def get_Fees(session: Session=Depends(get_session)):
  fees= session.exec(select(Fees)).all()
  return fees

@app.get("/Fees/{fees_id}")
def get_Fees_by_id(fees_id: int, session: Session=Depends(get_session)):
  fees= session.get(Fees, fees_id)
  return fees

@app.delete("/Fees/{fees_id}", status_code=204)
def delete_Fees_by_id(fees_id: int, session: Session=Depends(get_session)):
  fees= session.get(Fees, fees_id)
  if not fees:
    raise HTTPException(status_code=404, detail="Fees not found")
  session.delete(fees)
  session.commit()
  return {"detail": f"Fees {fees_id} deleted"}

@app.delete("/Fees", status_code=204)
def delete_Fees(session: Session=Depends(get_session)):
  fees= session.exec(select(Fees)).all()
  for fees in fees:
    session.delete(fees)
    session.commit()
  return {"detail": "All Fees deleted"}

@app.put("/Fees/")
def update_Fees(data: Fees, session: Session=Depends(get_session)):
  fees=session.exec(select(Fees)).all()
  if not fees:
    raise HTTPException(sstatus_code=404, detail="Fees not found")
  update_data=data.dict(exclude_unset=True)
  for f in fees:
    for key, value in update_data.items():
      setattr(f, key, value)
  session.commit()

  for f in fees:
    session.refresh(f)
  return f

@app.put("/Fees/{fees_id}")
def update_Fees(fees_id: int, data: Fees, session: Session=Depends(get_session)):
  fees= session.get(Fees, fees_id)
  if not fees:
    raise HTTPException(status_code=404, detail="Fees not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(fees)
  session.commit()
  session.refresh(fees)
  return fees


@app.post("/Payment/")
def create_Payment(payment: Payment, session: Session=Depends(get_session)):
  session.add(payment)
  session.commit()
  session.refresh(payment)
  return payment

@app.get("/Payment/")
def get_Payment(session: Session=Depends(get_session)):
  payment= session.exec(select(Payment)).all()
  return payment

@app.get("/Payment/{payment_id}")
def get_Payment_by_id(payment_id: int, session: Session=Depends(get_session)):
  payment= session.get(Payment, payment_id)
  return payment

@app.delete("/Payment/{payment_id}", status_code=204)
def delete_Payment_by_id(payment_id: int, session: Session=Depends(get_session)):
  payment= session.get(Payment, payment_id)
  if not payment:
    raise HTTPException(status_code=404, detail="Payment not found")
  session.delete(payment)
  session.commit()
  return {"detail": f"Payment {payment_id} deleted"}

@app.delete("/Payment", status_code=204)
def delete_Payment(session: Session=Depends(get_session)):
  payment= session.exec(select(Payment)).all()
  for payment in payment:
    session.delete(payment)
    session.commit()
  return {"detail": "All Payment deleted"}

@app.put("/Payment/")
def update_Fees(data: Payment, session: Session=Depends(get_session)):
  payment=session.exec(select(Payment)).all()
  if not payment:
    raise HTTPException(sstatus_code=404, detail="Payment not found")
  update_data=data.dict(exclude_unset=True)
  for p in payment:
    for key, value in update_data.items():
      setattr(p, key, value)
  session.commit()

  for p in payment:
    session.refresh(p)
  return p

@app.put("/Payment/{payment_id}")
def update_Payment(payment_id: int, data: Payment, session: Session=Depends(get_session)):
  payment= session.get(Payment, payment_id)
  if not payment:
    raise HTTPException(status_code=404, detail="Payment not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(payment)
  session.commit()
  session.refresh(payment)
  return payment


@app.post("/Certification/")
def create_Certification(certification: Certification, session: Session=Depends(get_session)):
  session.add(certification)
  session.commit()
  session.refresh(certification)
  return certification

@app.get("/Certification/")
def get_Certification(session: Session=Depends(get_session)):
  certification= session.exec(select(Certification)).all()
  return certification

@app.get("/Certification/{certification_id}")
def get_Certification_by_id(certification_id: int, session: Session=Depends(get_session)):
  certification= session.get(Certification, certification_id)
  return certification

@app.delete("/Certification/{certification_id}", status_code=204)
def delete_Certification_by_id(certification_id: int, session: Session=Depends(get_session)):
  certification= session.get(Certification, certification_id)
  if not certification:
    raise HTTPException(status_code=404, detail="Certification not found")
  session.delete(certification)
  session.commit()
  return {"detail": f"Certification {certification_id} deleted"}

@app.delete("/Certification", status_code=204)
def delete_Certification(session: Session=Depends(get_session)):
  certification= session.exec(select(Certification)).all()
  for certification in certification:
    session.delete(certification)
    session.commit()
  return {"detail": "All Certification deleted"}

@app.put("/Certification/")
def update_Certification(data: Certification, session: Session=Depends(get_session)):
  certification=session.exec(select(Certification)).all()
  if not certification:
    raise HTTPException(sstatus_code=404, detail="Certification not found")
  update_data=data.dict(exclude_unset=True)
  for c in certification:
    for key, value in update_data.items():
      setattr(c, key, value)
  session.commit()

  for c in certification:
    session.refresh(c)
  return c

@app.put("/Certification/{certification_id}")
def update_Certification(certification_id: int, data: Certification, session: Session=Depends(get_session)):
  certification= session.get(Certification, certification_id)
  if not certification:
    raise HTTPException(status_code=404, detail="Certification not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(certification)
  session.commit()
  session.refresh(certification)
  return certification


@app.post("/Placement/")
def create_Placement(placement: Placement, session: Session=Depends(get_session)):
  session.add(placement)
  session.commit()
  session.refresh(placement)
  return placement

@app.get("/Placement/")
def get_Placement(session: Session=Depends(get_session)):
  placement= session.exec(select(Placement)).all()
  return placement

@app.get("/Placement/{placement_id}")
def get_Placement_by_id(placement_id: int, session: Session=Depends(get_session)):
  placement= session.get(Placement, placement_id)
  return placement

@app.delete("/Placement/{placement_id}", status_code=204)
def delete_Placement_by_id(placement_id: int, session: Session=Depends(get_session)):
  placement= session.get(Placement, placement_id)
  if not placement:
    raise HTTPException(status_code=404, detail="Placement not found")
  session.delete(placement)
  session.commit()
  return {"detail": f"Placement {placement_id} deleted"}

@app.delete("/Placement", status_code=204)
def delete_Placement(session: Session=Depends(get_session)):
  placement= session.exec(select(Placement)).all()
  for placement in placement:
    session.delete(placement)
    session.commit()
  return {"detail": "All Placement deleted"}

@app.put("/Placement/")
def update_Placement(data: Placement, session: Session=Depends(get_session)):
  placement=session.exec(select(Placement)).all()
  if not placement:
    raise HTTPException(sstatus_code=404, detail="Placement not found")
  update_data=data.dict(exclude_unset=True)
  for p in placement:
    for key, value in update_data.items():
      setattr(p, key, value)
  session.commit()

  for p in placement:
    session.refresh(p)
  return p

@app.put("/Placement/{placement_id}")
def update_Placement(placement_id: int, data: Placement, session: Session=Depends(get_session)):
  placement= session.get(Placement, placement_id)
  if not placement:
    raise HTTPException(status_code=404, detail="Placement not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(placement)
  session.commit()
  session.refresh(placement)
  return placement


@app.post("/Package/")
def create_Package(package: Package, session: Session=Depends(get_session)):
  session.add(package)
  session.commit()
  session.refresh(package)
  return package

@app.get("/Package/")
def get_Package(session: Session=Depends(get_session)):
  package= session.exec(select(Package)).all()
  return package

@app.get("/Package/{package_id}")
def get_Package_by_id(package_id: int, session: Session=Depends(get_session)):
  package= session.get(Package, package_id)
  return package

@app.delete("/Package/{package_id}", status_code=204)
def delete_Package_by_id(package_id: int, session: Session=Depends(get_session)):
  package= session.get(Package, package_id)
  if not package:
    raise HTTPException(status_code=404, detail="Package not found")
  session.delete(package)
  session.commit()
  return {"detail": f"Package {package_id} deleted"}

@app.delete("/Package", status_code=204)
def delete_Package(session: Session=Depends(get_session)):
  package= session.exec(select(Package)).all()
  for package in package:
    session.delete(package)
    session.commit()
  return {"detail": "All Package deleted"}

@app.put("/Package/")
def update_Package(data: Package, session: Session=Depends(get_session)):
  package=session.exec(select(Package)).all()
  if not package:
    raise HTTPException(sstatus_code=404, detail="Package not found")
  update_data=data.dict(exclude_unset=True)
  for p in package:
    for key, value in update_data.items():
      setattr(p, key, value)
  session.commit()

  for p in package:
    session.refresh(p)
  return p

@app.put("/Package/{package_id}")
def update_Package(package_id: int, data: Package, session: Session=Depends(get_session)):
  package= session.get(Package, package_id)
  if not package:
    raise HTTPException(status_code=404, detail="Package not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(package)
  session.commit()
  session.refresh(package)
  return package


@app.post("/Batch/")
def create_Batch(batch: Batch, session: Session=Depends(get_session)):
  session.add(batch)
  session.commit()
  session.refresh(batch)
  return batch

@app.get("/Batch/")
def get_Batch(session: Session=Depends(get_session)):
  batch= session.exec(select(Batch)).all()
  return batch

@app.get("/Batch/{batch_id}")
def get_Batch_by_id(batch_id: int, session: Session=Depends(get_session)):
  batch= session.get(Batch, batch_id)
  return batch

@app.delete("/Batch/{batch_id}", status_code=204)
def delete_Batch_by_id(batch_id: int, session: Session=Depends(get_session)):
  batch = session.get(Batch, batch_id)
  if not batch:
    raise HTTPException(status_code=404, detail="Batch not found")
  session.delete(batch)
  session.commit()
  return {"detail": f"Batch {batch_id} deleted"}

@app.delete("/Batch", status_code=204)
def delete_Batch(session: Session=Depends(get_session)):
  batch = session.exec(select(Batch)).all()
  for batch in batch:
    session.delete(batch)
    session.commit()
  return {"detail": "All Batch deleted"}

@app.put("/Batch/")
def update_Batch(data: Batch, session: Session=Depends(get_session)):
  batch=session.exec(select(Batch)).all()
  if not batch:
    raise HTTPException(sstatus_code=404, detail="Batch not found")
  update_data=data.dict(exclude_unset=True)
  for b in batch:
    for key, value in update_data.items():
      setattr(b, key, value)
  session.commit()

  for b in batch:
    session.refresh(b)
  return b

@app.put("/Batch/{batch_id}")
def update_Batch(batch_id: int, data: Batch, session: Session=Depends(get_session)):
  batch= session.get(Batch, batch_id)
  if not batch:
    raise HTTPException(status_code=404, detail="Batch not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(batch)
  session.commit()
  session.refresh(batch)
  return batch


@app.post("/Attendance/")
def create_Attendance(attendance: Attendance, session: Session=Depends(get_session)):
  session.add(attendance)
  session.commit()
  session.refresh(attendance)
  return attendance

@app.get("/Attendance/")
def get_Attendance(session: Session=Depends(get_session)):
  attendance= session.exec(select(Attendance)).all()
  return attendance

@app.get("/Attendance/{attendance_id}")
def get_Attendance_by_id(attendance_id: int, session: Session=Depends(get_session)):
  attendance= session.get(Attendance, attendance_id)
  return attendance

@app.delete("/Attendance/{attendance_id}", status_code=204)
def delete_Attendance_by_id(attendance_id: int, session: Session=Depends(get_session)):
  attendance = session.get(Attendance, attendance_id)
  if not attendance:
    raise HTTPException(status_code=404, detail="Attendance not found")
  session.delete(attendance)
  session.commit()
  return {"detail": f"Attendance {attendance_id} deleted"}

@app.delete("/Attendance", status_code=204)
def delete_Attendance(session: Session=Depends(get_session)):
  attendance = session.exec(select(Attendance)).all()
  for attendance in attendance:
    session.delete(attendance)
    session.commit()
  return {"detail": "All Attendance deleted"}

@app.put("/Attendance/")
def update_Attendance(data: Attendance, session: Session=Depends(get_session)):
  attendance=session.exec(select(Attendance)).all()
  if not attendance:
    raise HTTPException(sstatus_code=404, detail="Attendance not found")
  update_data=data.dict(exclude_unset=True)
  for a in attendance:
    for key, value in update_data.items():
      setattr(a, key, value)
  session.commit()

  for a in attendance:
    session.refresh(a)
  return a

@app.put("/Attendance/{attendance_id}")
def update_Attendance(attendance_id: int, data: Attendance, session: Session=Depends(get_session)):
  attendance= session.get(Attendance, attendance_id)
  if not attendance:
    raise HTTPException(status_code=404, detail="Attendance not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(attendance)
  session.commit()
  session.refresh(attendance)
  return attendance


@app.post("/Assignment/")
def create_Assignment(assignment: Assignment, session: Session=Depends(get_session)):
  session.add(assignment)
  session.commit()
  session.refresh(assignment)
  return assignment

@app.get("/Assignment/")
def get_Assignment(session: Session=Depends(get_session)):
  assignment= session.exec(select(Assignment)).all()
  return assignment

@app.get("/Assignment/{assignment_id}")
def get_Assignment_by_id(assignment_id: int, session: Session=Depends(get_session)):
  assignment= session.get(Assignment, assignment_id)
  return assignment

@app.delete("/Assignment/{assignment_id}", status_code=204)
def delete_Assignment_by_id(assignment_id: int, session: Session=Depends(get_session)):
  assignment = session.get(Assignment, assignment_id)
  if not assignment:
    raise HTTPException(status_code=404, detail="Assignment not found")
  session.delete(assignment)
  session.commit()
  return {"detail": f"Assignment {assignment_id} deleted"}

@app.delete("/Assignment", status_code=204)
def delete_Assignment(session: Session=Depends(get_session)):
  assignment = session.exec(select(Assignment)).all()
  for assignment in assignment:
    session.delete(assignment)
    session.commit()
  return {"detail": "All Assignment deleted"}

@app.put("/Assignment/")
def update_Assignment(data: Assignment, session: Session=Depends(get_session)):
  assignment=session.exec(select(Assignment)).all()
  if not assignment:
    raise HTTPException(sstatus_code=404, detail="Assignment not found")
  update_data=data.dict(exclude_unset=True)
  for a in assignment:
    for key, value in update_data.items():
      setattr(a, key, value)
  session.commit()

  for a in assignment:
    session.refresh(a)
  return a

@app.put("/Assignment/{assignment_id}")
def update_Assignment(assignment_id: int, data: Assignment, session: Session=Depends(get_session)):
  assignment= session.get(Assignment, assignment_id)
  if not assignment:
    raise HTTPException(status_code=404, detail="Assignment not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(assignment)
  session.commit()
  session.refresh(assignment)
  return assignment


@app.post("/Result/")
def create_Result(result: Result, session: Session=Depends(get_session)):
  session.add(result)
  session.commit()
  session.refresh(result)
  return result

@app.get("/Result/")
def get_Result(session: Session=Depends(get_session)):
  result= session.exec(select(Result)).all()
  return result

@app.get("/Result/{result_id}")
def get_Result_by_id(result_id: int, session: Session=Depends(get_session)):
  result= session.get(Result, result_id)
  return result

@app.delete("/Result/{result_id}", status_code=204)
def delete_Result_by_id(result_id: int, session: Session=Depends(get_session)):
  result = session.get(Result, result_id)
  if not result:
    raise HTTPException(status_code=404, detail="Result not found")
  session.delete(result)
  session.commit()
  return {"detail": f"Result {result_id} deleted"}

@app.delete("/Result", status_code=204)
def delete_Result(session: Session=Depends(get_session)):
  result = session.exec(select(Result)).all()
  for result in result:
    session.delete(result)
    session.commit()
  return {"detail": "All Result deleted"}

@app.put("/Result/")
def update_Result(data: Result, session: Session=Depends(get_session)):
  result=session.exec(select(Result)).all()
  if not result:
    raise HTTPException(sstatus_code=404, detail="Result not found")
  update_data=data.dict(exclude_unset=True)
  for r in result:
    for key, value in update_data.items():
      setattr(r, key, value)
  session.commit()

  for r in result:
    session.refresh(r)
  return r

@app.put("/Result/{result_id}")
def update_Result(result_id: int, data: Result, session: Session=Depends(get_session)):
  result= session.get(Result, result_id)
  if not result:
    raise HTTPException(status_code=404, detail="Result not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(result)
  session.commit()
  session.refresh(result)
  return result


@app.post("/Inquiry/")
def create_Inquiry(inquiry: Inquiry, session: Session=Depends(get_session)):
  session.add(inquiry)
  session.commit()
  session.refresh(inquiry)
  return inquiry

@app.get("/Inquiry/")
def get_Inquiry(session: Session=Depends(get_session)):
  inquiry= session.exec(select(Inquiry)).all()
  return inquiry

@app.get("/Inquiry/{inquiry_id}")
def get_Inquiry_by_id(inquiry_id: int, session: Session=Depends(get_session)):
  inquiry= session.get(Inquiry, inquiry_id)
  return inquiry

@app.delete("/Inquiry/{inquiry_id}", status_code=204)
def delete_Inquiry_by_id(inquiry_id: int, session: Session=Depends(get_session)):
  inquiry = session.get(Inquiry, inquiry_id)
  if not inquiry:
    raise HTTPException(status_code=404, detail="Inquiry not found")
  session.delete(inquiry)
  session.commit()
  return {"detail": f"Inquiry {inquiry_id} deleted"}

@app.delete("/Inquiry", status_code=204)
def delete_Inquiry(session: Session=Depends(get_session)):
  inquiry = session.exec(select(Inquiry)).all()
  for inquiry in inquiry:
    session.delete(inquiry)
    session.commit()
  return {"detail": "All Inquiry deleted"}

@app.put("/Inquiry/")
def update_Inquiry(data: Inquiry, session: Session=Depends(get_session)):
  inquiry=session.exec(select(Inquiry)).all()
  if not inquiry:
    raise HTTPException(sstatus_code=404, detail="Inquiry not found")
  update_data=data.dict(exclude_unset=True)
  for i in inquiry:
    for key, value in update_data.items():
      setattr(i, key, value)
  session.commit()

  for i in inquiry:
    session.refresh(i)
  return i

@app.put("/Inquiry/{inquiry_id}")
def update_Inquiry(inquiry_id: int, data: Inquiry, session: Session=Depends(get_session)):
  inquiry= session.get(Inquiry, inquiry_id)
  if not inquiry:
    raise HTTPException(status_code=404, detail="Inquiry not found")
  
  for key, value in data.dict(exclude_unset=True).items():
    setattr(inquiry)
  session.commit()
  session.refresh(inquiry)
  return inquiry