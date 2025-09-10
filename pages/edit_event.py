from nicegui import ui
from components.header import show_header
from components.footer import show_footer
from pages.add_event import global_job_listings
from datetime import datetime, timedelta

def show_edit_event_page(job_id: str = None):
    """Display job editing page with edit, update, and delete functionality."""
    show_header()
    
    # Find the job by ID
    job = next((j for j in global_job_listings if j['id'] == job_id), None) if job_id else None
    
    if not job and job_id:
        with ui.column().classes('w-full max-w-4xl mx-auto p-6'):
            ui.label('Job Not Found').classes('text-2xl font-bold text-red-600')
            ui.label('The requested job could not be found or may have been removed.')
            ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('btn btn-secondary mt-4')
        return
    
    with ui.column().classes('w-full max-w-5xl mx-auto p-4 md:p-8'):
        # Header
        with ui.card().classes('w-full mb-8 bg-gradient-to-r from-orange-500 to-red-500 text-white border-0'):
            with ui.column().classes('w-full p-8 text-center'):
                ui.icon('edit', size='xl').classes('mb-4')
                ui.label('✏️ Edit Job Posting' if job else '📝 Manage Jobs').classes('text-4xl lg:text-5xl font-bold mb-4')
                ui.label('Update job details or manage existing postings' if job else 'Select a job to edit or manage').classes('text-xl opacity-90')

        if not job:
            # Job selection interface
            show_job_management_interface()
        else:
            # Job editing form
            show_job_edit_form(job)

    show_footer()

def show_job_management_interface():
    """Show interface to select and manage jobs."""
    if not global_job_listings:
        with ui.card().classes('w-full p-12 text-center border border-gray-200'):
            ui.icon('work_off', size='xl', color='gray-400').classes('mx-auto mb-4')
            ui.label('No jobs to manage').classes('text-xl font-medium text-gray-600 mb-2')
            ui.label('Post your first job to start managing job listings.').classes('text-gray-500')
            ui.button('Post a Job', on_click=lambda: ui.navigate.to('/post-job')).classes('btn btn-primary mt-6')
    else:
        ui.label('Select a job to edit or manage:').classes('text-xl font-semibold text-gray-800 mb-6')
        
        with ui.row().classes('w-full gap-6 flex-wrap'):
            for job in global_job_listings:
                with ui.card().classes('w-full lg:w-80 p-6 hover:shadow-lg transition-shadow'):
                    ui.label(job['job_title']).classes('text-lg font-bold text-gray-900 mb-2')
                    ui.label(job['company']).classes('text-gray-600 mb-2')
                    ui.label(f"📍 {job['location']}").classes('text-sm text-gray-500 mb-4')
                    
                    with ui.row().classes('w-full gap-2'):
                        ui.button('Edit', on_click=lambda j=job: ui.navigate.to(f'/edit-job/{j["id"]}')).classes('btn btn-primary flex-1')
                        ui.button('Delete', on_click=lambda j=job: confirm_delete_job(j)).classes('btn btn-secondary flex-1')

def show_job_edit_form(job):
    """Show the job editing form with pre-populated data."""
    
    # Job Information Section
    with ui.card().classes('w-full p-6 bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200 mb-6'):
        with ui.column().classes('w-full space-y-6'):
            ui.label('📋 Job Information').classes('text-2xl font-bold text-gray-800 mb-4')
            
            job_title = ui.input(label='Job Title *', value=job.get('job_title', '')).classes('form-input w-full')
            
            with ui.row().classes('w-full gap-4'):
                company = ui.input(label='Company Name *', value=job.get('company', '')).classes('form-input flex-1')
                job_type = ui.select(
                    label='Job Type *',
                    options=['Full-time', 'Part-time', 'Contract', 'Temporary', 'Internship', 'Freelance'],
                    value=job.get('job_type', 'Full-time')
                ).classes('form-input flex-1')
            
            with ui.row().classes('w-full gap-4'):
                location = ui.input(label='Location *', value=job.get('location', '')).classes('form-input flex-1')
                experience_level = ui.select(
                    label='Experience Level *',
                    options=['Entry Level', 'Mid Level', 'Senior', 'Lead', 'Manager', 'Executive'],
                    value=job.get('experience_level', 'Mid Level')
                ).classes('form-input flex-1')

    # Salary & Benefits Section
    with ui.card().classes('w-full p-6 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200 mb-6'):
        with ui.column().classes('w-full space-y-6'):
            ui.label('💰 Salary & Benefits').classes('text-2xl font-bold text-gray-800 mb-4')
            
            with ui.row().classes('w-full gap-4'):
                min_salary = ui.number(
                    label='Minimum Salary ($) *',
                    format='%.0f',
                    min=0,
                    value=float(job.get('min_salary', 50000))
                ).classes('form-input flex-1')
                
                max_salary = ui.number(
                    label='Maximum Salary ($) *',
                    format='%.0f',
                    min=0,
                    value=float(job.get('max_salary', 120000))
                ).classes('form-input flex-1')
            
            salary_period = ui.select(
                label='Payment Period',
                options=['per year', 'per month', 'per hour', 'per project'],
                value=job.get('salary_period', 'per year')
            ).classes('form-input w-48')

    # Job Description Section
    with ui.card().classes('w-full p-6 bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200 mb-6'):
        with ui.column().classes('w-full space-y-6'):
            ui.label('📝 Job Description & Requirements').classes('text-2xl font-bold text-gray-800 mb-4')
            
            job_description = ui.textarea(
                label='Job Description *',
                value=job.get('description', '')
            ).classes('form-input w-full').style('min-height: 150px')
            
            requirements = ui.textarea(
                label='Requirements & Qualifications *',
                value=job.get('requirements', '')
            ).classes('form-input w-full').style('min-height: 120px')

    # Application Details Section
    with ui.card().classes('w-full p-6 bg-gradient-to-br from-orange-50 to-red-50 border border-orange-200 mb-6'):
        with ui.column().classes('w-full space-y-6'):
            ui.label('📧 Application Details').classes('text-2xl font-bold text-gray-800 mb-4')
            
            application_email = ui.input(
                label='Contact Email *',
                value=job.get('contact_email', '')
            ).classes('form-input w-full')
            
            application_url = ui.input(
                label='Application URL (optional)',
                value=job.get('application_url', '')
            ).classes('form-input w-full')

    # Action Buttons
    with ui.card().classes('w-full p-6 bg-gray-50'):
        with ui.row().classes('w-full justify-center gap-4'):
            ui.button('← Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('btn btn-secondary px-6 py-3')
            ui.button('🗑️ Delete Job', on_click=lambda: confirm_delete_job(job)).classes('btn btn-secondary px-6 py-3')
            ui.button('💾 Update Job', on_click=lambda: update_job(
                job, job_title, company, job_type, location, experience_level,
                min_salary, max_salary, salary_period, job_description, 
                requirements, application_email, application_url
            )).classes('btn btn-primary px-8 py-3 text-lg font-bold')

def update_job(job, job_title, company, job_type, location, experience_level,
               min_salary, max_salary, salary_period, job_description, 
               requirements, application_email, application_url):
    """Update the job with new information."""
    
    # Validation
    if not all([job_title.value, company.value, location.value, job_description.value, application_email.value]):
        ui.notify('Please fill in all required fields', type='warning')
        return
    
    # Update job data
    job.update({
        'job_title': job_title.value,
        'company': company.value,
        'job_type': job_type.value,
        'location': location.value,
        'experience_level': experience_level.value,
        'min_salary': min_salary.value,
        'max_salary': max_salary.value,
        'salary_period': salary_period.value,
        'description': job_description.value,
        'requirements': requirements.value,
        'contact_email': application_email.value,
        'application_url': application_url.value,
        'updated_date': datetime.now().strftime('%Y-%m-%d')
    })
    
    ui.notify('✅ Job updated successfully!', type='positive')
    ui.timer(1.5, lambda: ui.navigate.to('/jobs'), once=True)

def confirm_delete_job(job):
    """Show confirmation dialog for job deletion."""
    with ui.dialog() as delete_dialog, ui.card():
        ui.label(f'Delete "{job["job_title"]}"?').classes('text-lg font-semibold mb-4')
        ui.label('This action cannot be undone. The job posting will be permanently removed.').classes('text-gray-600 mb-6')
        
        with ui.row().classes('w-full justify-end gap-2'):
            ui.button('Cancel', on_click=delete_dialog.close).classes('btn btn-secondary')
            ui.button('Delete Job', on_click=lambda: delete_job(job, delete_dialog)).classes('btn btn-primary')
    
    delete_dialog.open()

def delete_job(job, dialog):
    """Delete the job from the global listings."""
    global_job_listings.remove(job)
    dialog.close()
    ui.notify(f'🗑️ Job "{job["job_title"]}" deleted successfully', type='positive')
    ui.timer(1.0, lambda: ui.navigate.to('/jobs'), once=True)