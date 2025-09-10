import urllib.request
import urllib.error
import json

def test_api():
    url = "https://advertisement-management-api-91xh.onrender.com/api/jobs/"
    print(f"Testing URL: {url}")
    
    try:
        # Create a request with a custom User-Agent
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0',
                'Accept': 'application/json'
            }
        )
        
        # Make the request
        with urllib.request.urlopen(req) as response:
            data = response.read()
            encoding = response.info().get_param('charset', 'utf-8')
            print(f"Status: {response.status}")
            print("Headers:")
            for header, value in response.getheaders():
                print(f"  {header}: {value}")
            
            try:
                # Try to parse as JSON
                json_data = json.loads(data.decode(encoding))
                print("\nResponse JSON:")
                print(json.dumps(json_data, indent=2))
            except json.JSONDecodeError:
                print("\nResponse (not JSON):")
                print(data.decode(encoding))
                
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        print("Response:")
        print(e.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_api()
