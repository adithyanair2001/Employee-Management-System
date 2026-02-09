import os
import pytest
from flask import Flask
from Application.application import app as flask_app
from Application.models import db, Employee, Department, Salary

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with flask_app.app_context():
        db.create_all()
        # Add a department
        dept = Department(name='TestDept', location='TestLoc')
        db.session.add(dept)
        db.session.commit()
        # Add an employee
        emp = Employee(first_name='John', last_name='Doe', email='john.doe@example.com', hire_date='2022-01-01', department_id=dept.department_id)
        db.session.add(emp)
        db.session.commit()
        # Add a salary
        sal = Salary(employee_id=emp.employee_id, amount=50000, start_date='2022-01-01')
        db.session.add(sal)
        db.session.commit()
    with flask_app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Employees' in rv.data

def test_get_employee(client):
    rv = client.get('/employee/1')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['name'] == 'John Doe'
    assert data['salary'] == 50000.0
    assert data['department'] == 'TestDept'

def test_add_employee(client):
    payload = {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@example.com',
        'hire_date': '2023-01-01',
        'department_id': 1
    }
    rv = client.post('/employee', json=payload)
    assert rv.status_code == 201
    data = rv.get_json()
    assert 'employee_id' in data
    assert data['message'] == 'Employee added successfully!'

def test_add_employee_missing_field(client):
    payload = {
        'first_name': 'Jane',
        'email': 'jane.smith@example.com',
        'hire_date': '2023-01-01',
        'department_id': 1
    }
    rv = client.post('/employee', json=payload)
    assert rv.status_code == 400
    data = rv.get_json()
    assert 'error' in data

def test_add_employee_duplicate_email(client):
    payload = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'hire_date': '2023-01-01',
        'department_id': 1
    }
    rv = client.post('/employee', json=payload)
    assert rv.status_code == 400
    data = rv.get_json()
    assert 'error' in data
