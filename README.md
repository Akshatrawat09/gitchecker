# Test Case Generator

An AI-powered application that integrates with GitHub to automatically generate test cases for your code repositories.

## Features

- 🔐 GitHub OAuth authentication
- 📁 Repository and file browsing
- 🤖 AI-powered test case generation
- 📝 Multiple testing framework support (Jest, JUnit, pytest, Selenium)
- ✏️ Code editing with syntax highlighting
- 🔄 Pull request creation for generated tests

## Tech Stack

**Frontend:**
- React 18 with TypeScript
- Material-UI for components
- Monaco Editor for code display
- React Query for state management

**Backend:**
- Python FastAPI
- GitHub API integration
- OpenAI API for test generation
- JWT authentication

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker (optional)

### Environment Setup

1. Clone the repository
2. Copy environment files:
   ```bash
   cp backend/.env.example backend/.env
   ```
3. Configure your environment variables in `backend/.env`:
   - GitHub OAuth credentials (get from GitHub Developer Settings)
   - OpenAI API key (get from OpenAI Platform)
   - JWT secret key (generate a secure random string)

⚠️ **Security Note**: Never commit API keys to version control. The `.env` file is already in `.gitignore`.

### Development with Docker

```bash
# Start all services
docker-compose up --build

# Frontend will be available at http://localhost:3000
# Backend API at http://localhost:8000
```

#+## Manual Development Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request
