import os

class Config:
    # API Configuration
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://advertisement-management-api-91xh.onrender.com')
    
    # Authentication
    AUTH_TOKEN_KEY = 'auth_token'
    
    # API Endpoints - using the working /jobs/ endpoint as primary
    class Endpoints:
        # Primary endpoints (working)
        JOBS = '/jobs/'
        AUTH = '/auth/'
        USERS = '/users/'
        
        # Alternative endpoint variations (kept for reference)
        API_JOBS = '/api/v1/jobs/'
        API_AUTH = '/api/v1/auth/'
        API_USERS = '/api/v1/users/'
        
        # Legacy endpoint variations (kept for backward compatibility)
        LEGACY_JOBS = '/api/jobs/'
        LEGACY_AUTH = '/api/auth/'
        LEGACY_USERS = '/api/users/'

# Create a config instance
config = Config()
