from nicegui import ui
from components.header import show_header
from utils.api_client import api_client
from datetime import datetime

def show_jobs_page():
    """Elegant job listings page with modern design."""
    show_header()
    
    with ui.column().classes('min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100'):
        # Hero section with search
        with ui.column().classes('w-full bg-white shadow-sm border-b'):
            with ui.column().classes('max-w-6xl mx-auto p-8'):
                # Header with stats
                with ui.row().classes('w-full justify-between items-center mb-8'):
                    with ui.column().classes('gap-2'):
                        ui.label('Find Your Dream Job').classes('text-4xl font-bold text-gray-900')
                        ui.label('Discover opportunities that match your skills and passion').classes('text-lg text-gray-600')
                    
                    ui.button('Post New Job', on_click=lambda: ui.navigate.to('/post-job')).classes(
                        'bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-3 rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1'
                    )
                
                # Search and filters
                with ui.row().classes('w-full gap-4 mb-6'):
                    search_input = ui.input('Search jobs...', placeholder='Job title, company, or keywords').classes(
                        'flex-1 rounded-xl border-2 border-gray-200 focus:border-blue-500 transition-colors'
                    ).props('outlined dense')
                    
                    location_input = ui.input('Location', placeholder='City, state, or remote').classes(
                        'w-64 rounded-xl border-2 border-gray-200 focus:border-blue-500 transition-colors'
                    ).props('outlined dense')
                    
                    ui.button('Search', on_click=lambda: filter_jobs(search_input.value, location_input.value)).classes(
                        'bg-blue-600 text-white px-6 py-2 rounded-xl font-medium hover:bg-blue-700 transition-colors'
                    )
                
                # Filter chips
                with ui.row().classes('gap-2 flex-wrap'):
                    filter_options = ['Full-time', 'Part-time', 'Remote', 'Contract', 'Internship']
                    for option in filter_options:
                        ui.button(option, on_click=lambda opt=option: toggle_filter(opt)).classes(
                            'bg-gray-100 text-gray-700 px-4 py-2 rounded-full text-sm hover:bg-blue-100 hover:text-blue-700 transition-colors'
                        )
        
        # Main content area
        with ui.column().classes('max-w-6xl mx-auto p-8 w-full'):
            # Load jobs
            try:
                jobs = api_client.get_jobs()
                job_count = len(jobs) if jobs else 0
            except Exception as e:
                ui.notify(f'Error loading jobs: {str(e)}', type='negative')
                jobs = []
                job_count = 0
            
            # Results header
            with ui.row().classes('w-full justify-between items-center mb-6'):
                ui.label(f'{job_count} Jobs Found').classes('text-xl font-semibold text-gray-800')
                
                with ui.row().classes('gap-2 items-center'):
                    ui.label('Sort by:').classes('text-sm text-gray-600')
                    ui.select(['Newest', 'Salary: High to Low', 'Salary: Low to High', 'Company A-Z'], 
                             value='Newest').classes('w-40').props('outlined dense')
            
            if not jobs:
                # Empty state
                with ui.column().classes('text-center py-16'):
                    ui.icon('work_outline', size='4rem').classes('text-gray-300 mb-4')
                    ui.label('No jobs found').classes('text-2xl font-semibold text-gray-600 mb-2')
                    ui.label('Be the first to post a job opportunity').classes('text-gray-500 mb-6')
                    ui.button('Post the First Job', on_click=lambda: ui.navigate.to('/post-job')).classes(
                        'bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-3 rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-300'
                    )
            else:
                # Jobs grid
                with ui.grid(columns='repeat(auto-fill, minmax(400px, 1fr))').classes('gap-6 w-full'):
                    for job in jobs:
                        create_job_card(job)

def create_job_card(job):
    """Create an elegant job card with modern styling."""
    with ui.card().classes(
        'group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 '
        'transform hover:-translate-y-2 border border-gray-100 overflow-hidden cursor-pointer'
    ).on('click', lambda: ui.navigate.to(f'/view-job/{job.get("id", "")}')):
        
        # Job type badge
        with ui.row().classes('absolute top-4 right-4 z-10'):
            job_type = job.get('employment_type', 'Full-time')
            badge_color = {
                'Full-time': 'bg-green-100 text-green-800',
                'Part-time': 'bg-blue-100 text-blue-800', 
                'Contract': 'bg-purple-100 text-purple-800',
                'Remote': 'bg-indigo-100 text-indigo-800',
                'Internship': 'bg-orange-100 text-orange-800'
            }.get(job_type, 'bg-gray-100 text-gray-800')
            
            ui.label(job_type).classes(f'px-3 py-1 rounded-full text-xs font-medium {badge_color}')
        
        # Job image or placeholder at the top of the card
        # image_url = job.get('image_url') or (job.get('images', [{}])[0] if isinstance(job.get('images'), list) and job.get('images') else None)
        # if isinstance(image_url, dict):
        #     image_url = image_url.get('url', '')
            
        # if image_url and isinstance(image_url, str) and image_url.startswith(('http://', 'https://')):
        #     ui.image(image_url).classes('w-full h-40 object-cover')
        ui.image(job.get('flyer')).classes('w-full h-40 object-cover')
        
        with ui.column().classes('p-6 h-full'):
            # Company logo placeholder and info
            with ui.row().classes('items-center gap-4 mb-4'):
                # Company avatar
                with ui.avatar().classes('bg-gradient-to-br from-blue-500 to-indigo-600 text-white text-lg font-bold'):
                    company_name = job.get('posted_by', 'Company')
                    ui.label(company_name[0].upper() if company_name else 'C')
                
                with ui.column().classes('flex-1'):
                    ui.label(job.get('title', 'No Title')).classes(
                        'text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors line-clamp-2'
                    )
                    ui.label(job.get('posted_by', 'Unknown Company')).classes(
                        'text-gray-600 font-medium'
                    )
            
            # Location and date
            with ui.row().classes('items-center gap-4 mb-4 text-sm text-gray-500'):
                with ui.row().classes('items-center gap-1'):
                    ui.icon('location_on', size='sm').classes('text-gray-400')
                    ui.label(job.get('location', 'Remote'))
                
                with ui.row().classes('items-center gap-1'):
                    ui.icon('schedule', size='sm').classes('text-gray-400')
                    posted_date = job.get('date_posted', '')
                    if posted_date:
                        try:
                            date_obj = datetime.strptime(posted_date, '%Y-%m-%d')
                            days_ago = (datetime.now() - date_obj).days
                            if days_ago == 0:
                                ui.label('Today')
                            elif days_ago == 1:
                                ui.label('1 day ago')
                            else:
                                ui.label(f'{days_ago} days ago')
                        except:
                            ui.label(posted_date)
                    else:
                        ui.label('Recently posted')
            
            # Job description preview
            description = job.get('description', '')
            if description:
                preview = description[:120] + '...' if len(description) > 120 else description
                ui.label(preview).classes('text-gray-600 text-sm mb-4 line-clamp-3')
            
            # Show additional database fields if available
            additional_info = []
            if job.get('experience_level'):
                additional_info.append(f"Experience: {job['experience_level']}")
            if job.get('education_required'):
                additional_info.append(f"Education: {job['education_required']}")
            if job.get('remote_work_available'):
                additional_info.append("Remote Available")
            
            if additional_info:
                ui.label(' • '.join(additional_info)).classes('text-xs text-blue-600 mb-2')
            
            # Salary and category
            with ui.row().classes('items-center justify-between mt-auto'):
                # Salary
                if job.get('salary_min') or job.get('salary_max'):
                    salary_parts = []
                    currency = job.get('currency', '$')
                    if job.get('salary_min'):
                        salary_parts.append(f"{currency}{job['salary_min']:,}")
                    if job.get('salary_max'):
                        salary_parts.append(f"{currency}{job['salary_max']:,}")
                    salary_text = ' - '.join(salary_parts)
                    ui.label(salary_text).classes('text-lg font-bold text-green-600')
                else:
                    ui.label('Salary not specified').classes('text-sm text-gray-500')
                
                # Category tag
                category = job.get('category', 'General')
                ui.label(category).classes(
                    'px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-xs font-medium'
                )
            
            # Action buttons
            with ui.row().classes('gap-2 mt-4 pt-4 border-t border-gray-100'):
                ui.button('View Details', on_click=lambda e, j=job: (e.stopPropagation(), ui.navigate.to(f'/view-job/{j.get("id", "")}'))).classes(
                    'flex-1 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-colors'
                )
                ui.button('Quick Apply', on_click=lambda e, j=job: (e.stopPropagation(), ui.navigate.to(f'/view-job/{j.get("id", "")}'))).classes(
                    'flex-1 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 transition-colors'
                )

def filter_jobs(search_term, location):
    """Filter jobs based on search criteria."""
    ui.notify(f'Searching for "{search_term}" in "{location}"', type='info')
    # TODO: Implement actual filtering logic

def toggle_filter(filter_option):
    """Toggle job type filter."""
    ui.notify(f'Filter toggled: {filter_option}', type='info')
    # TODO: Implement filter toggle logic

def quick_apply(job):
    """Quick apply to job."""
    ui.notify(f'Quick apply to {job.get("title", "job")}', type='positive')
