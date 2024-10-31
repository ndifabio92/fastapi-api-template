# FASTAPI-API-TEMPLATE

# Local

## Project root

`python -m venv venv`

`cd api/`

`source venv/Script/activate`

`uvicorn main:app --reload`

# Docker

## Requirements

- Docker
- Docker Compose

## Project Structure

- **`web`**: Main service running the FastAPI application.
- **`db`**: PostgreSQL database service.
- **`adminer`**: Adminer service for PostgreSQL database management.

## Commands

### Start the Application

`docker-compose up -d`

### Stop the Application

`docker-compose down`

## Accessing the Application

Una vez que los contenedores estén en ejecución, puedes acceder a las siguientes rutas:

- API Documentation: [Swagger UI](http://localhost:8000/docs) - Here you can view and test the API endpoints.
- Database Administrator: [Adminer](http://localhost:8080) - Here you can manage the PostgreSQL database, using the credentials found in the docker-compose file.

## Health Check

- [health-check/database](http://localhost:8000/health-check/database): Reports the database status
