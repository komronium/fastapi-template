# FastAPI Template

Production-ready FastAPI template with clean architecture and JWT authentication.

## Features

- ✅ JWT Authentication
- ✅ SQLAlchemy + PostgreSQL
- ✅ Clean Architecture
- ✅ Pydantic Validation
- ✅ Docker Support
- ✅ Unit Tests
- ✅ API Documentation

## Project Structure

```bash
📦 app/
├── 📂 api/                # API endpoints
│   └── 📂 v1/
├── 📂 core/              # Core configurations
├── 📂 db/                # Database setup
├── 📂 models/            # SQLAlchemy models
├── 📂 schemas/           # Pydantic schemas
├── 📂 services/          # Business logic
└── 📂 tests/             # Unit tests
```

## Quick Start

### Using Docker

```bash
# Clone repository
git clone https://github.com/yourusername/fastapi-template.git

# Setup environment
copy .env.example .env

# Run with Docker
docker-compose up -d
```

### Local Development

```bash
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```
