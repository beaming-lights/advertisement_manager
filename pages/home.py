from nicegui import ui, app
from datetime import datetime
from components.header import show_header
from components.footer import show_footer, show_newsletter_section
from .add_event import global_job_listings

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

def show_home_page():
    """Creates the JobCamp-style home page."""
    show_header()
    
    # JobCamp Hero Section
    with ui.column().classes('w-full'):
        # Main Hero Container - JobCamp style
        with ui.row().classes('w-full bg-white py-20 px-4'):
            with ui.column().classes('w-full max-w-7xl mx-auto'):
                with ui.row().classes('w-full items-center gap-16'):
                    # Left Column - Hero Content
                    with ui.column().classes('flex-1 space-y-8'):
                        ui.label('Get hired by the popular teams.').classes('text-5xl lg:text-6xl font-bold text-gray-900 leading-tight')
                        ui.label('Creating a beautiful job website is not easy always. To make your life easier, we are introducing Jobcamp template.').classes('text-xl text-gray-600 leading-relaxed max-w-2xl')
                        
                        # Search Bar - JobCamp style
                        with ui.card().classes('w-full max-w-2xl bg-white border border-gray-200 shadow-lg rounded-2xl p-2'):
                            with ui.row().classes('w-full gap-2'):
                                job_search = ui.input('Job title, keywords...').classes('flex-1 border-0 bg-gray-50 rounded-xl px-4 py-3 text-gray-800').props('outlined=false')
                                location_search = ui.input('Location').classes('flex-1 border-0 bg-gray-50 rounded-xl px-4 py-3 text-gray-800').props('outlined=false')
                                ui.button('Search Jobs', on_click=lambda: search_jobs(job_search.value, location_search.value)).classes('bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-xl transition-colors')
                        
                        # Stats Row - JobCamp style
                        with ui.row().classes('w-full gap-8 mt-8'):
                            with ui.column().classes('text-center'):
                                ui.label('295').classes('text-3xl font-bold text-blue-600')
                                ui.label('New jobs posted today').classes('text-sm text-gray-600')
                            with ui.column().classes('text-center'):
                                ui.label('14').classes('text-3xl font-bold text-blue-600')
                                ui.label('New companies registered').classes('text-sm text-gray-600')
                    
                    # Right Column - Hero Image from Pixabay
                    with ui.column().classes('flex-1 hidden lg:flex items-center justify-center'):
                        with ui.card().classes('w-full h-96 border-0 relative overflow-hidden rounded-2xl shadow-2xl'):
                            # Background gradient as fallback
                            with ui.element('div').classes('absolute inset-0 bg-gradient-to-br from-blue-500 to-purple-600'):
                                pass
                            
                            # Hero image
                            ui.image('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1280&q=80').classes('absolute inset-0 w-full h-full object-cover')
                            
                            # Gradient overlay
                            with ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-blue-600/70 to-purple-600/70'):
                                pass
                            
                            # Overlay content
                            with ui.column().classes('relative z-10 items-center justify-center h-full text-center p-8'):
                                ui.label('Find Your Dream Job').classes('text-3xl font-bold text-white mb-4')
                                ui.label('Join thousands of professionals').classes('text-lg text-white/90 mb-6')
                                
                                # Floating benefit chips
                                with ui.row().classes('space-x-4 flex-wrap justify-center'):
                                    ui.chip('Remote Work').classes('bg-white/20 backdrop-blur text-white border border-white/30')
                                    ui.chip('High Salary').classes('bg-white/20 backdrop-blur text-white border border-white/30')
                                    ui.chip('Great Benefits').classes('bg-white/20 backdrop-blur text-white border border-white/30')

        # How It Works Section - JobCamp style
        with ui.row().classes('w-full py-20 px-4 bg-gray-50'):
            with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
                ui.label('Easy steps to land your next job').classes('text-4xl lg:text-5xl font-bold text-gray-900 mb-16')
                
                with ui.row().classes('w-full justify-center gap-8 lg:gap-12'):
                    # Step 1 - JobCamp style
                    with ui.column().classes('text-center max-w-sm'):
                        with ui.card().classes('w-20 h-20 mx-auto mb-6 bg-blue-100 border-0 flex items-center justify-center rounded-2xl'):
                            ui.icon('person_add', size='xl', color='blue-600')
                        ui.label('Register Your Account').classes('text-2xl font-bold text-gray-900 mb-4')
                        ui.label('Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital.').classes('text-gray-600 leading-relaxed')
                    
                    # Step 2 - JobCamp style
                    with ui.column().classes('text-center max-w-sm'):
                        with ui.card().classes('w-20 h-20 mx-auto mb-6 bg-green-100 border-0 flex items-center justify-center rounded-2xl'):
                            ui.icon('search', size='xl', color='green-600')
                        ui.label('Apply for New Jobs').classes('text-2xl font-bold text-gray-900 mb-4')
                        ui.label('Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches.').classes('text-gray-600 leading-relaxed')
                    
                    # Step 3 - JobCamp style
                    with ui.column().classes('text-center max-w-sm'):
                        with ui.card().classes('w-20 h-20 mx-auto mb-6 bg-purple-100 border-0 flex items-center justify-center rounded-2xl'):
                            ui.icon('celebration', size='xl', color='purple-600')
                        ui.label('Get Hired Immediately').classes('text-2xl font-bold text-gray-900 mb-4')
                        ui.label('Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital.').classes('text-gray-600 leading-relaxed')

        # Featured Jobs Section - JobCamp style
        with ui.row().classes('w-full py-20 px-4 bg-white'):
            with ui.column().classes('w-full max-w-7xl mx-auto'):
                ui.label('Featured Jobs').classes('text-4xl lg:text-5xl font-bold text-gray-900 text-center mb-16')
                
                # Job Grid - JobCamp style
                if not global_job_listings:
                    with ui.card().classes('w-full p-12 text-center border border-gray-200'):
                        ui.icon('work_off', size='xl', color='gray-400').classes('mx-auto mb-4')
                        ui.label('No jobs posted yet').classes('text-xl font-medium text-gray-600 mb-2')
                        ui.label('Be the first to post a job and find great talent!').classes('text-gray-500 mb-4')
                        ui.button('Post Your First Job', on_click=lambda: ui.open('/post-job'), color='primary').classes('px-8 py-3')
                else:
                    with ui.row().classes('w-full gap-6 flex-wrap'):
                        for job in global_job_listings[:6]:  # Show first 6 jobs
                            create_jobcamp_job_card(job)
                
                # View More Jobs Button
                with ui.row().classes('w-full justify-center mt-12'):
                    ui.button('View All Jobs', on_click=lambda: ui.open('/jobs')).classes('bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-xl transition-colors')
        
        # Company Logos Section with reliable images
        company_images = [
            'https://images.unsplash.com/photo-1611224923853-80b023f02d71?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
            'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80'
        ]
        
        with ui.row().classes('w-full py-16 px-4 bg-gray-50'):
            with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
                ui.label('Trusted by leading companies worldwide').classes('text-2xl font-bold text-gray-900 mb-12')
                
                with ui.row().classes('w-full flex-wrap justify-center gap-8'):
                    for i, img_url in enumerate(company_images):
                        with ui.card().classes('w-20 h-20 bg-white border border-gray-200 flex items-center justify-center rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 overflow-hidden'):
                            ui.image(img_url).classes('w-12 h-12 object-cover rounded-lg')

        # Stats Section with Background Image - JobCamp style
        with ui.row().classes('w-full py-20 px-4 relative overflow-hidden'):
            # Background gradient as fallback
            with ui.element('div').classes('absolute inset-0 bg-blue-600'):
                pass
            
            # Background image using ui.image
            ui.image('https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&auto=format&fit=crop&w=1280&q=80').classes('absolute inset-0 w-full h-full object-cover opacity-30')
            
            with ui.column().classes('w-full max-w-7xl mx-auto text-center relative z-10'):
                ui.label('Over 50k+ people landed their first job from Jobcamp.').classes('text-3xl lg:text-4xl font-bold text-white mb-4')
                ui.label('Join companies from anywhere in the world.').classes('text-xl text-blue-100 mb-12')
                
                with ui.row().classes('w-full justify-center gap-16'):
                    with ui.column().classes('text-center'):
                        ui.label('50,000+').classes('text-4xl font-bold text-white')
                        ui.label('Jobs Posted').classes('text-blue-200')
                    with ui.column().classes('text-center'):
                        ui.label('25,000+').classes('text-4xl font-bold text-white')
                        ui.label('Companies').classes('text-blue-200')
                    with ui.column().classes('text-center'):
                        ui.label('100,000+').classes('text-4xl font-bold text-white')
                        ui.label('Happy Candidates').classes('text-blue-200')
        
        # Newsletter Section
        show_newsletter_section()
        
        # Footer
        show_footer()

def create_jobcamp_job_card(job):
    """Creates a JobCamp-style job card with reliable images."""
    with ui.card().classes('w-full lg:w-80 bg-white border border-gray-200 hover:border-blue-300 hover:shadow-lg transition-all duration-300 rounded-2xl p-6'):
        # Company logo and bookmark with reliable images
        with ui.row().classes('w-full justify-between items-start mb-4'):
            # Company avatars with Unsplash images for better reliability
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
        
        # Job title and company
        ui.link(job['job_title'], f"/jobs/{job['id']}").classes('text-xl font-bold text-gray-900 hover:text-blue-600 transition-colors mb-2 block')
        ui.label(job['company']).classes('text-gray-600 mb-4')
        
        # Job details
        with ui.row().classes('w-full justify-between items-center mb-4'):
            with ui.row().classes('items-center gap-1'):
                ui.icon('location_on', size='sm', color='gray-500')
                ui.label(job['location']).classes('text-sm text-gray-600')
            with ui.row().classes('items-center gap-1'):
                ui.icon('schedule', size='sm', color='gray-500')
                ui.label(job['job_type']).classes('text-sm text-gray-600')
        
        # Salary
        if job.get('salary_min') and job.get('salary_max'):
            salary_text = f"${job['salary_min']:,} - ${job['salary_max']:,}"
            ui.label(salary_text).classes('text-lg font-bold text-green-600 mb-4')
        
        # Apply button
        ui.button('Apply Now', on_click=lambda j=job: apply_to_job(j)).classes('w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-colors')

def create_job_card(job):
    """Creates a modern job card component with enhanced styling and animations."""
    with ui.card().classes('modern-card job-card w-full p-6 hover:shadow-2xl transition-all duration-300 cursor-pointer group animate-fade-in-up'):
        with ui.row().classes('w-full justify-between items-start mb-4'):
            with ui.column().classes('flex-1'):
                ui.link(job['job_title'], f"/jobs/{job['id']}").classes('text-xl lg:text-2xl font-bold text-gray-800 hover:text-primary transition-colors duration-300 group-hover:text-primary')
                with ui.row().classes('items-center space-x-2 mt-1'):
                    ui.icon('business', size='sm', color='primary')
                    ui.label(job['company']).classes('text-primary font-semibold text-lg')
            
            # Save button and posted date
            with ui.column().classes('items-end space-y-2'):
                ui.button(icon='bookmark_border', on_click=lambda: ui.notify('Job saved!')).props('flat round dense').classes('text-gray-400 hover:text-primary transition-colors')
                ui.label(format_date(job.get('posted_date'))).classes('text-sm text-gray-500 bg-gray-50 px-2 py-1 rounded-full')
        
        # Enhanced chips with better styling
        with ui.row().classes('w-full mb-4 flex-wrap gap-2'):
            location_text = f"{job['location']} {'🌍 Remote' if job.get('is_remote') else ''}"
            ui.chip(location_text, icon='location_on').classes('modern-chip chip-primary')
            ui.chip(job['job_type'], icon='schedule').classes('modern-chip chip-success')
            if job.get('experience_level'):
                ui.chip(job['experience_level'], icon='trending_up').classes('modern-chip')
        
        # Job description with better typography
        description = job.get('description', '')[:180] + ('...' if len(job.get('description', '')) > 180 else '')
        ui.label(description).classes('text-gray-600 mb-4 leading-relaxed text-base')
        
        # Enhanced salary display
        if job.get('salary_min') or job.get('salary_max'):
            salary_parts = []
            if job.get('salary_min'):
                salary_parts.append(f"${float(job['salary_min']):,.0f}")
            if job.get('salary_max'):
                salary_parts.append(f"${float(job['salary_max']):,.0f}")
            salary_text = ' - '.join(salary_parts)
            with ui.row().classes('items-center space-x-2 mb-4'):
                ui.icon('attach_money', color='positive')
                ui.label(salary_text).classes('text-xl font-bold text-green-600')
                ui.label('/year').classes('text-sm text-gray-500')
        
        # Skills tags if available
        if job.get('skills'):
            with ui.row().classes('w-full mb-4 flex-wrap gap-1'):
                for skill in job['skills'][:4]:  # Show max 4 skills
                    ui.badge(skill).classes('bg-blue-50 text-blue-700 text-xs px-2 py-1')
                if len(job.get('skills', [])) > 4:
                    ui.badge(f'+{len(job["skills"]) - 4} more').classes('bg-gray-100 text-gray-600 text-xs px-2 py-1')
        
        # Enhanced action buttons
        with ui.row().classes('w-full justify-between items-center pt-4 border-t border-gray-100'):
            ui.button('👁️ View Details', on_click=lambda j=job: ui.open(f"/jobs/{j['id']}")).classes('btn-secondary flex-1 mr-2')
            ui.button('🚀 Apply Now', on_click=lambda j=job: apply_to_job(j)).classes('btn-primary flex-1 ml-2')

def search_jobs(query, location):
    """Handle job search functionality."""
    ui.notify(f'Searching for "{query}" in "{location}"...', type='info')
    # In a real app, this would filter jobs and update the display
    ui.open('/jobs')

def view_job_details(job):
    """Navigate to job details page."""
    ui.notify(f'Viewing details for {job["title"]}', type='info')
    ui.open('/jobs')

def apply_to_job(job):
    """Handle job application."""
    if job.get('application_url'):
        ui.open(job['application_url'])
        ui.notify(f'Opening application page for {job["job_title"]}', type='info')
    else:
        ui.notify(f'Send your application to: {job["contact_email"]}', type='info')
