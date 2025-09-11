#!/usr/bin/env python3
"""
Test script to check what image data the API returns
"""

import sys
import os
import json
import requests
from pprint import pprint

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config import Config
from utils.api_client import api_client

def test_api_images():
    """Test what image data the API returns"""
    print("🔍 Testing API Image Data Retrieval")
    print("=" * 50)
    
    try:
        # First, get all jobs to see what's available
        print("1. Fetching all jobs...")
        jobs = api_client.get_jobs()
        
        if not jobs:
            print("❌ No jobs found in API")
            return
        
        print(f"✅ Found {len(jobs)} jobs")
        
        # Look at the first job to see its structure
        first_job = jobs[0]
        print(f"\n2. Examining first job structure:")
        print(f"Job ID: {first_job.get('id', 'N/A')}")
        print(f"Title: {first_job.get('title', 'N/A')}")
        
        # Check for image-related fields
        image_fields = ['flyer', 'image_url', 'images', 'image', 'photo', 'picture']
        print(f"\n3. Checking for image fields in job data:")
        
        for field in image_fields:
            if field in first_job:
                value = first_job[field]
                print(f"   ✅ {field}: {type(value)} = {str(value)[:100]}...")
            else:
                print(f"   ❌ {field}: Not found")
        
        # Print all fields to see what's available
        print(f"\n4. All available fields in job:")
        for key, value in first_job.items():
            print(f"   {key}: {type(value)} = {str(value)[:50]}...")
        
        # Test getting individual job details
        job_id = first_job.get('id')
        if job_id:
            print(f"\n5. Testing individual job retrieval for ID: {job_id}")
            try:
                individual_job = api_client.get_job_by_id(str(job_id))
                if individual_job:
                    print("✅ Individual job retrieved successfully")
                    
                    # Check if individual job has more image data
                    print("   Image fields in individual job:")
                    for field in image_fields:
                        if field in individual_job:
                            value = individual_job[field]
                            print(f"   ✅ {field}: {type(value)} = {str(value)[:100]}...")
                else:
                    print("❌ Failed to retrieve individual job")
            except Exception as e:
                print(f"❌ Error retrieving individual job: {e}")
        
        # Test the get_job_images method
        print(f"\n6. Testing get_job_images method:")
        try:
            images = api_client.get_job_images(str(job_id))
            if images:
                print(f"✅ Found {len(images)} images via get_job_images")
                for i, img in enumerate(images):
                    print(f"   Image {i+1}: {type(img)} = {str(img)[:100]}...")
            else:
                print("❌ No images found via get_job_images")
        except Exception as e:
            print(f"❌ Error with get_job_images: {e}")
        
    except Exception as e:
        print(f"❌ Error testing API: {e}")
        import traceback
        traceback.print_exc()

def test_direct_api_call():
    """Test direct API calls to see raw response"""
    print("\n" + "=" * 50)
    print("🔗 Testing Direct API Calls")
    print("=" * 50)
    
    base_url = Config.API_BASE_URL
    jobs_endpoint = f"{base_url}/jobs/"
    
    try:
        print(f"Making direct request to: {jobs_endpoint}")
        response = requests.get(jobs_endpoint, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response type: {type(data)}")
            
            if isinstance(data, list) and len(data) > 0:
                first_job = data[0]
                print(f"\nFirst job raw data:")
                pprint(first_job, width=100, depth=3)
            elif isinstance(data, dict):
                print(f"\nResponse data:")
                pprint(data, width=100, depth=3)
        else:
            print(f"Error response: {response.text}")
            
    except Exception as e:
        print(f"❌ Direct API call failed: {e}")

if __name__ == "__main__":
    test_api_images()
    test_direct_api_call()
