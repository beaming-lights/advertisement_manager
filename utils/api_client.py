import requests
import json
from typing import Dict, Any, Optional
from config import config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self):
        self.base_url = config.API_BASE_URL
        self.token = None

    def set_token(self, token: str):
        """Set the authentication token for API requests."""
        self.token = token

    def _get_headers(self) -> Dict[str, str]:
        """Get headers with authentication and CORS support."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            # CORS headers
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def post_job(self, job_data: Dict[str, Any]) -> Dict[str, Any]:
        """Post a new job listing with enhanced error handling and logging."""
        # Try different endpoint variations
        endpoints_to_try = [
            config.Endpoints.JOBS,      # /jobs/
            config.Endpoints.API_JOBS,  # /api/v1/jobs/
            '/api/jobs/'               # Fallback
        ]
        
        last_error = None
        
        print(f"Attempting to post job to API. Endpoints to try: {endpoints_to_try}")
        print(f"Job data being sent: {json.dumps(job_data, indent=2)}")
        
        for endpoint in endpoints_to_try:
            try:
                print(f"Trying endpoint: {endpoint}")
                response = self._make_request('POST', endpoint, json=job_data)
                
                # Log the raw response for debugging
                print(f"Response status: {response.status_code}")
                print(f"Response headers: {dict(response.headers)}")
                
                try:
                    response_data = response.json()
                    print(f"Response JSON: {json.dumps(response_data, indent=2)}")
                except json.JSONDecodeError:
                    print(f"Non-JSON response: {response.text[:500]}")
                    response_data = response.text
                
                # Check for successful response
                if 200 <= response.status_code < 300:
                    print(f"Successfully posted job via {endpoint}")
                    return response_data
                else:
                    error_msg = f"API returned {response.status_code} for {endpoint}"
                    if hasattr(response, 'text'):
                        error_msg += f": {response.text[:500]}"
                    raise Exception(error_msg)
                    
            except Exception as e:
                last_error = e
                error_msg = f"Failed with endpoint {endpoint}: {str(e)}"
                logger.warning(error_msg)
                print(error_msg)
                continue
        
        # If we get here, all endpoints failed
        error_msg = f"Failed to post job. All endpoint variations failed. Last error: {str(last_error)}"
        logger.error(error_msg)
        print(error_msg)
        raise Exception(error_msg)

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make an HTTP request with CORS support and enhanced error handling."""
        url = f"{self.base_url.rstrip('/')}{endpoint}"
        headers = self._get_headers()
        
        # Log the request details
        logger.info(f"{method.upper()} {url}")
        logger.debug(f"Request headers: {headers}")
        if 'json' in kwargs:
            logger.debug(f"Request body: {json.dumps(kwargs['json'], indent=2)}")
        
        try:
            # First, handle OPTIONS preflight if needed
            if method.upper() == 'POST':
                try:
                    preflight = requests.options(
                        url,
                        headers={
                            'Access-Control-Request-Method': 'POST',
                            'Origin': 'http://localhost:8080'  # Update with your frontend URL if different
                        },
                        timeout=5
                    )
                    logger.debug(f"Preflight response: {preflight.status_code}")
                    logger.debug(f"Preflight headers: {dict(preflight.headers)}")
                except Exception as e:
                    logger.warning(f"Preflight check failed: {str(e)}")
            
            # Make the actual request
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                timeout=30,  # Increased timeout for slow connections
                **kwargs
            )
            
            # Log response details
            logger.info(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {dict(response.headers)}")
            
            # Log response body for debugging
            try:
                response_data = response.json()
                logger.debug(f"Response data: {json.dumps(response_data, indent=2)}")
            except ValueError:
                logger.warning(f"Non-JSON response: {response.text[:500]}")
            
            return response
            
        except requests.exceptions.RequestException as e:
            error_details = {
                'error': str(e),
                'type': type(e).__name__,
                'url': url,
                'method': method
            }
            
            if hasattr(e, 'response') and e.response is not None:
                error_details['status_code'] = e.response.status_code
                try:
                    error_details['response_headers'] = dict(e.response.headers)
                    error_details['response_text'] = e.response.text[:1000]  # First 1000 chars
                except:
                    pass
            
            error_msg = f"Request failed: {json.dumps(error_details, indent=2)}"
            logger.error(error_msg)
            raise Exception(error_msg)

    def get_jobs(self) -> Dict[str, Any]:
        """Get all job listings. Tries multiple endpoint variations."""
        # List of endpoint variations to try
        endpoints_to_try = [
            config.Endpoints.JOBS,      # /jobs/
            config.Endpoints.API_JOBS,  # /api/v1/jobs/
            '/api/jobs/'               # Fallback
        ]
        
        last_error = None
        
        for endpoint in endpoints_to_try:
            try:
                logger.info(f"Trying endpoint: {endpoint}")
                response = self._make_request('GET', endpoint)
                response.raise_for_status()
                
                # Get the response data
                response_data = response.json()
                logger.info(f"Response from {endpoint}: {json.dumps(response_data, indent=2)[:500]}...")  # Log first 500 chars
                
                # If response is a list, return it directly
                if isinstance(response_data, list):
                    return response_data
                    
                # If response is a dict with a results/data key, return that
                if isinstance(response_data, dict):
                    if 'results' in response_data:
                        return response_data['results']
                    elif 'data' in response_data:
                        return response_data['data']
                    elif 'jobs' in response_data:
                        return response_data['jobs']
                    # If no standard key, return the entire response
                    return response_data
                    
                # If we get here, the response format is unexpected
                logger.warning(f"Unexpected response format from {endpoint}")
                return response_data
                
            except Exception as e:
                last_error = e
                logger.warning(f"Failed with endpoint {endpoint}: {str(e)}")
                continue
        
        # If we get here, all endpoints failed
        error_msg = f"All endpoint variations failed. Last error: {str(last_error)}"
        logger.error(error_msg)
        raise Exception(error_msg)

    def get_job(self, job_id: str) -> Dict[str, Any]:
        """Get a specific job listing by ID."""
        # List of endpoint variations to try
        endpoints_to_try = [
            f"{config.Endpoints.API_JOBS.rstrip('/')}/{job_id}/",  # /api/v1/jobs/{id}/
            f"{config.Endpoints.JOBS.rstrip('/')}/{job_id}/",      # /jobs/{id}/
            f"/api/jobs/{job_id}/"                                # Fallback
        ]
        
        last_error = None
        
        for endpoint in endpoints_to_try:
            try:
                response = self._make_request('GET', endpoint)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                last_error = e
                logger.warning(f"Failed with endpoint {endpoint}: {str(e)}")
                continue
        
        # If we get here, all endpoints failed
        error_msg = f"Failed to fetch job {job_id}. All endpoint variations failed. Last error: {str(last_error)}"
        logger.error(error_msg)
        raise Exception(error_msg)

# Global API client instance
api_client = ApiClient()
