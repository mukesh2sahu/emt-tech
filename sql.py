CREATE DATABASE company_hr;
USE company_hr;

#Left Table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

#Right Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10,2),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);


INSERT INTO departments (department_id, department_name, location) VALUES
(10, 'Administration', 'New York'),
(20, 'Marketing', 'Los Angeles'),
(30, 'Purchasing', 'Chicago'),
(40, 'Human Resources', 'Boston'),
(50, 'IT', 'San Francisco');

INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, salary, department_id) VALUES
(101, 'John', 'Smith', 'john.smith@company.com', '2020-06-15', 85000.00, 10),
(102, 'Emily', 'Johnson', 'emily.johnson@company.com', '2019-03-22', 72000.00, 20),
(103, 'Michael', 'Williams', 'michael.williams@company.com', '2021-01-10', 68000.00, 30),
(104, 'Sarah', 'Brown', 'sarah.brown@company.com', '2018-11-05', 92000.00, 20),
(105, 'David', 'Jones', 'david.jones@company.com', '2022-02-18', 75000.00, 10),
(106, 'Jennifer', 'Garcia', 'jennifer.garcia@company.com', '2020-09-30', 81000.00, 40),
(107, 'Robert', 'Miller', 'robert.miller@company.com', '2021-07-12', 65000.00, NULL),
(108, 'Lisa', 'Davis', 'lisa.davis@company.com', '2019-05-25', 88000.00, 50),
(109, 'James', 'Rodriguez', 'james.rodriguez@company.com', '2022-04-03', 70000.00, NULL),
(110, 'Patricia', 'Martinez', 'patricia.martinez@company.com', '2018-08-14', 95000.00, 30);

select * from employees;

select * from departments;

SELECT first_name AS name, salary AS income FROM employees;

#An INNER JOIN returns only the rows where there's a matching value in both tables you're joining.
-- INNER JOIN: Only matching rows (employees with departments)
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

#A LEFT JOIN keeps all records from the first (left) table and adds matching data from the second (right) table. 
#If no match exists, it fills in NULL for the right table's columns.
-- LEFT JOIN: All employees (including those without departments)
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

#A RIGHT JOIN keeps all records from the second (right) table and adds matching data from the first (left) table. 
#If no match exists, it fills in NULL for the left table's columns.
-- RIGHT JOIN: All departments (including those without employees)
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;

-- FULL OUTER JOIN: All rows from both tables (not supported in MySQL, use UNION of LEFT and RIGHT)
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
UNION
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id
WHERE e.employee_id IS NULL;

-- CROSS JOIN: Cartesian product of all rows
SELECT e.first_name, d.department_name
FROM employees e
CROSS JOIN departments d;

    