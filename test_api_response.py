import requests
import json

def test_api_endpoint():
    base_url = 'https://advertisement-management-api-91xh.onrender.com'
    endpoint = '/jobs/'
    url = base_url.rstrip('/') + endpoint
    
    print(f"Testing API endpoint: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print("Response Headers:", json.dumps(dict(response.headers), indent=2))
        
        try:
            data = response.json()
            print("Response JSON:")
            print(json.dumps(data, indent=2))
            
            # Check the structure
            if isinstance(data, list):
                print("\nResponse is a list. Length:", len(data))
                if data:
                    print("First item keys:", list(data[0].keys()))
            elif isinstance(data, dict):
                print("\nResponse is a dictionary. Keys:", list(data.keys()))
                if 'results' in data:
                    print("'results' is in the response")
                if 'data' in data:
                    print("'data' is in the response")
                if 'jobs' in data:
                    print("'jobs' is in the response")
            
            return data
            
        except json.JSONDecodeError:
            print("Response is not JSON:")
            print(response.text[:1000])
            return {"error": "Non-JSON response", "content": response.text[:1000]}
            
    except requests.exceptions.RequestException as e:
        error_msg = f"Request failed: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_msg += f"\nStatus code: {e.response.status_code}"
            try:
                error_msg += f"\nResponse: {e.response.text}"
            except:
                pass
        print(error_msg)
        return {"error": str(e), "status_code": getattr(e.response, 'status_code', None)}

if __name__ == "__main__":
    result = test_api_endpoint()
    print("\nTest completed.")
