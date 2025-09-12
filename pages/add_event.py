from nicegui import ui
from utils.api_client import api_client
import requests
from config import Config
from datetime import datetime
from components.header import show_header
from components.footer import show_footer

def show_add_event_page():
    """Post job page with exact API schema matching"""
    
    # Add header
    show_header()
    
    # Hero section for post job page with background image
    with ui.column().classes('w-full relative text-white py-24 px-4'):
        # Background image with overlay
        with ui.element('div').classes('absolute inset-0 -z-10'):
            ui.image('https://images.pexels.com/photos/3184419/pexels-photo-3184419.jpeg') \
                .classes('w-full h-full object-cover')
            ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-blue-900/90 to-indigo-800/90')
        
        # Hero content
        with ui.column().classes('w-full max-w-7xl mx-auto text-center relative z-10'):
            ui.label('Post a New Job').classes('text-4xl md:text-5xl font-bold mb-4')
            ui.label('Reach qualified candidates and find your next great hire').classes('text-xl text-blue-100')
    
    # Main content container
    with ui.column().classes('w-full max-w-7xl mx-auto px-4 py-12'):
        with ui.card().classes('w-full max-w-2xl mx-auto p-8 -mt-16 relative z-10 shadow-xl'):
            ui.label('Job Details - API Schema').classes('text-xl font-bold mb-6')
            
            # Exact API required fields
            title = ui.input('title *', placeholder='Job title as expected by API').classes('w-full mb-4')
            description = ui.textarea('description *', placeholder='Job description text').classes('w-full mb-4')
            
            with ui.row().classes('w-full gap-4 mb-4'):
                category = ui.select(['Technology', 'Healthcare', 'Finance', 'Education', 'Marketing', 'Sales'], 
                                    value='Technology', label='category *').classes('flex-1')
                employment_type = ui.select(['Full-time', 'Part-time', 'Contract', 'Freelance', 'Internship'], 
                                        value='Full-time', label='employment_type *').classes('flex-1')
        
            location = ui.input('location *', placeholder='Job location').classes('w-full mb-4')
            
            with ui.row().classes('w-full gap-4 mb-4'):
                salary_min = ui.number('salary_min *', value=0, format='%.0f').classes('flex-1')
                salary_max = ui.number('salary_max *', value=0, format='%.0f').classes('flex-1')
            
            currency = ui.select(['USD', 'EUR', 'GBP', 'CAD', 'AUD'], value='USD', label='currency *').classes('w-full mb-4')
            posted_by = ui.input('posted_by *', placeholder='Company or person posting').classes('w-full mb-4')
            
            with ui.row().classes('w-full gap-4 mb-4'):
                from datetime import datetime
                today = datetime.now().strftime('%Y-%m-%d')
                date_posted = ui.input('date_posted * (YYYY-MM-DD)', value=today).classes('flex-1')
                application_deadline = ui.input('application_deadline * (YYYY-MM-DD)', value=today).classes('flex-1')
            
            job_status = ui.select(['Active', 'Closed', 'Draft'], value='Active', label='job_status *').classes('w-full mb-4')
            
            # File upload section (required by API)
            ui.label("flyer * (Required by API)").classes('text-lg font-semibold mb-2')
            uploaded_files = []
            
            def handle_upload(e):
                uploaded_files.clear()
                uploaded_files.extend(e.content.get('files', []))
                ui.notify(f'✅ {len(uploaded_files)} file(s) uploaded', type='positive')
            
            ui.upload(on_upload=handle_upload, multiple=False).props('accept="*/*"').classes('w-full mb-6')
            
            # Submit button
            ui.button('Post Job to API', 
                    on_click=lambda: submit_job(title, description, category, employment_type, 
                                              location, salary_min, salary_max, currency, 
                                              posted_by, date_posted, application_deadline, 
                                              job_status, uploaded_files)).classes('bg-blue-600 text-white px-8 py-3 hover:bg-blue-700 transition-colors')
    
    # Add footer
    show_footer()

def submit_job(title, description, category, employment_type, location, salary_min, salary_max, currency, posted_by, date_posted, application_deadline, job_status, uploaded_files):
    """Submit job to API with exact field mapping matching API schema"""
    # Validate all required fields according to API schema
    required_fields = [
        (title, 'title'),
        (description, 'description'), 
        (category, 'category'),
        (employment_type, 'employment_type'),
        (location, 'location'),
        (salary_min, 'salary_min'),
        (salary_max, 'salary_max'),
        (currency, 'currency'),
        (posted_by, 'posted_by'),
        (date_posted, 'date_posted'),
        (application_deadline, 'application_deadline'),
        (job_status, 'job_status')
    ]
    
    missing_fields = []
    for field, name in required_fields:
        if not field.value or (isinstance(field.value, (int, float)) and field.value == 0):
            missing_fields.append(name)
    
    if missing_fields:
        ui.notify(f'Please fill in all required fields: {", ".join(missing_fields)}', type='negative')
        return
    
    try:
        # Prepare job data
        job_data = {
            'title': title.value,
            'description': description.value,
            'category': category.value,
            'employment_type': employment_type.value,
            'location': location.value,
            'salary_min': int(salary_min.value) if salary_min.value else 0,
            'salary_max': int(salary_max.value) if salary_max.value else 0,
            'currency': currency.value,
            'posted_by': posted_by.value,
            'date_posted': date_posted.value,
            'application_deadline': application_deadline.value,
            'job_status': job_status.value
        }
        
        # Post job to API
        result = api_client.post_job(job_data)
        
        if result and result.get('success'):
            ui.notify('✅ Job posted successfully to API!', type='positive')
            # Add to global list for backward compatibility
            global_job_listings.append(job_data)
        else:
            ui.notify('❌ Failed to post job to API', type='negative')
            return
        
        # Clear form
        title.value = ''
        description.value = ''
        category.value = 'Technology'
        employment_type.value = 'Full-time'
        location.value = ''
        salary_min.value = 0
        salary_max.value = 0
        currency.value = 'USD'
        posted_by.value = ''
        date_posted.value = today
        application_deadline.value = today
        job_status.value = 'Active'
        
        # Navigate to jobs page
        ui.navigate.to('/jobs')
        
    except Exception as e:
        ui.notify(f'❌ Error posting job: {str(e)}', type='negative')

# Global job listings for compatibility
global_job_listings = []

def get_global_job_listings():
    """Get job listings from the API and update the global cache."""
    global global_job_listings
    try:
        print("Fetching jobs from API...")
        response = api_client.get_jobs()
        print(f"API Response: {response}")
        
        # Handle different response formats
        if isinstance(response, list):
            # If the response is already a list, use it directly
            global_job_listings = response
        elif isinstance(response, dict):
            # If the response is a dictionary, check for common keys
            if 'results' in response:
                global_job_listings = response['results']
            elif 'data' in response:
                global_job_listings = response['data']
            elif 'jobs' in response:
                global_job_listings = response['jobs']
            else:
                # If no standard key is found, try to use the entire response as a list
                global_job_listings = [response]
        else:
            global_job_listings = []
            
        print(f"Found {len(global_job_listings)} jobs")
        if global_job_listings:
            print(f"First job: {global_job_listings[0]}")
            
        return global_job_listings
        
    except Exception as e:
        error_msg = f"Failed to fetch jobs: {str(e)}"
        print(error_msg)
        ui.notify(error_msg, type='negative')
        return []