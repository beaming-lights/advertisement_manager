#!/usr/bin/env python3

import requests
import json
from config import Config

def test_api_connection():
    """Test API connection and endpoints"""
    base_url = Config.API_BASE_URL
    print(f"Testing API connection to: {base_url}")
    
    # Test 1: Basic connectivity
    print("\n=== Test 1: Basic Connectivity ===")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"Root endpoint: {response.status_code}")
    except Exception as e:
        print(f"Root endpoint failed: {e}")
    
    # Test 2: Jobs endpoint GET
    print("\n=== Test 2: GET /jobs ===")
    try:
        response = requests.get(f"{base_url}/jobs", timeout=10)
        print(f"GET /jobs: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.text[:200]}...")
    except Exception as e:
        print(f"GET /jobs failed: {e}")
    
    # Test 3: Alternative endpoints
    endpoints = ["/jobs/", "/api/jobs", "/api/jobs/", "/advertisements", "/api/advertisements"]
    print("\n=== Test 3: Alternative Endpoints ===")
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
            print(f"GET {endpoint}: {response.status_code}")
        except Exception as e:
            print(f"GET {endpoint} failed: {e}")
    
    # Test 4: POST with minimal data
    print("\n=== Test 4: POST Test ===")
    test_data = {
        "title": "Test Job",
        "description": "Test Description",
        "category": "Technology",
        "employment_type": "Full-time",
        "location": "Remote",
        "salary_min": "50000",
        "salary_max": "80000",
        "currency": "USD",
        "posted_by": "Test Company",
        "date_posted": "2024-01-01",
        "application_deadline": "2024-12-31",
        "job_status": "Active"
    }
    
    # Try different POST approaches
    endpoints_to_test = ["/jobs", "/jobs/", "/api/jobs", "/api/jobs/"]
    
    for endpoint in endpoints_to_test:
        print(f"\n--- Testing POST {endpoint} ---")
        
        # Try JSON
        try:
            response = requests.post(
                f"{base_url}{endpoint}",
                json=test_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            print(f"JSON POST {endpoint}: {response.status_code}")
            if response.text:
                print(f"Response: {response.text[:200]}...")
        except Exception as e:
            print(f"JSON POST {endpoint} failed: {e}")
        
        # Try form data
        try:
            response = requests.post(
                f"{base_url}{endpoint}",
                data=test_data,
                timeout=10
            )
            print(f"Form POST {endpoint}: {response.status_code}")
            if response.text:
                print(f"Response: {response.text[:200]}...")
        except Exception as e:
            print(f"Form POST {endpoint} failed: {e}")

if __name__ == "__main__":
    test_api_connection()
