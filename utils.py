from nicegui import ui
from datetime import datetime
from pages.add_event import global_job_listings

def format_date(date_str: str) -> str:
    """Format date string to a relative time string."""
    if not date_str:
        return 'Recently'
    try:
        posted_date = datetime.strptime(date_str, '%Y-%m-%d')
        delta = datetime.now() - posted_date
        
        if delta.days == 0:
            return 'Today'
        elif delta.days == 1:
            return 'Yesterday'
        elif delta.days < 30:
            return f"{delta.days} days ago"
        else:
            return 'Recently'
    except (ValueError, TypeError):
        return 'Recently'

def apply_to_job(job):
    """Handle job application."""
    if job.get('application_url'):
        ui.navigate.to(job['application_url'])
        ui.notify(f'Opening application page for {job["job_title"]}', type='info')
    else:
        contact_email = job.get('contact_email', 'the company')
        ui.notify(f'Send your application to: {contact_email}', type='info')

def create_jobcamp_job_card(job):
    """Creates a JobCamp-style job card with reliable images."""
    with ui.card().classes('job-card w-full lg:w-80'):
        with ui.row().classes('w-full justify-between items-start mb-4'):
            company_images = {
                'TechCorp Inc.': 'https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                'MarketPro Agency': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                'Creative Studios': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                'ContentFirst': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                'InnovateTech': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                'WebCraft Solutions': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80'
            }
            img_url = company_images.get(job['company'], 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80')
            
            with ui.card().classes('w-12 h-12 border-0 overflow-hidden rounded-xl shadow-lg'):
                ui.image(img_url).classes('w-full h-full object-cover')
            ui.button(icon='bookmark_border').props('flat round dense size=sm').classes('text-gray-400 hover:text-blue-600')
        
        ui.link(job['job_title'], f"/jobs/{job['id']}").classes('text-xl font-bold text-gray-900 hover:text-blue-600 transition-colors mb-2 block')
        ui.label(job['company']).classes('text-gray-600 mb-4')
        
        with ui.row().classes('w-full justify-between items-center mb-4'):
            with ui.row().classes('items-center gap-1'):
                ui.icon('location_on', size='sm', color='gray-500')
                ui.label(job['location']).classes('text-sm text-gray-600')
            with ui.row().classes('items-center gap-1'):
                ui.icon('schedule', size='sm', color='gray-500')
                ui.label(job['job_type']).classes('text-sm text-gray-600')
        
        if job.get('salary_min') and job.get('salary_max'):
            salary_text = f"${job['salary_min']:,} - ${job['salary_max']:,}"
            ui.label(salary_text).classes('text-lg font-bold text-green-600 mb-4')
        
        with ui.row().classes('w-full gap-2'):
            ui.button('Apply Now', on_click=lambda j=job: apply_to_job(j)).classes('flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-colors')
            ui.button('Edit', on_click=lambda j=job: ui.navigate.to(f'/edit-job/{j["id"]}')).classes('w-16 bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 rounded-xl transition-colors')

def search_jobs(query, location, category='All Categories'):
    """Handle job search functionality with category filtering."""
    if query or location or category != 'All Categories':
        search_params = []
        if query:
            search_params.append(f'"{query}"')
        if location:
            search_params.append(f'in "{location}"')
        if category != 'All Categories':
            search_params.append(f'category: {category}')
        
        search_text = 'Searching for ' + ' '.join(search_params) + '...'
        ui.notify(search_text, type='info')
        
        filtered_jobs = []
        for job in global_job_listings:
            match = True
            if query and query.lower() not in job['job_title'].lower() and query.lower() not in job['company'].lower():
                match = False
            if location and location.lower() not in job['location'].lower():
                match = False
            if category != 'All Categories' and category.lower() not in job.get('category', '').lower():
                match = False
            if match:
                filtered_jobs.append(job)
        
        if filtered_jobs:
            ui.notify(f'Found {len(filtered_jobs)} matching jobs!', type='positive')
        else:
            ui.notify('No jobs found matching your criteria', type='warning')
        
        ui.navigate.to('/jobs')
    else:
        ui.notify('Please enter search criteria', type='warning')