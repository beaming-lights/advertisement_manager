import os

class Config:
    # API Configuration
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://advertisement-management-api-91xh.onrender.com')
    
    # Authentication
    AUTH_TOKEN_KEY = 'auth_token'
    
    # API Endpoints - updated to use working endpoints
    class Endpoints:
        # Advert endpoints (using the working /jobs/ endpoint instead of /adverts/)
        ADVERTS = "/jobs/"
        ADVERT_DETAIL = "/jobs/{id}/"  # Assuming this is the correct endpoint pattern
        ADVERT_CREATE = "/jobs/create/"  # Update this if different
        ADVERT_UPDATE = "/jobs/{id}/update/"  # Update this if different
        ADVERT_DELETE = "/jobs/{id}/delete/"  # Update this if different
        
        # Job endpoints
        JOBS = '/api/jobs/'
        
        # Authentication endpoints
        LOGIN = '/auth/login/'
        REGISTER = '/auth/register/'
        LOGOUT = '/auth/logout/'
        
        # User endpoints
        USERS = '/api/v1/users/'
        PROFILE = "/api/v1/auth/profile/"
        
        # Job endpoints (confirmed working)
        JOBS_WORKING = "/jobs/"
        JOB_DETAIL = "/jobs/{id}/"  # Assuming this is the correct endpoint pattern
        
        # User endpoints
        USERS = '/api/v1/users/'
        
        # Company endpoints (if needed)
        COMPANIES = '/companies/'
        
        # Event endpoints (if needed)
        EVENTS = '/events/'
        
        # Legacy endpoint variations (kept for backward compatibility)
        API_JOBS = '/api/jobs/'
        LEGACY_JOBS = '/api/jobs/'
        LEGACY_AUTH = '/api/auth/'
        LEGACY_USERS = '/api/users/'
        AUTH = '/auth/'
        API_AUTH = '/api/v1/auth/'
        API_USERS = '/api/v1/users/'

# Create a config instance
config = Config()
