import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_api_endpoint():
    base_url = 'https://advertisement-management-api-91xh.onrender.com'
    endpoint = '/api/jobs/'
    url = base_url.rstrip('/') + endpoint
    
    logger.info(f"Testing API endpoint: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Headers: {response.headers}")
        
        try:
            data = response.json()
            logger.info(f"Response JSON: {data}")
            return data
        except ValueError:
            logger.warning(f"Non-JSON response: {response.text[:500]}")
            return {"error": "Non-JSON response", "content": response.text[:500]}
            
    except requests.exceptions.RequestException as e:
        error_msg = f"Request failed: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_msg += f"\nStatus code: {e.response.status_code}"
            try:
                error_msg += f"\nResponse: {e.response.text}"
            except:
                pass
        logger.error(error_msg)
        return {"error": str(e), "status_code": getattr(e.response, 'status_code', None)}

if __name__ == "__main__":
    result = test_api_endpoint()
    print("\nTest Result:")
    print("-" * 50)
    print(f"Status: {'SUCCESS' if 'error' not in result else 'FAILED'}")
    if 'error' in result:
        print(f"Error: {result['error']}")
        if 'status_code' in result and result['status_code']:
            print(f"Status Code: {result['status_code']}")
