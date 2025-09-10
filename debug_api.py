import requests
import sys

def test_endpoint(url):
    print(f"Testing URL: {url}")
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print("Headers:", response.headers)
        
        # Try to get JSON response
        try:
            data = response.json()
            print("\nJSON Response:")
            print(data)
            return data
        except ValueError:
            print("\nResponse is not JSON")
            print("Response content:")
            print(response.text[:1000])  # Print first 1000 chars of non-JSON response
            return response.text
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return str(e)

if __name__ == "__main__":
    base_url = "https://advertisement-management-api-91xh.onrender.com"
    endpoints = [
        "/jobs/",
        "/api/v1/jobs/",
        "/api/jobs/"
    ]
    
    for endpoint in endpoints:
        url = f"{base_url.rstrip('/')}{endpoint}"
        print("\n" + "="*80)
        print(f"Testing endpoint: {endpoint}")
        print("="*80)
        test_endpoint(url)
    
    print("\nTest completed.")
    
    # Write output to file
    with open("api_test_output.txt", "w") as f:
        import io
        import contextlib
        
        # Redirect stdout to capture all output
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            for endpoint in endpoints:
                url = f"{base_url.rstrip('/')}{endpoint}"
                print("\n" + "="*80)
                print(f"Testing endpoint: {endpoint}")
                print("="*80)
                test_endpoint(url)
        
        # Write to file
        f.write(temp_stdout.getvalue())
    
    print("\nOutput saved to api_test_output.txt")
