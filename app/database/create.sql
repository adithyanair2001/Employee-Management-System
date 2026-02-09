
USE mydb;

-- 1. Department table
CREATE TABLE department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    UNIQUE KEY idx_department_name (name)
);

-- 2. Employee table 
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    hire_date DATE NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(department_id),
    INDEX idx_employee_email (email),
    INDEX idx_employee_department (department_id)
);

-- 3. Salary table
CREATE TABLE salary (
    salary_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    INDEX idx_salary_employee (employee_id),
    INDEX idx_salary_start_date (start_date)
);