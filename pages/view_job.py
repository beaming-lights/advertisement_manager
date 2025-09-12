from nicegui import ui
from components.header import show_header
from utils.api_client import api_client
from datetime import datetime, timedelta
import random
import string
import asyncio
import httpx
from typing import Dict, Any, List, Optional, Union

async def fetch_job(job_id: str) -> Optional[Dict[str, Any]]:
    """Fetch a single job by ID from the API."""
    try:
        # Replace with your actual API endpoint
        url = f"https://api.example.com/jobs/{job_id}"  # Update this with your actual API endpoint
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
            return None
    except Exception as e:
        print(f"Error fetching job {job_id}: {e}")
        return None

def get_demo_job(job_id: str = None):
    """Return a demo job with realistic data for testing.
    
    Args:
        job_id: Optional job ID to generate consistent demo data for the same ID
    """
    # Use the provided job_id or generate a consistent one based on the input
    demo_id = job_id or 'demo123'
    random.seed(hash(demo_id))  # For consistent demo data generation
    
    # List of possible job templates
    job_templates = [
        {
            'title': 'Senior Software Engineer',
            'category': 'Technology',
            'description': (
                'We are looking for an experienced Senior Software Engineer to join our team. '
                'You will be responsible for developing and maintaining high-quality software solutions '
                'that meet our clients needs. The ideal candidate has a strong background in software development '
                'and is passionate about creating efficient and scalable applications.'
            ),
            'requirements': (
                '• 5+ years of experience in software development\n'
                '• Strong proficiency in Python, JavaScript, or similar languages\n'
                '• Experience with modern web frameworks (e.g., React, Vue, Angular)\n'
                '• Knowledge of database design and optimization\n'
                '• Excellent problem-solving and communication skills'
            ),
            'benefits': (
                '• Competitive salary and equity\n'
                '• Health, dental, and vision insurance\n'
                '• 401(k) matching\n'
                '• Flexible work hours and remote work options\n'
                '• Professional development budget'
            ),
            'flyer': 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'title': 'UX/UI Designer',
            'category': 'Design',
            'description': (
                'We are seeking a talented UX/UI Designer to create amazing user experiences. '
                'The ideal candidate should have an eye for clean and artful design, possess superior UI skills '
                'and be able to translate high-level requirements into beautiful, intuitive, and functional designs.'
            ),
            'requirements': (
                '• 3+ years of UX/UI design experience\n'
                '• Strong portfolio of design projects\n'
                '• Proficiency in Figma, Sketch, or Adobe XD\n'
                '• Experience with user research and testing\n'
                '• Understanding of front-end development (HTML/CSS/JS)'
            ),
            'benefits': (
                '• Competitive salary\n'
                '• Health and wellness benefits\n'
                '• Remote work flexibility\n'
                '• Creative work environment\n'
                '• Professional development opportunities'
            ),
            'flyer': 'https://images.unsplash.com/photo-1547658719-da2b51169166?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'title': 'Data Scientist',
            'category': 'Data Science',
            'description': (
                'We are looking for a Data Scientist to analyze large amounts of raw information to find patterns '
                'that will help improve our company. We will rely on you for building data products to extract '
                'valuable business insights and to optimize and improve our product development.'
            ),
            'requirements': (
                '• Strong problem-solving skills with an emphasis on product development\n'
                '• Experience using statistical computer languages (R, Python, etc.)\n'
                '• Knowledge of advanced statistical techniques and concepts\n'
                '• Experience with distributed data/computing tools\n'
                '• Excellent written and verbal communication skills'
            ),
            'benefits': (
                '• Competitive salary with stock options\n'
                '• Comprehensive health benefits\n'
                '• Flexible work arrangements\n'
                '• Learning and development budget\n'
                '• Cutting-edge technology stack'
            ),
            'flyer': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        }
    ]
    
    # Select a template based on the job_id for consistency
    template = job_templates[hash(demo_id) % len(job_templates)]
    
    # Generate consistent company name based on job_id
    companies = [
        'TechCorp Inc.', 'InnovateX', 'DataSphere', 'WebCraft', 'ByteForge',
        'CodePulse', 'Nexus Systems', 'Quantum Leap', 'PixelPioneers', 'CloudHarbor'
    ]
    company = companies[hash(demo_id) % len(companies)]
    
    # Generate consistent location
    locations = [
        'San Francisco, CA', 'New York, NY', 'Austin, TX', 'Seattle, WA',
        'Boston, MA', 'Chicago, IL', 'Denver, CO', 'Remote', 'London, UK', 'Berlin, Germany'
    ]
    location = locations[hash(demo_id) % len(locations)]
    
    # Generate salary based on job title
    salary_ranges = {
        'Senior': (120000, 180000),
        'Lead': (150000, 220000),
        'Junior': (70000, 100000),
        'Mid-level': (90000, 130000),
        '': (80000, 150000)  # Default range
    }
    
    # Find matching salary range
    salary_range = None
    for prefix, s_range in salary_ranges.items():
        if template['title'].startswith(prefix):
            salary_range = s_range
            break
    
    if not salary_range:
        salary_range = salary_ranges['']
    
    # Add some variation based on job_id
    salary_min = salary_range[0] + (hash(demo_id) % 20000)
    salary_max = salary_range[1] + (hash(demo_id) % 20000)
    
    # Generate random but consistent dates
    days_ago = (hash(demo_id) % 30) + 1  # 1-30 days ago
    deadline_days = (hash(demo_id) % 30) + 15  # 15-45 days from now
    
    return {
        'id': demo_id,
        'title': template['title'],
        'description': template['description'],
        'posted_by': company,
        'location': location,
        'employment_type': random.choice(['Full-time', 'Contract', 'Part-time', 'Internship']),
        'category': template['category'],
        'salary_min': salary_min,
        'salary_max': salary_max,
        'currency': 'USD',
        'date_posted': (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d'),
        'application_deadline': (datetime.now() + timedelta(days=deadline_days)).strftime('%Y-%m-%d'),
        'job_status': 'Active',
        'flyer': template['flyer'],
        'requirements': template['requirements'],
        'benefits': template['benefits']
    }

@ui.page('/job/{job_id}')
async def show_view_job_page(job_id: str):
    """Show detailed view of a single job.
    
    Args:
        job_id: The ID of the job to display.
    """
    show_header()
    
    # Create a container for the content
    container = ui.column().classes('w-full max-w-6xl mx-auto p-4')
    
    # Show loading state
    with container:
        with ui.row().classes('w-full justify-center'):
            ui.spinner('dots')
            ui.label('Loading job details...')
    
    # Try to find the job in the provided data
    job = None
    try:
        # This is a temporary solution - in a real app, you'd fetch from an API
        jobs_data = {
            "68c054195d0595ad9961d880": {
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
            "68c15cf1c2aebe868e3e939c": {
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
            "68c296cf95dd00811c919bac": {
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
            "68c29828b511afd27fdcfda0": {
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
        }
        
        job = jobs_data.get(job_id)
    except Exception as e:
        with container:
            container.clear()
            with ui.column().classes('items-center justify-center text-center p-8'):
                ui.icon('error_outline', size='xl').classes('text-red-500 text-5xl mb-4')
                ui.label('Error Loading Job').classes('text-2xl font-bold text-gray-800 mb-2')
                ui.label(f'An error occurred while loading the job: {str(e)}').classes('text-gray-600 mb-6')
                ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs'))\
                    .classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors')
    
    # Clear the loading state and show the job details
    container.clear()
    if job:
        # Create the job view with the found job
        create_job_view(job, job_id)
    else:
        # Show job not found message
        with container:
            with ui.column().classes('items-center justify-center text-center p-8'):
                ui.icon('error_outline', size='xl').classes('text-red-500 text-5xl mb-4')
                ui.label('Job Not Found').classes('text-2xl font-bold text-gray-800 mb-2')
                ui.label('The job you are looking for does not exist or has been removed.').classes('text-gray-600 mb-6')
                ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs'))\
                    .classes('bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors')

async def delete_job(job_id: str):
    """Handle job deletion - redirects to jobs page."""
    ui.navigate.to('/jobs')

def create_job_view(job: Dict[str, Any], job_id: str):
    """Create the job details view with the given job data."""
    with ui.column().classes('w-full bg-gray-50 min-h-screen'):
        # Header with back button and title
        with ui.row().classes('w-full items-center p-4 bg-white shadow-sm'):
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/jobs'))\
                .props('flat color=primary')
            ui.label('Job Details').classes('text-2xl font-bold text-gray-800')
        
        # Hero section with job image and basic info
        with ui.column().classes('w-full relative'):
            # Job image with gradient overlay
            if job.get('flyer'):
                with ui.element('div').classes('relative w-full h-96 overflow-hidden'):
                    ui.image(job['flyer']).classes('w-full h-full object-cover')
                    # Gradient overlay
                    with ui.element('div').classes('absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent'):
                        pass
            
            # Job title and company overlay
            with ui.column().classes('absolute bottom-0 left-0 right-0 p-8'):
                with ui.column().classes('max-w-6xl mx-auto w-full'):
                    ui.label(job.get('title', 'No Title')).classes('text-4xl font-bold text-white')
                    ui.label(job.get('posted_by', 'Company not specified')).classes('text-xl text-gray-200')
                    
                    # Job meta info
                    with ui.row().classes('mt-4 gap-6 flex-wrap'):
                        if job.get('employment_type'):
                            with ui.row().classes('items-center gap-2 bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full'):
                                ui.icon('work', size='sm').classes('text-white')
                                ui.label(job['employment_type']).classes('text-white text-sm')
                        
                        if job.get('location'):
                            with ui.row().classes('items-center gap-2 bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full'):
                                ui.icon('location_on', size='sm').classes('text-white')
                                ui.label(job['location']).classes('text-white text-sm')
                        
                        if job.get('date_posted'):
                            with ui.row().classes('items-center gap-2 bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full'):
                                ui.icon('event', size='sm').classes('text-white')
                                ui.label(f"Posted: {job['date_posted']}").classes('text-white text-sm')
                    
                    # Salary information if available
                    if job.get('salary_min') or job.get('salary_max'):
                        with ui.row().classes('mt-3 items-center gap-2 bg-green-600/90 backdrop-blur-sm px-4 py-2 rounded-lg'):
                            ui.icon('attach_money', size='sm').classes('text-white')
                            salary_parts = []
                            if job.get('salary_min'):
                                salary_parts.append(f"${job['salary_min']:,}")
                            if job.get('salary_max'):
                                salary_parts.append(f"${job['salary_max']:,}")
                            salary_text = ' - '.join(salary_parts)
                            if job.get('currency'):
                                salary_text += f" {job['currency']}"
                            ui.label(salary_text).classes('text-white font-semibold')
                            if job.get('employment_type') == 'Contract':
                                ui.label('/hr').classes('text-white/80 text-sm')
            
        # Main content area
        with ui.column().classes('max-w-4xl mx-auto w-full px-4 py-8'):
            # Action buttons
            with ui.row().classes('w-full justify-end gap-3 mb-8'):
                ui.button('Save Job', icon='bookmark_border', on_click=lambda: save_job(job))\
                    .props('outline')
                ui.button('Apply Now', icon='send', on_click=lambda: apply_to_job(job))\
                    .classes('bg-blue-600 text-white hover:bg-blue-700')
                
                with ui.menu() as share_menu:
                    ui.menu_item('Copy Link', lambda: copy_to_clipboard(f"{ui.page.url}"))
                    ui.menu_item('Share via Email', lambda: share_via_email(job))
                    ui.menu_item('Share on LinkedIn', lambda: share_via_linkedin(job))
                
                ui.button('Share', icon='share', on_click=share_menu.open).props('outline')
            
            # Job details card
            with ui.card().classes('w-full mb-6 overflow-hidden'):
                # Job description section
                with ui.column().classes('p-6'):
                    ui.label('Job Description').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Job type and location
                    with ui.row().classes('flex-wrap gap-4 mb-6'):
                        if job.get('employment_type'):
                            with ui.row().classes('items-center gap-2 text-gray-600'):
                                ui.icon('work', size='sm')
                                ui.label(job['employment_type'])
                        
                        if job.get('location'):
                            with ui.row().classes('items-center gap-2 text-gray-600'):
                                ui.icon('location_on', size='sm')
                                ui.label(job['location'])
                        
                        if job.get('date_posted'):
                            with ui.row().classes('items-center gap-2 text-gray-600'):
                                ui.icon('event', size='sm')
                                ui.label(f"Posted: {job['date_posted']}")
                    
                    # Job description
                    description = job.get('description', 'No description provided.')
                    if isinstance(description, str):
                        with ui.column().classes('prose max-w-none'):
                            ui.markdown(description)
                
                # Requirements section
                requirements = job.get('requirements')
                if requirements:
                    with ui.column().classes('bg-gray-50 p-6 border-t'):
                        ui.label('Requirements').classes('text-xl font-semibold text-gray-800 mb-3')
                        if isinstance(requirements, str):
                            with ui.column().classes('prose max-w-none'):
                                ui.markdown(requirements.replace('• ', '- '))
                
                # Benefits section
                benefits = job.get('benefits')
                if benefits:
                    with ui.column().classes('bg-white p-6 border-t'):
                        ui.label('Benefits').classes('text-xl font-semibold text-gray-800 mb-3')
                        if isinstance(benefits, str):
                            with ui.column().classes('prose max-w-none'):
                                ui.markdown(benefits.replace('• ', '- '))
                
                # Application deadline
                if job.get('application_deadline'):
                    with ui.row().classes('bg-blue-50 p-4 w-full items-center justify-between'):
                        with ui.column():
                            ui.label('Application Deadline').classes('text-sm font-medium text-gray-600')
                            ui.label(job['application_deadline']).classes('text-lg font-semibold text-gray-800')
                        
                        ui.button('Apply Now', icon='send', on_click=lambda: apply_to_job(job))\
                            .classes('bg-blue-600 text-white hover:bg-blue-700')
                
                # Footer with share options
                with ui.row().classes('bg-gray-50 p-4 w-full justify-between items-center border-t'):
                    ui.label('Share this job:').classes('text-gray-600')
                    
                    with ui.row().classes('gap-2'):
                        def create_share_button(icon, color, action):
                            return ui.button(icon=icon, on_click=action)
                        
                        create_share_button('link', 'gray', lambda: copy_to_clipboard(ui.page.url))\
                            .props('flat color=gray-600')
                        create_share_button('mail', 'gray', lambda: share_via_email(job))\
                            .props('flat color=gray-600')
                        create_share_button('share', 'gray', lambda: share_job(job))\
                            .props('flat color=gray-600')
                
                # Benefits if available
                benefits = job.get('benefits')
                if benefits:
                    ui.label('Benefits').classes('text-lg font-semibold mt-6 mb-2')
                    if isinstance(benefits, str):
                        ui.html(f"<div class='prose max-w-none'>{benefits}</div>")
            
            # Action buttons
            with ui.row().classes('w-full justify-between items-center mt-4'):
                # Back button
                ui.button('← Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).props('flat')
                
                # Right-aligned action buttons
                with ui.row().classes('gap-2'):
                    # Apply button with external link if available, otherwise show disabled button
                    apply_url = job.get('apply_url') or job.get('application_url') or job.get('apply_link')
                    if apply_url:
                        ui.button('Apply Now', on_click=lambda: ui.open(apply_url)).props('color=primary')
                    else:
                        ui.button('Apply Now').props('disabled color=primary')
                    
                    # Save/Bookmark button
                    ui.button(icon='bookmark_border').props('flat')
                    
                    # Share button
                    ui.button(icon='share').props('flat')
                    
                    # Create a container for the delete dialog
                    with ui.column() as delete_container:
                        with ui.dialog().classes('w-full max-w-md') as delete_dialog, \
                             ui.card().classes('w-full p-4'):
                            
                            with ui.column().classes('items-center gap-4 w-full'):
                                ui.icon('warning', size='xl').classes('text-red-500 text-4xl')
                                ui.label('Delete Job').classes('text-xl font-semibold')
                                ui.label('Are you sure you want to delete this job? This action cannot be undone.').classes('text-gray-600 text-center')
                                
                                with ui.row().classes('w-full justify-end gap-3 mt-4'):
                                    ui.button('Cancel', on_click=delete_dialog.close).classes('px-6')
                                    ui.button('Delete Job', 
                                        on_click=lambda: (
                                            delete_dialog.close(),
                                            ui.navigate.to('/jobs')  # Direct navigation without async
                                        )
                                    ).classes('bg-red-600 text-white hover:bg-red-700 px-6')
                        
                        # Delete button that opens the confirmation dialog
                        ui.button(icon='delete', 
                            on_click=delete_dialog.open
                        ).props('flat color=red').tooltip('Delete Job')

def display_job_image(image_url, title='Image'):
    """Simple function to display a job image"""
    with ui.card().classes('w-64 hover:shadow-lg transition-shadow'):
        ui.image(image_url).classes('w-full h-40 object-cover')
        with ui.card_section():
            ui.label(title).classes('text-sm font-medium')

def display_api_image(image):
    """Simple display for API images"""
    if isinstance(image, dict) and image.get('url'):
        display_job_image(image['url'], image.get('name', 'Image'))

def apply_to_job(job):
    """Handle job application"""
    ui.notify('Application feature coming soon!', type='info')

def save_job(job):
    """Save job to user's saved jobs"""
    ui.notify('Job saved to your favorites!', type='positive')

def share_job(job):
    """Share job via different methods"""
    with ui.dialog() as dialog, ui.card().classes('p-4'):
        ui.label('Share this job').classes('text-lg font-bold mb-4')
        
        job_url = f"https://yoursite.com/job/{job.get('id', '')}"
        
        with ui.column().classes('gap-3'):
            ui.input('Job URL', value=job_url, readonly=True).classes('w-full')
            
            with ui.row().classes('gap-2'):
                ui.button('Copy Link', on_click=lambda: copy_to_clipboard(job_url)).classes('bg-blue-500 text-white')
                ui.button('Email', on_click=lambda: share_via_email(job)).classes('bg-green-500 text-white')
                ui.button('LinkedIn', on_click=lambda: share_via_linkedin(job)).classes('bg-blue-700 text-white')
            
            ui.button('Close', on_click=dialog.close).classes('bg-gray-500 text-white mt-4')
    
    dialog.open()

def copy_to_clipboard(text):
    """Copy text to clipboard"""
    ui.run_javascript(f'navigator.clipboard.writeText("{text}")')
    ui.notify('Link copied to clipboard!', type='positive')

def share_via_email(job):
    """Share job via email"""
    subject = f"Job Opportunity: {job.get('title', 'Job')}"
    body = f"Check out this job opportunity:\n\n{job.get('title', 'Job')} at {job.get('posted_by', 'Company')}\nLocation: {job.get('location', 'N/A')}\n\nView details: https://yoursite.com/job/{job.get('id', '')}"
    mailto_url = f"mailto:?subject={subject}&body={body}"
    ui.run_javascript(f'window.open("{mailto_url}")')

def share_via_linkedin(job):
    """Share job via LinkedIn"""
    url = f"https://yoursite.com/job/{job.get('id', '')}"
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={url}"
    ui.run_javascript(f'window.open("{linkedin_url}", "_blank")')
