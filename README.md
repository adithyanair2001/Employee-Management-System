# How to Run the Application

### Using Docker
1. Ensure Docker and Docker Compose are installed.
2. Start the containers with the following command:
   ```bash
   docker-compose up --build
   ```
3. Access the application at `http://localhost:5000`.

### Stopping the Application
To stop the containers, run:
```bash
docker-compose down
```

---

*Previous content remains unchanged*# Employee Management System - Developer Guide

## Project Overview
This is a full-stack employee management application built with Flask, HTML, and Docker. It uses SQLite as the database to store employee details.

## Prerequisites
- Docker
- Docker Compose
- Python 3.7+
- SQLite

## Installation
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate to the project directory.

## How to Run the Application
### Using Docker
1. Ensure Docker and Docker Compose are installed.
2. Start the containers with the following command:
   ```bash
   docker-compose up --build
   ```
3. Access the application at `http://localhost:5000`.

### Stopping the Application
To stop the containers, run:
```bash
docker-compose down
```

## Development Workflow

### Coding Standards
- Use PEP8 style guidelines
- Keep functions under 20 lines
- Use descriptive variable names
- Write docstrings for complex functions

### Testing
Unit tests are located in the `tests` directory. Run tests with:
```bash
docker-compose exec backend pytest tests/
```

## Key Concepts

### Data Model
Employees have:
- id (primary key)
- name
- position
- department
- salary

## Common Tasks

### Adding a new employee
1. Send a POST request to `/api/employees`
2. Include employee details in JSON format:
```json
{
  "name": "John Doe",
  "position": "Developer",
  "department": "IT",
  "salary": 50000
}
```

## Troubleshooting

### Database connection issues
Check the `config.py` file for correct database URI. The default is:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
```

## References
- Flask documentation: https://flask.palletsprojects.com/
- SQLite documentation: https://sqlite.org/docs.html
