







import os
import logging
from flask import Flask, render_template, jsonify, request, abort
from models import db, Employee, Salary
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='../UserInterface')

# Read DB config from environment variables
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST', 'mydb')
DB_NAME = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/employee/<int:id>')
def get_employee(id):
    try:
        emp = Employee.query.get_or_404(id)
        salary = Salary.query.filter_by(employee_id=emp.employee_id).order_by(Salary.start_date.desc()).first()
        return jsonify({
            'name': f"{emp.first_name} {emp.last_name}",
            'employee_id': emp.employee_id,
            'salary': float(salary.amount) if salary else None,
            'department': emp.department.name if emp.department else "N/A"
        })
    except SQLAlchemyError as e:
        logger.error(f"Error fetching employee: {e}")
        abort(500, description="Database error.")

# Example: Add employee endpoint with validation
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email', 'hire_date', 'department_id']
    for field in required_fields:
        if field not in data:
            logger.warning(f"Missing field: {field}")
            return jsonify({'error': f'Missing field: {field}'}), 400
    try:
        # Validate date
        try:
            hire_date = datetime.strptime(data['hire_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format for hire_date. Use YYYY-MM-DD.'}), 400
        # Check for existing email
        if Employee.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists.'}), 400
        emp = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            hire_date=hire_date,
            department_id=data['department_id']
        )
        db.session.add(emp)
        db.session.commit()
        logger.info(f"Added employee: {emp.email}")
        return jsonify({'message': 'Employee added successfully!', 'employee_id': emp.employee_id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Error adding employee: {e}")
        return jsonify({'error': 'Database error.'}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
