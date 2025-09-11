from nicegui import ui, app
from components.header import show_header
from datetime import datetime
from utils.api_client import api_client
import json
import requests
from utils.api import base_url

def show_add_event_page():
    flyer_content = None

    def handle_flyer_upload(e):
        nonlocal flyer_content
        flyer_content = e.content

    """Displays a modern, enhanced form for posting new job listings."""
    show_header()
    
    with ui.column().classes('w-full max-w-5xl mx-auto p-4 md:p-8'):
        # Enhanced header with gradient background
        with ui.card().classes('w-full mb-8 bg-gradient-to-r from-primary to-secondary text-white border-0'):
            with ui.column().classes('w-full p-8 text-center'):
                ui.icon('add_business', size='xl').classes('mb-4 animate-bounce')
                ui.label('🚀 Post a New Job').classes('text-4xl lg:text-5xl font-bold mb-4')
                ui.label('Find the perfect candidate for your team').classes('text-xl opacity-90')
        
        with ui.card().classes('modern-card w-full p-8 shadow-2xl animate-fade-in-up'):
            with ui.column().classes('w-full space-y-8'):
                # Step 1: Job Information Section
                with ui.card().classes('w-full p-6 bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200'):
                    with ui.column().classes('w-full space-y-6'):
                        with ui.row().classes('items-center space-x-3 mb-4'):
                            ui.avatar('1', color='primary').classes('text-white font-bold')
                            ui.label('📋 Job Information').classes('text-2xl font-bold text-gray-800')
                        
                        # Job Title with enhanced styling
                        job_title = ui.input(
                            label='Job Title *',
                            placeholder='e.g., Senior Software Engineer, Product Manager, UX Designer'
                        ).classes('form-input w-full')
                        
                        # Company Name with icon
                        with ui.row().classes('w-full items-end space-x-4'):
                            company = ui.input(
                                label='Company Name *',
                                placeholder='Your amazing company name'
                            ).classes('form-input flex-1')
                            
                            ui.button(icon='business', on_click=lambda: ui.notify('Company profile coming soon!')).props('flat').classes('text-primary mb-2')
                        
                        # Job Type and Experience Level
                        with ui.row().classes('w-full gap-4'):
                            job_type = ui.select(
                                label='Job Type *',
                                options=['Full-time', 'Part-time', 'Contract', 'Temporary', 'Internship', 'Freelance'],
                                value='Full-time'
                            ).classes('form-input flex-1')
                            
                            experience_level = ui.select(
                                label='Experience Level *',
                                options=['Entry Level', 'Mid Level', 'Senior', 'Lead', 'Manager', 'Executive'],
                                value='Mid Level'
                            ).classes('form-input flex-1')
                        
                        # Location with remote toggle
                        with ui.row().classes('w-full items-end gap-4'):
                            location = ui.input(
                                label='Location *',
                                placeholder='e.g., New York, NY or Worldwide'
                            ).classes('form-input flex-1')
                            
                            with ui.column().classes('items-center'):
                                remote_ok = ui.switch('Remote Position', value=False).classes('text-primary')
                                ui.label('🌍 Remote').classes('text-sm text-gray-600')
                
                # Step 2: Salary & Benefits Section
                with ui.card().classes('w-full p-6 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200'):
                    with ui.column().classes('w-full space-y-6'):
                        with ui.row().classes('items-center space-x-3 mb-4'):
                            ui.avatar('2', color='positive').classes('text-white font-bold')
                            ui.label('💰 Salary & Benefits').classes('text-2xl font-bold text-gray-800')
                        
                        # Salary Range with enhanced styling
                        with ui.row().classes('w-full gap-4'):
                            min_salary = ui.number(
                                label='Minimum Salary ($) *',
                                format='%.0f',
                                min=0,
                                value=50000
                            ).classes('form-input flex-1')
                            
                            max_salary = ui.number(
                                label='Maximum Salary ($) *',
                                format='%.0f',
                                min=0,
                                value=120000
                            ).classes('form-input flex-1')
                        
                        # Salary Period
                        salary_period = ui.select(
                            label='Payment Period',
                            options=['per year', 'per month', 'per hour', 'per project'],
                            value='per year'
                        ).classes('form-input w-48')
                        
                        # Benefits with enhanced textarea
                        benefits = ui.textarea(
                            label='Benefits & Perks',
                            placeholder='🏥 Health insurance\n🦷 Dental coverage\n💰 401(k) matching\n🏖️ Unlimited PTO\n🏠 Remote work options\n📚 Learning budget'
                        ).classes('form-input w-full').style('min-height: 120px')
                
                # Step 3: Job Description & Requirements
                with ui.card().classes('w-full p-6 bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200'):
                    with ui.column().classes('w-full space-y-6'):
                        with ui.row().classes('items-center space-x-3 mb-4'):
                            ui.avatar('3', color='secondary').classes('text-white font-bold')
                            ui.label('📝 Job Description & Requirements').classes('text-2xl font-bold text-gray-800')
                        
                        # Job Description with rich text editor styling
                        job_description = ui.textarea(
                            label='Job Description *',
                            placeholder='🎯 What will this person do?\n\n• Lead product development initiatives\n• Collaborate with cross-functional teams\n• Drive innovation and technical excellence\n• Mentor junior team members\n\nDescribe the role, responsibilities, and what makes this opportunity exciting!'
                        ).classes('form-input w-full').style('min-height: 200px')
                        
                        # Requirements with enhanced styling
                        requirements = ui.textarea(
                            label='Requirements & Qualifications *',
                            placeholder='🎓 What are you looking for?\n\nRequired:\n• 5+ years of experience in...\n• Proficiency in Python, JavaScript\n• Strong communication skills\n\nPreferred:\n• Experience with cloud platforms\n• Leadership experience\n• Bachelor\'s degree in...'
                        ).classes('form-input w-full').style('min-height: 180px')
                        
                        # Skills tags input
                        with ui.column().classes('w-full space-y-3'):
                            ui.label('Required Skills & Technologies').classes('text-lg font-semibold text-gray-700')
                            with ui.row().classes('w-full items-center gap-2'):
                                skill_input = ui.input(
                                    placeholder='Add skill (e.g., Python, React, Leadership)'
                                ).classes('form-input flex-1')
                                ui.button('+ Add Skill', on_click=lambda: add_skill_tag()).classes('btn btn-primary')
                            
                            # Skills display area
                            with ui.row().classes('flex-wrap gap-2 mt-2') as skills_display:
                                # Sample skills for demonstration
                                for skill in ['Python', 'JavaScript', 'Leadership']:
                                    ui.chip(skill, removable=True).classes('bg-blue-100 text-blue-800')
                
                # Step 4: Application Details
                with ui.card().classes('w-full p-6 bg-gradient-to-br from-orange-50 to-red-50 border border-orange-200'):
                    with ui.column().classes('w-full space-y-6'):
                        with ui.row().classes('items-center space-x-3 mb-4'):
                            ui.avatar('4', color='warning').classes('text-white font-bold')
                            ui.label('📧 Application Details').classes('text-2xl font-bold text-gray-800')
                        
                        # Contact Email with validation
                        application_email = ui.input(
                            label='Contact Email *',
                            placeholder='careers@yourcompany.com'
                        ).classes('form-input w-full')
                        
                        # Application URL
                        application_url = ui.input(
                            label='Application URL (optional)',
                            placeholder='https://yourcompany.com/careers/apply'
                        ).classes('form-input w-full')
                        
                        # Application deadline
                        from datetime import datetime, timedelta
                        default_deadline = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
                        ui.label('Application Deadline').classes('text-sm font-medium text-gray-700 mb-1')
                        deadline = ui.date(
                            value=default_deadline
                        ).classes('form-input w-64')
                        ui.upload(on_upload=handle_flyer_upload)
                
                # Enhanced Form Actions with modern styling
                with ui.card().classes('w-full mt-8 p-6 bg-gradient-to-r from-gray-50 to-white border border-gray-200'):
                    with ui.column().classes('w-full space-y-4'):
                        ui.label('🚀 Ready to publish your job?').classes('text-xl font-bold text-gray-800 text-center')
                        ui.label('Review your job posting and publish it to start receiving applications').classes('text-gray-600 text-center')
                        
                        with ui.row().classes('w-full justify-center gap-4'):
                            # Clear Form Button
                            ui.button(
                                '🗑️ Clear Form',
                                on_click=lambda: clear_form_with_confirmation(),
                                color='gray'
                            ).classes('btn btn-secondary px-6 py-3')
                            
                            # Preview Button
                            ui.button(
                                '👁️ Preview Job',
                                on_click=lambda: show_enhanced_preview(),
                                color='primary'
                            ).classes('btn btn-secondary px-6 py-3')
                            
                            # Submit Button with enhanced styling
                            ui.button(
                                '🚀 Publish Job',
                                on_click=lambda:validate_and_submit_enhanced({
                                    'job_title': job_title.value,
                                    'company': company.value,
                                    'job_type': job_type.value,
                                    'location': location.value,
                                    'is_remote': remote_ok.value,
                                    'min_salary': min_salary.value,
                                    'max_salary': max_salary.value,
                                    'benefits': benefits.value,
                                    'description': job_description.value,
                                    'requirements': requirements.value,
                                    'contact_email': application_email.value,
                                    'application_url': application_url.value,
                                    'flyer':flyer_content,
                                    'posted_date': datetime.now().strftime('%Y-%m-%d'),
                                    'id': f"job_{len(global_job_listings) + 1}"
                                }),
                                color='positive'
                            ).classes('btn btn-primary px-8 py-3 text-lg font-bold')

# Helper functions for enhanced form functionality
def add_skill_tag():
    """Add a skill tag to the skills display."""
    ui.notify('Skill added! (Demo functionality)', type='positive')

def clear_form_with_confirmation():
    """Clear form with confirmation dialog."""
    with ui.dialog() as confirm_dialog, ui.card():
        ui.label('Are you sure you want to clear the form?').classes('text-lg font-semibold mb-4')
        ui.label('All your progress will be lost.').classes('text-gray-600 mb-4')
        with ui.row().classes('w-full justify-end gap-2'):
            ui.button('Cancel', on_click=confirm_dialog.close).props('flat')
            ui.button('Clear Form', on_click=lambda: [confirm_dialog.close(), ui.notify('Form cleared', type='info')], color='negative')
    confirm_dialog.open()

def show_enhanced_preview():
    """Show enhanced job preview with better styling."""
    ui.notify('Opening enhanced preview...', type='info')

def validate_and_submit_enhanced(data):
    response = requests.post(f"{base_url}/jobs", data)
    print(response.status_code)
    """Enhanced validation and submission with better UX."""
    # ui.notify('🎉 Job posted successfully! Redirecting...', type='positive')
    # ui.timer(2.0, lambda: ui.navigate.to('/jobs'), once=True)

def validate_and_submit(**fields):
    """Validate form fields before submission."""
    # Check required fields
    required_fields = {
        'job_title': 'Job Title',
        'company': 'Company Name',
        'description': 'Job Description',
        'contact_email': 'Contact Email'
    }
    
    # Validate required fields
    for field, label in required_fields.items():
        field_value = fields[field].value if hasattr(fields[field], 'value') else fields[field]
        if not field_value:
            ui.notify(f'❌ {label} is required', type='negative')
            return
    
    # Validate email format
    if '@' not in fields['contact_email'].value or '.' not in fields['contact_email'].value.split('@')[-1]:
        ui.notify('❌ Please enter a valid email address', type='negative')
        return
    
    # Validate salary range if provided
    if fields['min_salary'].value and fields['max_salary'].value:
        try:
            min_sal = float(fields['min_salary'].value)
            max_sal = float(fields['max_salary'].value)
            if min_sal > max_sal:
                ui.notify('❌ Maximum salary must be greater than minimum salary', type='negative')
                return
        except (ValueError, TypeError):
            pass  # Non-numeric values will be handled by the number input
    
    # If all validations pass, proceed to post the job
    post_job({
        'job_title': fields['job_title'].value,
        'company': fields['company'].value,
        'job_type': fields['job_type'].value,
        'location': fields['location'].value,
        'is_remote': fields['is_remote'].value,
        'min_salary': fields['min_salary'].value,
        'max_salary': fields['max_salary'].value,
        'benefits': fields['benefits'].value,
        'description': fields['description'].value,
        'requirements': fields['requirements'].value,
        'contact_email': fields['contact_email'].value,
        'application_url': fields['application_url'].value,
        'posted_date': datetime.now().strftime('%Y-%m-%d'),
        'id': f"job_{len(global_job_listings) + 1}"
    })

def post_job(job_data):
    """Handle job posting submission with comprehensive error handling and user feedback."""
    try:
        print("=== Starting job submission ===")
        print("Job data before processing:", json.dumps(job_data, indent=2, default=str))
        
        # Ensure required fields are present
        required_fields = ['title', 'company', 'location', 'description']
        missing_fields = [field for field in required_fields if not job_data.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        # Process salary fields
        if 'salary_min' in job_data and job_data['salary_min']:
            try:
                job_data['salary_min'] = int(float(job_data['salary_min']))
            except (ValueError, TypeError) as e:
                print(f"Warning: Could not convert salary_min to int: {e}")
                job_data['salary_min'] = None
                
        if 'salary_max' in job_data and job_data['salary_max']:
            try:
                job_data['salary_max'] = int(float(job_data['salary_max']))
            except (ValueError, TypeError) as e:
                print(f"Warning: Could not convert salary_max to int: {e}")
                job_data['salary_max'] = None
        
        # Add timestamp if not present
        if 'posted_date' not in job_data:
            job_data['posted_date'] = datetime.now().isoformat()
        
        print("Job data after processing:", json.dumps(job_data, indent=2, default=str))
            
        # Post job to the API
        print("Sending job data to API...")
        response = api_client.post_job(job_data)
        print("API Response received:", json.dumps(response, indent=2, default=str) if response else "No response")
        
        if not response:
            raise Exception("Received empty response from API")
        
        # Check for error in response
        if isinstance(response, dict) and 'error' in response:
            raise Exception(f"API Error: {response.get('error', 'Unknown error')}")
            
        # Force refresh the global cache
        print("Refreshing job listings...")
        updated_listings = get_global_job_listings()
        print(f"Updated job listings count: {len(updated_listings) if updated_listings else 0}")
        
        # Show success message
        success_msg = '🎉 Job posted successfully!'
        print(success_msg)
        ui.notify(success_msg, type='positive')
        
        # Clear the form
        clear_form()
        
        # Navigate to jobs page after a short delay
        def navigate_to_jobs():
            print("Navigating to jobs page...")
            ui.navigate.to('/jobs')
        
        # Add a small delay to ensure the user sees the success message
        ui.timer(1.5, navigate_to_jobs, once=True)
        
    except Exception as e:
        error_msg = f'❌ Error posting job: {str(e)}'
        print(error_msg)
        
        # More detailed error for the console
        import traceback
        traceback.print_exc()
        
        # User-friendly error message
        ui.notify(error_msg, type='negative', 
                 close_button='OK', 
                 position='top',
                 timeout=10000)  # Show for 10 seconds

def clear_form(fields=None):
    """Clear all form fields."""
    if fields:
        for field in fields:
            if hasattr(field, 'value'):
                field.value = '' if not isinstance(field, (ui.checkbox, ui.select)) else None
    ui.notify('Form cleared', type='info')

def show_preview(job_data):
    """Show a preview of the job posting."""
    # Create a preview dialog
    with ui.dialog() as preview_dialog, ui.card():
        ui.label('Job Posting Preview').classes('text-xl font-bold mb-4')
        
        with ui.column().classes('space-y-4'):
            ui.label(f"Job Title: {job_data['job_title'].value}")
            ui.label(f"Company: {job_data['company'].value}")
            ui.label(f"Location: {job_data['location'].value} {'(Remote)' if job_data['is_remote'].value else ''}")
            ui.label(f"Job Type: {job_data['job_type'].value}")
            
            if job_data['min_salary'].value or job_data['max_salary'].value:
                salary_range = []
                if job_data['min_salary'].value:
                    salary_range.append(f"${float(job_data['min_salary'].value):,.0f}")
                if job_data['max_salary'].value:
                    salary_range.append(f"${float(job_data['max_salary'].value):,.0f}")
                ui.label(f"Salary: {' - '.join(salary_range)}")
            
            if job_data['benefits'].value:
                with ui.expansion('Benefits', icon='work').classes('w-full'):
                    ui.html(f"<div class='whitespace-pre-line'>{job_data['benefits'].value}</div>")
            
            with ui.expansion('Job Description', icon='description').classes('w-full'):
                ui.html(f"<div class='whitespace-pre-line'>{job_data['description'].value}</div>")
            
            with ui.expansion('Requirements', icon='checklist').classes('w-full'):
                ui.html(f"<div class='whitespace-pre-line'>{job_data['requirements'].value}</div>")
            
            ui.label('How to Apply')
            if job_data['application_url'].value:
                ui.link('Apply Online', job_data['application_url'].value, new_tab=True)
            else:
                ui.label(f"Email your application to: {job_data['contact_email'].value}")
        
        with ui.row().classes('w-full justify-end mt-4'):
            ui.button('Close', on_click=preview_dialog.close)
    
    preview_dialog.open()

# Global job listings cache
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