from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
import os
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.middleware import RequestLoggingMiddleware, ExceptionHandlingMiddleware
from app.routers import auth, repositories, test_generation, test_generation

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Test Case Generator API")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Frontend URL: {settings.FRONTEND_URL}")
    yield
    # Shutdown
    logger.info("Shutting down Test Case Generator API")

app = FastAPI(
    title="Test Case Generator API",
    description="API for generating test cases from GitHub repositories using AI",
    version="1.0.0",
    docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
    lifespan=lifespan
)

# Add custom middleware (order matters!)
app.add_middleware(ExceptionHandlingMiddleware)
app.add_middleware(RequestLoggingMiddleware)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=settings.ALLOWED_HOSTS
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Test Case Generator API is running",
        "version": "1.0.0",
        "docs": "/docs" if settings.ENVIRONMENT == "development" else "disabled",
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    
    # Basic health checks
    health_status = {
        "status": "healthy",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
    # Add configuration status (without sensitive data)
    config_status = {
        "github_configured": bool(settings.GITHUB_CLIENT_ID),
        "openai_configured": bool(settings.OPENAI_API_KEY),
        "jwt_configured": settings.JWT_SECRET_KEY != "your-secret-key-change-in-production"
    }
    
    health_status["configuration"] = config_status
    
    return health_status

# Include routers
app.include_router(auth.router, prefix="/api")
app.include_router(repositories.router, prefix="/api")

# Import and include test generation router
from app.routers import test_generation
app.include_router(test_generation.router, prefix="/api")
app.include_router(test_generation.router, prefix="/api")
app.include_router(test_generation.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.ENVIRONMENT == "development",
        log_level="info"
    )