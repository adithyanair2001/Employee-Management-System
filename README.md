
# Employee Management System

## Project Overview
The Employee Management System is a full-stack application designed to manage employee details using Flask as the web framework and MySQL as the database. The system utilizes Docker containers and Docker Compose to run the application and database together.


## Prerequisites

To run this project, you will need:

- **Docker** (for containerization)
- **Docker Compose** (for orchestrating multi-container applications)

### Installing Docker and Docker Compose

#### Windows
1. Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
2. Follow the installation instructions and ensure Docker Desktop is running.
3. Docker Compose is included with Docker Desktop.
4. (Optional) Enable WSL 2 backend for better performance (recommended for Windows 10/11).

#### Mac
1. Download and install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
2. Follow the installation instructions and ensure Docker Desktop is running.
3. Docker Compose is included with Docker Desktop.

#### Linux (Ubuntu/Debian example)
1. Uninstall old versions:
   ```bash
   sudo apt-get remove docker docker-engine docker.io containerd runc
   ```
2. Install Docker Engine:
   ```bash
   sudo apt-get update
   sudo apt-get install ca-certificates curl gnupg
   sudo install -m 0755 -d /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```
3. Add your user to the docker group (optional, to run docker without sudo):
   ```bash
   sudo usermod -aG docker $USER
   # Log out and log back in for this to take effect
   ```
4. Verify installation:
   ```bash
   docker --version
   docker compose version
   ```

## Installation Steps (All Platforms)

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd Employee-Management-System
   ```

2. **Configure environment variables (optional):**
   - The `.env` file in the root directory contains default database credentials. You can edit this file if needed.

3. **Build and start the application:**
   ```bash
   docker compose up --build
   ```
   - This command will build the backend and database images, start the containers, and initialize the database with schema and sample data.

4. **Access the application:**
   - Open your browser and go to: [http://localhost:5000](http://localhost:5000)

5. **Stopping the application:**
   ```bash
   docker compose down
   ```
   - This will stop and remove the running containers.

## Project Structure

- **app**: Contains all source code related to the Flask application.
  - `dockerfile`: Instructions for building the Docker image for the Flask app.
  - `UserInterface/index.html`: HTML structure of the user interface (now with responsive design and client-side validation).
  - `database/`: SQL scripts and configuration files for setting up the MySQL database.
- **docker-compose.yml**: Orchestrates the backend and database containers.
- **.env**: Stores environment variables for configuration.

## Database Setup

The database is automatically initialized with schema and sample data using the scripts in `app/database/` when the containers are started.

## Features
- RESTful API endpoints for employee management
- Input validation and error handling on both backend and frontend
- Responsive and user-friendly web interface
- Logging for backend actions
- Environment variable-based configuration

## Running the Application

To run the application, use Docker Compose as described above.

## Stopping the Application

To stop and remove running containers:
```bash
docker-compose down
```

## Contributing Guidelines

- Follow PEP 8 style guidelines for Python code.
- Write docstrings for complex functions.
- Keep functions under 20 lines.
- Use descriptive variable names.

## Testing

Unit tests can be added in a `tests` directory. (Not included by default.)

## References

- Flask documentation: https://flask.palletsprojects.com/
- MySQL documentation: https://dev.mysql.com/doc/
