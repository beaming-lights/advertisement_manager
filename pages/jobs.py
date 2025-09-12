from nicegui import ui
from components.header import show_header
from utils.api_client import api_client
from datetime import datetime

def show_jobs_page():
    """Elegant job listings page with modern design with demo data."""
    show_header()
    
    with ui.column().classes('w-full min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100'):
        # Hero section with background image and overlay
        with ui.column().classes('w-full relative'):
            # Background image with darker overlay - reduced height
            with ui.column().classes('absolute inset-0 z-0 h-96'):
                ui.image('https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80')\
                    .classes('w-full h-full object-cover')
                with ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-black/70 via-black/60 to-black/50'):
                    pass
            
            # Centered title and subtitle
            with ui.column().classes('relative z-10 max-w-4xl mx-auto text-center py-24'):
                ui.label('Find Your Dream Job').classes('text-5xl md:text-6xl font-bold text-white leading-tight')
                ui.label('Discover opportunities that match your skills and passion')\
                    .classes('text-xl text-white/90 mt-4 max-w-2xl mx-auto')
                
        # Search section below hero
        with ui.column().classes('w-full bg-white shadow-sm -mt-10 z-20 relative'):
            with ui.column().classes('max-w-6xl mx-auto w-full px-8'):
                # Modern search bar with glass effect
                with ui.column().classes('w-full bg-white rounded-2xl p-6 shadow-lg border border-gray-200'):
                    # Search row - all elements in one line
                    with ui.row().classes('w-full items-end gap-4'):
                        with ui.column().classes('flex-1'):
                            ui.label('What are you looking for?').classes('text-gray-700 text-sm font-medium mb-1 whitespace-nowrap')
                            search_input = ui.input(placeholder='Job title, company, or keywords').classes(
                                'w-full bg-white border border-gray-200 text-gray-900 placeholder-gray-400 rounded-xl focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all hover:border-gray-300'
                            ).props('outlined dense')
                        
                        with ui.column().classes('flex-1'):
                            ui.label('Location').classes('text-gray-700 text-sm font-medium mb-1')
                            location_input = ui.input(placeholder='City, state, or remote').classes(
                                'w-full bg-white border border-gray-200 text-gray-900 placeholder-gray-400 rounded-xl focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all hover:border-gray-300'
                            ).props('outlined dense')
                        
                        ui.button('', icon='search').classes(
                            'h-10 bg-blue-600 text-white px-6 rounded-xl font-medium transition-all transform hover:scale-105 hover:bg-blue-700'
                        ).on('click', lambda: ui.notify('Search functionality is for demo purposes', type='info'))
                    
                    # Filter links
                    with ui.row().classes('gap-4 flex-wrap mt-4'):
                        filter_options = ['Full-time', 'Part-time', 'Remote', 'Contract', 'Internship']
                        for option in filter_options:
                            ui.link(option, 'javascript:void(0)').classes(
                                'text-gray-600 hover:text-blue-600 text-sm font-medium no-underline transition-colors'
                            ).on('click', lambda e, opt=option: toggle_filter(opt))
        
        # Main content area with demo jobs
        with ui.column().classes('max-w-6xl mx-auto p-8 w-full'):
            # Only show the first job from the list
            jobs = [
                {
                    "title": "Cleaning Job",
                    "description": "We make your home a haven.",
                    "category": "Sanitation",
                    "employment_type": "Freelance",
                    "location": "Osu",
                    "salary_min": 120000,
                    "salary_max": 15000000000,
                    "currency": "Dinar",
                    "posted_by": "Hydra",
                    "date_posted": "26-08-2025",
                    "application_deadline": "27-08-2026",
                    "job_status": "Closed",
                    "flyer": "https://res.cloudinary.com/dx5tbpgob/image/upload/v1757439787/six52qgly1m8hisamnlc.jpg",
                    "id": "68c054195d0595ad9961d880"
                },
                {
                    "title": "Join the Dream Team",
                    "description": "Become a good basketball player",
                    "category": "Sports",
                    "employment_type": "Full time",
                    "location": "Ablekuma",
                    "salary_min": 4200,
                    "salary_max": 45200,
                    "currency": "GHS",
                    "posted_by": "Hydra",
                    "date_posted": "45-10-56",
                    "application_deadline": "45-10-57",
                    "job_status": "Pending",
                    "flyer": "https://res.cloudinary.com/dx5tbpgob/image/upload/v1757502706/dqu3n652fgsirpxrfptp.jpg",
                    "id": "68c15cf1c2aebe868e3e939c"
                },
                {
                    "title": "Kill Bill",
                    "description": "Assassination Contract",
                    "category": "Killer Man",
                    "employment_type": "Freelance",
                    "location": "London",
                    "salary_min": 7500000,
                    "salary_max": 56210000,
                    "currency": "GHS",
                    "posted_by": "Vera Pomaa",
                    "date_posted": "4/12/27",
                    "application_deadline": "6/2/28",
                    "job_status": "open",
                    "flyer": "https://res.cloudinary.com/dx5tbpgob/image/upload/v1757583056/c4heyvqvubb27zndq1um.jpg",
                    "id": "68c296cf95dd00811c919bac"
                },
                {
                    "title": "Nanny Job",
                    "description": "I need to babysit my kin",
                    "category": "Humanities",
                    "employment_type": "Fulltime",
                    "location": "Canada - Ablekuma",
                    "salary_min": 4500,
                    "salary_max": 5320,
                    "currency": "USD",
                    "posted_by": "Kofi Asiamah",
                    "date_posted": "12/12/12",
                    "application_deadline": "12/12/25",
                    "job_status": "open",
                    "flyer": "https://res.cloudinary.com/dx5tbpgob/image/upload/v1757583399/jfrmm3e9mzb2aq5bmfc0.jpg",
                    "id": "68c29828b511afd27fdcfda0"
                }
            ]
               # Create a grid with 2 jobs per row
            with ui.column().classes('w-full max-w-7xl mx-auto px-4'):
                # Process jobs in pairs
                for i in range(0, min(len(jobs), 4), 2):
                    with ui.row().classes('w-full flex justify-between gap-4 mb-6'):
                        # First job in the pair
                        with ui.column().classes('flex-1'):
                            create_job_card(jobs[i])
                        # Second job in the pair (if exists)
                        if i + 1 < len(jobs):
                            with ui.column().classes('flex-1'):
                                create_job_card(jobs[i + 1])
                
                # Add some spacing at the bottom
                ui.space().classes('h-16')

def create_job_card(job):
    """Create an elegant job card with modern styling for demo jobs."""
    import random
    import string
    
    # Use the job's ID or generate a random one if not available
    job_id = job.get('id', ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)))
    
    with ui.card().classes('''
        w-full h-full flex flex-col hover:shadow-xl transition-all duration-200 
        border border-gray-200 rounded-lg overflow-hidden hover:border-blue-200
        hover:shadow-md m-0 p-0 flex-grow bg-white
    '''):
        # Job image with overlay - clickable area for the card
        with ui.element('div').classes('relative h-40 w-full bg-gray-100 cursor-pointer').on('click', lambda e, jid=job_id: ui.navigate.to(f'/job/{jid}')):
            if job.get('flyer'):
                ui.image(job['flyer']).classes('absolute inset-0 w-full h-full object-cover')
                # Gradient overlay
                with ui.element('div').classes('absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent'):
                    pass
                # Company name overlay with conditional New label
                with ui.column().classes('absolute bottom-0 left-0 p-4 w-full'):
                    with ui.row().classes('w-full justify-between items-end'):
                        ui.label(job.get('posted_by', 'Company Name')).classes('text-white font-medium text-lg')
                        # Show New label only for recent jobs (within 7 days)
                        posted_date = job.get('date_posted', '')
                        show_new = True
                        if posted_date:
                            try:
                                date_obj = datetime.strptime(posted_date, '%Y-%m-%d')
                                days_ago = (datetime.now() - date_obj).days
                                show_new = days_ago <= 7
                            except:
                                pass
                        
                        if show_new:
                            ui.label('New').classes('bg-green-500 text-white text-xs font-medium px-2 py-0.5 rounded-full')
            else:
                ui.icon('work_outline', size='xl').classes('absolute inset-0 m-auto text-gray-300')
        
        # Job details
        with ui.column().classes('p-6 flex-1 flex flex-col gap-3'):
            # Job title - larger and more prominent
            ui.label(job.get('title', 'Job Title')).classes('text-xl font-bold text-gray-900 leading-tight hover:text-blue-600 transition-colors')
            
            # Job type and location
            with ui.row().classes('items-center gap-2 mt-2 flex-wrap'):
                # Employment type as filter chip
                employment_type = job.get('employment_type', 'Full-time')
                with ui.row().classes('items-center gap-1.5 bg-blue-50 hover:bg-blue-100 px-3 py-1 rounded-full transition-colors border border-blue-200'):
                    ui.icon('work_outline', size='xs').classes('text-blue-600')
                    ui.label(employment_type).classes('text-xs font-medium text-blue-700')
                
                with ui.row().classes('items-center gap-1.5 text-gray-500'):
                    ui.icon('location_on', size='xs')
                    ui.label(job.get('location', 'Remote')).classes('text-sm')
            
            # Removed description preview - will only show in job details
            
            # Bottom section with date and view button
            # with ui.row().classes('items-center justify-between mt-auto pt-3 border-t border-gray-100'):
            #     # Posted date
            #     with ui.row().classes('items-center gap-1.5 text-xs text-gray-500'):
            #         # ui.icon('schedule', size='xs')
                    # posted_date = job.get('date_posted', '')
                    # if posted_date:
                    #     try:
                    #         date_obj = datetime.strptime(posted_date, '%Y-%m-%d')
                    #         days_ago = (datetime.now() - date_obj).days
                    #         if days_ago == 0:
                    #             ui.label('Today')
                    #         elif days_ago == 1:
                    #             ui.label('Yesterday')
                    #         else:
                    #             ui.label(f'{days_ago}d ago')
                    #     except:
                    #         ui.label('')
                    # else:
                    #     ui.label('')
                
                # # View Job button
                # ui.button('View Job', icon='arrow_forward', color='primary').props('flat dense').classes('text-xs font-medium')
            
            # Salary information if available
            if job.get('salary_min') or job.get('salary_max'):
                with ui.row().classes('items-center gap-2 mt-3 text-sm'):
                    ui.icon('attach_money', size='sm').classes('text-green-600')
                    salary_parts = []
                    if job.get('salary_min'):
                        salary_parts.append(f"${job['salary_min']:,}")
                    if job.get('salary_max'):
                        salary_parts.append(f"${job['salary_max']:,}")
                    salary_text = ' - '.join(salary_parts)
                    if job.get('currency'):
                        salary_text += f" {job['currency']}"
                    ui.label(salary_text).classes('font-medium')
            
            # Status badge
            job_status = job.get('job_status', '').lower()
            status_colors = {
                'open': 'bg-green-100 text-green-800',
                'closed': 'bg-red-100 text-red-800',
                'pending': 'bg-yellow-100 text-yellow-800',
                'draft': 'bg-gray-100 text-gray-800'
            }
            status_class = status_colors.get(job_status, 'bg-gray-100 text-gray-800')
            
            with ui.row().classes('items-center justify-between mt-4'):
                # Empty left side to maintain layout
                ui.space()
                
                # Right side: Action button
                ui.button('View Details', on_click=lambda e, jid=job_id: ui.navigate.to(f'/job/{jid}'))\
                    .classes('text-sm px-4 py-1 bg-blue-600 text-white hover:bg-blue-700')

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
