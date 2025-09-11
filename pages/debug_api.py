from nicegui import ui
from components.header import show_header
from utils.api_client import api_client
import json

def show_debug_api_page():
    """Debug page to inspect API responses and image data"""
    show_header()
    
    with ui.column().classes('max-w-6xl mx-auto p-6'):
        ui.label('API Debug - Image Data Inspector').classes('text-3xl font-bold mb-6')
        
        # Test API connection
        with ui.card().classes('p-6 mb-6'):
            ui.label('API Connection Test').classes('text-xl font-bold mb-4')
            
            with ui.row().classes('gap-4 mb-4'):
                ui.button('Test Get Jobs', on_click=test_get_jobs).classes('bg-blue-600 text-white')
                ui.button('Test Individual Job', on_click=test_individual_job).classes('bg-green-600 text-white')
                ui.button('Test Job Images', on_click=test_job_images).classes('bg-purple-600 text-white')
            
            # Results area
            global results_container
            results_container = ui.column().classes('mt-4')

def test_get_jobs():
    """Test getting all jobs and display results"""
    results_container.clear()
    
    with results_container:
        ui.label('Testing get_jobs()...').classes('text-lg font-semibold mb-2')
        
        try:
            jobs = api_client.get_jobs()
            
            if jobs:
                ui.label(f'✅ Found {len(jobs)} jobs').classes('text-green-600 mb-4')
                
                # Show first job in detail
                first_job = jobs[0]
                ui.label('First Job Data:').classes('font-semibold mb-2')
                
                with ui.card().classes('p-4 bg-gray-50'):
                    # Display all fields
                    for key, value in first_job.items():
                        with ui.row().classes('mb-2'):
                            ui.label(f'{key}:').classes('font-medium w-32')
                            if key in ['flyer', 'image_url', 'images', 'image']:
                                ui.label(str(value)).classes('text-blue-600 break-all')
                            else:
                                ui.label(str(value)[:100] + ('...' if len(str(value)) > 100 else ''))
                
                # Try to display any images found
                image_fields = ['flyer', 'image_url', 'images', 'image']
                for field in image_fields:
                    if first_job.get(field):
                        ui.label(f'Found image in field: {field}').classes('text-green-600 font-semibold mt-4')
                        
                        # Try to display the image
                        try:
                            image_value = first_job[field]
                            if isinstance(image_value, str) and image_value.startswith('http'):
                                with ui.card().classes('p-4 mt-2'):
                                    ui.label(f'Image URL: {image_value}').classes('mb-2')
                                    ui.image(image_value).classes('max-w-md')
                            elif isinstance(image_value, list):
                                ui.label(f'Multiple images found: {len(image_value)}').classes('mb-2')
                                for i, img_url in enumerate(image_value):
                                    if isinstance(img_url, str) and img_url.startswith('http'):
                                        with ui.card().classes('p-4 mt-2'):
                                            ui.label(f'Image {i+1}: {img_url}').classes('mb-2')
                                            ui.image(img_url).classes('max-w-md')
                        except Exception as e:
                            ui.label(f'Error displaying image: {e}').classes('text-red-600')
            else:
                ui.label('❌ No jobs found').classes('text-red-600')
                
        except Exception as e:
            ui.label(f'❌ Error: {str(e)}').classes('text-red-600')

def test_individual_job():
    """Test getting individual job details"""
    results_container.clear()
    
    with results_container:
        ui.label('Testing get_job_by_id()...').classes('text-lg font-semibold mb-2')
        
        try:
            # First get a job ID
            jobs = api_client.get_jobs()
            if not jobs:
                ui.label('❌ No jobs available to test').classes('text-red-600')
                return
            
            job_id = jobs[0].get('id')
            if not job_id:
                ui.label('❌ No job ID found').classes('text-red-600')
                return
            
            ui.label(f'Testing with Job ID: {job_id}').classes('mb-2')
            
            job = api_client.get_job_by_id(str(job_id))
            
            if job:
                ui.label('✅ Individual job retrieved successfully').classes('text-green-600 mb-4')
                
                with ui.card().classes('p-4 bg-gray-50'):
                    ui.label('Individual Job Data:').classes('font-semibold mb-2')
                    
                    # Show raw JSON
                    ui.code(json.dumps(job, indent=2, default=str)).classes('text-xs bg-white p-2 rounded max-h-96 overflow-auto')
                
                # Check for images
                image_fields = ['flyer', 'image_url', 'images', 'image']
                for field in image_fields:
                    if job.get(field):
                        ui.label(f'✅ Image field found: {field} = {job[field]}').classes('text-green-600 mt-2')
            else:
                ui.label('❌ Failed to retrieve individual job').classes('text-red-600')
                
        except Exception as e:
            ui.label(f'❌ Error: {str(e)}').classes('text-red-600')

def test_job_images():
    """Test the get_job_images method"""
    results_container.clear()
    
    with results_container:
        ui.label('Testing get_job_images()...').classes('text-lg font-semibold mb-2')
        
        try:
            # First get a job ID
            jobs = api_client.get_jobs()
            if not jobs:
                ui.label('❌ No jobs available to test').classes('text-red-600')
                return
            
            job_id = jobs[0].get('id')
            if not job_id:
                ui.label('❌ No job ID found').classes('text-red-600')
                return
            
            ui.label(f'Testing get_job_images() with Job ID: {job_id}').classes('mb-2')
            
            images = api_client.get_job_images(str(job_id))
            
            if images:
                ui.label(f'✅ Found {len(images)} images via get_job_images()').classes('text-green-600 mb-4')
                
                for i, img in enumerate(images):
                    with ui.card().classes('p-4 mb-2 bg-gray-50'):
                        ui.label(f'Image {i+1}:').classes('font-semibold mb-2')
                        ui.code(json.dumps(img, indent=2, default=str)).classes('text-xs bg-white p-2 rounded')
            else:
                ui.label('❌ No images found via get_job_images()').classes('text-red-600')
                
        except Exception as e:
            ui.label(f'❌ Error: {str(e)}').classes('text-red-600')

# Global variable for results container
results_container = None
