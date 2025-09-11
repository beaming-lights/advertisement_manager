from nicegui import ui
from components.header import show_header
from utils.api_client import api_client
from datetime import datetime

def show_edit_event_page(job_id=None):
    """Simple job editing form."""
    show_header()
    
    
    
    
    with ui.column().classes('max-w-2xl mx-auto p-6'):
        ui.label('Edit Job').classes('text-2xl font-bold mb-6')
        
        # Load job data if job_id provided
        job_data = {}
        if job_id:
            try:
                job_data = api_client.get_job(job_id)
            except:
                ui.notify('Job not found', type='negative')
                ui.navigate.to('/jobs')
                return
        
        with ui.card().classes('p-6'):
            # Basic job info
            title = ui.input('Job Title', value=job_data.get('title', '')).classes('w-full mb-4')
            company = ui.input('Company', value=job_data.get('company', '')).classes('w-full mb-4')
            location = ui.input('Location', value=job_data.get('location', '')).classes('w-full mb-4')
            
            # Job details
            job_type = ui.select(
                label='Job Type',
                options=['Full-time', 'Part-time', 'Contract', 'Internship'],
                value=job_data.get('job_type', 'Full-time')
            ).classes('w-full mb-4')
            
            # Salary
            with ui.row().classes('w-full gap-4 mb-4'):
                min_salary = ui.number('Min Salary', value=job_data.get('salary_min', 0)).classes('flex-1')
                max_salary = ui.number('Max Salary', value=job_data.get('salary_max', 0)).classes('flex-1')
            
            # Description and requirements
            description = ui.textarea('Job Description', value=job_data.get('description', '')).classes('w-full mb-4').style('min-height: 120px')
            requirements = ui.textarea('Requirements', value=job_data.get('requirements', '')).classes('w-full mb-4').style('min-height: 120px')
            
            # Contact
            email = ui.input('Contact Email', value=job_data.get('contact_email', '')).classes('w-full mb-6')
            
            # Action buttons
            with ui.row().classes('w-full gap-4'):
                ui.button(
                    'Cancel',
                    on_click=lambda: ui.navigate.to('/jobs')
                ).classes('flex-1 bg-gray-500 text-white')
                
                ui.button(
                    'Update Job',
                    on_click=lambda: update_job(
                        job_id, title, company, location, job_type, min_salary, max_salary,
                        description, requirements, email
                    )
                ).classes('flex-1 bg-blue-500 text-white')

def update_job(job_id, title, company, location, job_type, min_salary, max_salary, description, requirements, email):
    """Update job with basic validation."""
    # Validate required fields
    if not title.value or not company.value or not description.value or not email.value:
        ui.notify('Please fill in all required fields', type='negative')
        return
    
    # Prepare job data
    job_data = {
        'title': title.value,
        'company': company.value,
        'location': location.value,
        'job_type': job_type.value,
        'salary_min': min_salary.value if min_salary.value > 0 else None,
        'salary_max': max_salary.value if max_salary.value > 0 else None,
        'description': description.value,
        'requirements': requirements.value,
        'contact_email': email.value,
        'updated_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    try:
        # Note: This assumes your API has an update method
        response = api_client.update_job(job_id, job_data)
        ui.notify('Job updated successfully!', type='positive')
        
        # Navigate to jobs page
        ui.timer(1.0, lambda: ui.navigate.to('/jobs'), once=True)
        
    except Exception as e:
        ui.notify(f'Error updating job: {str(e)}', type='negative')