import requests
import json

def test_api():
    try:
        url = "https://advertisement-management-api-91xh.onrender.com/jobs/"
        print(f"Testing API: {url}")
        
        response = requests.get(url, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data)} jobs")
            
            if data:
                job = data[0]
                print(f"\nFirst job fields:")
                for key, value in job.items():
                    print(f"  {key}: {str(value)[:100]}...")
                    
                # Check specifically for image fields
                image_fields = ['flyer', 'image_url', 'images', 'image']
                print(f"\nImage fields:")
                for field in image_fields:
                    if field in job:
                        print(f"  ✓ {field}: {job[field]}")
                    else:
                        print(f"  ✗ {field}: not found")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
