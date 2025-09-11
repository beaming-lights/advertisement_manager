import requests
import json
from typing import Dict, List, Any, Optional
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
        """
        Post a new job listing to the advertisement management API.
        
        Args:
            job_data: Dictionary containing job details with the following keys:
                - title: Job title (required)
                - description: Job description (required)
                - company: Company name (required)
                - location: Job location (required)
                - salary_min: Minimum salary (optional)
                - salary_max: Maximum salary (optional)
                - job_type: Type of job (e.g., 'Full-time', 'Part-time')
                - requirements: Job requirements (optional)
                - benefits: Job benefits (optional)
                - contact_email: Contact email (optional)
                - application_url: URL to apply (optional)
        """
        # Use the working /jobs/ endpoint from config
        from config import Config
        endpoint = Config.Endpoints.ADVERTS.rstrip('/')
        
        # Map job data to the exact API schema format (multipart/form-data)
        from datetime import datetime
        
        # Required fields according to API schema - all values must be strings for multipart/form-data
        # Format dates properly (YYYY-MM-DD format)
        today = datetime.now().strftime('%Y-%m-%d')
        
        form_data = {
            'title': str(job_data.get('title', '')),
            'description': str(job_data.get('description', '')),
            'category': str(job_data.get('category', 'Technology')),
            'employment_type': str(job_data.get('employment_type', 'Full-time')),
            'location': str(job_data.get('location', '')),
            'salary_min': str(job_data.get('salary_min', 0)),
            'salary_max': str(job_data.get('salary_max', 0)),
            'currency': str(job_data.get('currency', 'USD')),
            'posted_by': str(job_data.get('posted_by', 'Company')),
            'date_posted': str(job_data.get('date_posted', today)),
            'application_deadline': str(job_data.get('application_deadline', today)),
            'job_status': str(job_data.get('job_status', 'Active'))
        }
        
        # Log the request
        logger.info(f"Posting job to API endpoint: {endpoint}")
        logger.debug(f"Request data: {json.dumps(form_data, indent=2, default=str)}")
        
        try:
            logger.info(f"Posting to endpoint: {endpoint}")
            
            # Try JSON first (most APIs prefer JSON)
            logger.info("Attempting JSON POST...")
            
            json_data = {
                'title': form_data['title'],
                'description': form_data['description'],
                'category': form_data['category'],
                'employment_type': form_data['employment_type'],
                'location': form_data['location'],
                'salary_min': int(form_data['salary_min']) if form_data['salary_min'] else 0,
                'salary_max': int(form_data['salary_max']) if form_data['salary_max'] else 0,
                'currency': form_data['currency'],
                'posted_by': form_data['posted_by'],
                'date_posted': form_data['date_posted'],
                'application_deadline': form_data['application_deadline'],
                'job_status': form_data['job_status'],
                'flyer': 'dummy_flyer.txt'  # Required field
            }
            
            try:
                response = self._make_request('POST', endpoint, json=json_data)
                
                if response.status_code in [200, 201]:
                    logger.info(f"JSON POST successful: {response.status_code}")
                elif response.status_code == 422:
                    logger.warning("JSON POST validation failed, trying form data...")
                    raise Exception("JSON validation failed")
                else:
                    logger.warning(f"JSON POST returned {response.status_code}, trying form data...")
                    raise Exception(f"JSON POST failed with {response.status_code}")
                    
            except Exception as json_error:
                logger.warning(f"JSON POST failed: {json_error}")
                logger.info("Trying form data POST...")
                
                # Fallback to multipart form data with actual file if available
                import io
                
                # Check if we have uploaded files from the form
                if hasattr(job_data, 'uploaded_files') and job_data.uploaded_files:
                    # Use actual uploaded file
                    uploaded_file = job_data.uploaded_files[0]
                    file_content = uploaded_file.get('content', b'dummy content')
                    file_name = uploaded_file.get('name', 'uploaded_file.txt')
                    file_type = uploaded_file.get('type', 'text/plain')
                    
                    files = {
                        'flyer': (file_name, io.BytesIO(file_content), file_type)
                    }
                else:
                    # Use dummy file as fallback
                    dummy_file = io.BytesIO(b'dummy flyer content')
                    files = {
                        'flyer': ('dummy.txt', dummy_file, 'text/plain')
                    }
                
                data = {
                    'title': form_data['title'],
                    'description': form_data['description'],
                    'category': form_data['category'],
                    'employment_type': form_data['employment_type'],
                    'location': form_data['location'],
                    'salary_min': form_data['salary_min'],
                    'salary_max': form_data['salary_max'],
                    'currency': form_data['currency'],
                    'posted_by': form_data['posted_by'],
                    'date_posted': form_data['date_posted'],
                    'application_deadline': form_data['application_deadline'],
                    'job_status': form_data['job_status']
                }
                
                logger.debug(f"Multipart data fields: {list(data.keys())}")
                logger.debug(f"Multipart files: {list(files.keys())}")
                response = self._make_request('POST', endpoint, data=data, files=files)
            
            # Log response details
            logger.info(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {dict(response.headers)}")
            
            # Handle response
            try:
                response_data = response.json()
                logger.debug(f"Response JSON: {json.dumps(response_data, indent=2)}")
            except json.JSONDecodeError:
                logger.warning(f"Non-JSON response: {response.text[:500]}")
                response_data = response.text
            
            # Check for successful response (2xx status code)
            if 200 <= response.status_code < 300:
                logger.info(f"Successfully posted job via {endpoint}")
                return {
                    'success': True,
                    'data': response_data,
                    'status_code': response.status_code
                }
            
            # Handle error responses
            error_msg = f"API returned {response.status_code} for {endpoint}"
            if hasattr(response, 'text'):
                error_msg += f": {response.text[:500]}"
            
            raise Exception(error_msg)
                
        except Exception as e:
            error_msg = f"Failed to post job: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make an HTTP request with enhanced error handling and connection management."""
        url = f"{self.base_url.rstrip('/')}{endpoint}"
        headers = self._get_headers()
        
        # Log the request details
        logger.info(f"{method.upper()} {url}")
        logger.debug(f"Request headers: {headers}")
        if 'json' in kwargs:
            logger.debug(f"Request body: {json.dumps(kwargs['json'], indent=2)}")
        if 'data' in kwargs:
            logger.debug(f"Request data: {kwargs['data']}")
        if 'files' in kwargs:
            logger.debug(f"Request files: {list(kwargs['files'].keys()) if kwargs['files'] else None}")
        
        # Remove Content-Type header for multipart/form-data to let requests set it automatically
        # Also remove other headers that might interfere with multipart
        if 'files' in kwargs or ('data' in kwargs and 'files' not in kwargs):
            headers_copy = {}
            # Only keep essential headers, remove content-type and accept headers
            if self.token:
                headers_copy["Authorization"] = f"Bearer {self.token}"
        else:
            headers_copy = headers
        
        try:
            # Make the request with better error handling
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers_copy,
                timeout=(10, 30),  # (connect timeout, read timeout)
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
            
        except requests.exceptions.ConnectionError as e:
            # Handle connection reset and similar network errors
            error_msg = f"Connection error to {url}: {str(e)}. This may be due to network issues or server unavailability."
            logger.error(error_msg)
            raise Exception(error_msg)
            
        except requests.exceptions.Timeout as e:
            error_msg = f"Request timeout to {url}: {str(e)}. The server may be slow or overloaded."
            logger.error(error_msg)
            raise Exception(error_msg)
            
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
                    error_details['response_text'] = e.response.text[:500]
                except:
                    pass
            
            error_msg = f"Request failed: {json.dumps(error_details, indent=2)}"
            logger.error(error_msg)
            raise Exception(error_msg)

    def get_job_by_id(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific job by ID from the API"""
        from config import Config
        endpoint = f"{Config.Endpoints.ADVERTS.rstrip('/')}/{job_id}"
        
        try:
            logger.info(f"Fetching job {job_id} from endpoint: {endpoint}")
            response = self._make_request('GET', endpoint)
            
            if response.status_code == 200:
                job_data = response.json()
                logger.info(f"Successfully retrieved job {job_id}")
                return job_data
            elif response.status_code == 404:
                logger.warning(f"Job {job_id} not found")
                return None
            else:
                logger.error(f"Failed to get job {job_id}: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error retrieving job {job_id}: {e}")
            return None
    
    def delete_job(self, job_id: str) -> bool:
        """
        Delete a job/event by ID.
        
        Args:
            job_id: The ID of the job/event to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            endpoint = f"{self.base_url}/jobs/{job_id}"
            response = requests.delete(
                endpoint,
                headers=self._get_headers(),
                timeout=10
            )
            
            if response.status_code == 200:
                return True
            elif response.status_code == 404:
                logger.warning(f"Job {job_id} not found for deletion")
            else:
                logger.error(f"Failed to delete job {job_id}. Status code: {response.status_code}")
            
            return False
            
        except Exception as e:
            logger.error(f"Error deleting job {job_id}: {str(e)}")
            return False
            
    def get_job_images(self, job_id: str) -> List[Dict[str, Any]]:
        """Get images/flyers for a specific job - extract from job data itself"""
        try:
            # Get the full job data which should contain image information
            job = self.get_job_by_id(job_id)
            if not job:
                logger.warning(f"No job found with ID {job_id}")
                return []
            
            images = []
            
            # Check for flyer field (Cloudinary URL)
            if job.get('flyer'):
                images.append({
                    'url': job['flyer'],
                    'type': 'flyer',
                    'name': 'Job Flyer'
                })
            
            # Check for image_url field
            if job.get('image_url'):
                images.append({
                    'url': job['image_url'],
                    'type': 'image',
                    'name': 'Job Image'
                })
            
            # Check for images array field
            if job.get('images') and isinstance(job['images'], list):
                for i, image_url in enumerate(job['images']):
                    if isinstance(image_url, str) and image_url.strip():
                        images.append({
                            'url': image_url,
                            'type': 'gallery',
                            'name': f'Image {i+1}'
                        })
            
            logger.info(f"Extracted {len(images)} images from job {job_id} data")
            return images
                
        except Exception as e:
            logger.error(f"Error extracting images for job {job_id}: {e}")
            return []

    def get_jobs(self) -> List[Dict[str, Any]]:
        """
        Get all job listings from the advertisement management API.
        
        Returns:
            List[Dict[str, Any]]: A list of job dictionaries
            
        Raises:
            Exception: If all API endpoints fail
        """
        # Use the working /jobs/ endpoint from config
        from config import Config
        endpoint = Config.Endpoints.ADVERTS.rstrip('/')
        
        try:
            logger.info(f"Fetching jobs from endpoint: {endpoint}")
            response = self._make_request('GET', endpoint)
            
            # Log response details
            logger.info(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {dict(response.headers)}")
            
            # Handle response
            try:
                response_data = response.json()
                logger.debug(f"Response JSON: {json.dumps(response_data, indent=2)}")
            except json.JSONDecodeError:
                logger.warning(f"Non-JSON response: {response.text[:500]}")
                response_data = []
            
            # Check for successful response (2xx status code)
            if 200 <= response.status_code < 300:
                logger.info(f"Successfully fetched jobs from {endpoint}")
                if isinstance(response_data, list):
                    return response_data
                else:
                    # If response is not a list, try to extract jobs from it
                    if isinstance(response_data, dict) and 'jobs' in response_data:
                        return response_data['jobs']
                    elif isinstance(response_data, dict) and 'data' in response_data:
                        return response_data['data']
                    else:
                        return []
            
            # Handle error responses
            error_msg = f"API returned {response.status_code} for {endpoint}"
            if hasattr(response, 'text'):
                error_msg += f": {response.text[:500]}"
            
            raise Exception(error_msg)
                
        except Exception as e:
            error_msg = f"Failed to fetch jobs: {str(e)}"
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
