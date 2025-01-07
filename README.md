# FastAPI Template

## Project Description
This is a FastAPI project template with a scalable and clean architecture, designed to help you quickly start building production-ready applications. It provides a set of common features like user authentication, secure password handling, Google login integration, and flexible user management, making it easy to integrate additional functionalities and scale your project.

### Features:

- **User authentication and management**\
Provides a complete user management system with secure registration, login, password change functionality, and Google login integration via OAuth2. Users can also upload and update their profile images, with support for managing user activity status.

- **Profile Image Upload and Management**\
Users can upload, update, and delete their profile images. Images are stored securely in AWS S3 with validation and public access URL generation.

- **Database Migrations with Alembic**\
Seamlessly manage database schema changes and migrations using Alembic.

- **Scalable API Structure**\
Versioned API endpoints (api/v1) for better scalability and easier maintenance.

- **Secure Password Handling and Encryption**\
Passwords are securely hashed and encrypted for storage and retrieval.

- **Data Validation with Pydantic**\
Ensures that the input and output data conform to the expected formats using Pydantic models.

- **Simple and Extensible Service Layer**\
A service layer that handles the business logic, allowing for easy maintenance and extensibility.

### Technologies Used:

- **FastAPI**\
A high-performance web framework for building APIs with Python 3.7+

- **Uvicorn**\
ASGI server for running FastAPI applications

- **Pydantic**\
Data validation and settings management using Python type annotations.

- **Alembic**\
A database migration tool for SQLAlchemy.

- **SQLAlchemy**\
ORM (Object Relational Mapper) for database interaction.

- **OAuth2**\
Secure login system with Google OAuth2 integration.

- **AWS S3 Integration**\
Profile images are securely uploaded and managed using AWS S3, with support for file validation and public URL generation.
