from nicegui import ui
from components.header import show_header
from components.footer import show_footer
# Removed page_header import as it's no longer needed
from pages.add_event import global_job_listings

# Sample company data
sample_company = {
    'id': '1',
    'name': 'TechCorp Solutions',
    'tagline': 'Building the future of technology',
    'industry': 'Technology & Software',
    'founded': '2015',
    'size': '500-1000 employees',
    'location': 'San Francisco, CA',
    'website': 'www.techcorp.com',
    'email': 'careers@techcorp.com',
    'phone': '+1 (555) 987-6543',
    'logo': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?auto=format&fit=crop&w=200&q=80',
    'cover_image': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80',
    'about': 'TechCorp Solutions is a leading technology company specializing in innovative software solutions for businesses worldwide. We are passionate about creating cutting-edge products that transform how companies operate and grow. Our team of talented professionals works collaboratively to deliver exceptional results for our clients.',
    'mission': 'To empower businesses through innovative technology solutions that drive growth, efficiency, and success in the digital age.',
    'values': ['Innovation', 'Collaboration', 'Excellence', 'Integrity', 'Customer Focus'],
    'benefits': [
        'Competitive salary and equity packages',
        'Comprehensive health, dental, and vision insurance',
        'Flexible work arrangements and remote options',
        'Professional development and learning opportunities',
        'Generous PTO and sabbatical programs',
        'State-of-the-art office facilities',
        'Team building events and company retreats'
    ],
    'stats': {
        'employees': '750+',
        'offices': '12',
        'countries': '8',
        'clients': '500+'
    },
    'social_links': {
        'linkedin': 'https://linkedin.com/company/techcorp',
        'twitter': 'https://twitter.com/techcorp',
        'facebook': 'https://facebook.com/techcorp',
        'instagram': 'https://instagram.com/techcorp'
    },
    'team_members': [
        {
            'name': 'Sarah Johnson',
            'title': 'CEO & Founder',
            'image': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?auto=format&fit=crop&w=150&q=80'
        },
        {
            'name': 'Michael Chen',
            'title': 'CTO',
            'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=150&q=80'
        },
        {
            'name': 'Emily Rodriguez',
            'title': 'Head of Design',
            'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80'
        },
        {
            'name': 'David Kim',
            'title': 'VP of Engineering',
            'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80'
        }
    ]
}

def show_company_profile_page(company_id: str = None):
    """Display company profile page."""
    show_header()
    
    # Use sample data for now, but filter by company_id if provided
    company = sample_company if str(sample_company.get('id', '1')) == str(company_id) else None
    
    if not company:
        with ui.column().classes('w-full h-screen flex items-center justify-center'):
            ui.label('Company not found').classes('text-2xl text-gray-500')
            ui.button('Back to Companies', on_click=lambda: ui.navigate.to('/companies'))
        return
    
    # Company header with background
    with ui.column().classes('w-full relative h-80 bg-cover bg-center'):
        ui.image(company['cover_image']).classes('absolute inset-0 w-full h-full object-cover')
        ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20')
        with ui.column().classes('relative z-10 h-full flex items-center'):
            with ui.column().classes('container mx-auto px-4 sm:px-6 lg:px-8 py-12'):
                ui.label(company['name']).classes('text-4xl md:text-5xl font-bold text-white')
                if company.get('tagline'):
                    ui.label(company['tagline']).classes('mt-2 text-lg md:text-xl text-white/90')
    
    # Main content
    
    with ui.column().classes('w-full min-h-screen bg-gray-50 -mt-20'):
        # Company info card floating over the header
        with ui.column().classes('w-full max-w-7xl mx-auto px-4 lg:px-8 relative z-10'):
            with ui.row().classes('bg-white rounded-xl shadow-lg p-6 items-center -mt-16'):
                # Company Logo
                ui.image(company['logo']).classes('w-24 h-24 rounded-lg bg-white p-2 mr-6 shadow-lg')
                
                # Company Info
                with ui.column():
                    with ui.row().classes('items-center space-x-4'):
                        ui.label(f"📍 {company['location']}").classes('text-gray-600')
                        ui.label(f"👥 {company['size']}").classes('text-gray-600')
                        ui.label(f"🏢 {company['industry']}").classes('text-gray-600')
                        ui.label(f"📅 Founded {company['founded']}").classes('text-gray-600')
        
        # Main Content
        with ui.row().classes('w-full max-w-7xl mx-auto p-8 gap-8'):
            # Left Content
            with ui.column().classes('w-full lg:w-2/3 space-y-6'):
                # About Section
                with ui.card().classes('w-full p-6'):
                    ui.label('About Us').classes('text-2xl font-semibold text-gray-900 mb-4')
                    ui.label(company['about']).classes('text-gray-700 leading-relaxed mb-4')
                    
                    ui.label('Our Mission').classes('text-lg font-semibold text-gray-900 mb-2')
                    ui.label(company['mission']).classes('text-gray-700 leading-relaxed')
                
                # Company Stats
                with ui.card().classes('w-full p-6'):
                    ui.label('Company Stats').classes('text-2xl font-semibold text-gray-900 mb-4')
                    with ui.grid(columns=4).classes('gap-4'):
                        for key, value in company['stats'].items():
                            with ui.column().classes('text-center'):
                                ui.label(value).classes('text-3xl font-bold text-blue-600')
                                ui.label(key.title()).classes('text-sm text-gray-600')
                
                # Values Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Our Values').classes('text-2xl font-semibold text-gray-900 mb-4')
                    with ui.row().classes('flex-wrap gap-3'):
                        for value in company['values']:
                            ui.label(value).classes('bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm')
                
                # Benefits Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Benefits & Perks').classes('text-2xl font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-2'):
                        for benefit in company['benefits']:
                            with ui.row().classes('items-center'):
                                ui.icon('check_circle').classes('text-green-500 mr-3')
                                ui.label(benefit).classes('text-gray-700')
                
                # Team Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Leadership Team').classes('text-2xl font-semibold text-gray-900 mb-6')
                    with ui.grid(columns=2).classes('gap-6'):
                        for member in company['team_members']:
                            with ui.row().classes('items-center'):
                                ui.image(member['image']).classes('w-16 h-16 rounded-full object-cover mr-4')
                                with ui.column():
                                    ui.label(member['name']).classes('font-semibold text-gray-900')
                                    ui.label(member['title']).classes('text-gray-600')
            
            # Right Sidebar
            with ui.column().classes('w-full lg:w-1/3 space-y-6'):
                # Contact Info
                with ui.card().classes('w-full p-6'):
                    ui.label('Contact Information').classes('text-xl font-semibold text-gray-900 mb-4')
                    
                    contact_items = [
                        ('language', 'Website', company['website']),
                        ('email', 'Email', company['email']),
                        ('phone', 'Phone', company['phone']),
                        ('business', 'Industry', company['industry'])
                    ]
                    
                    for icon, label, value in contact_items:
                        with ui.column().classes('mb-4'):
                            ui.label(label).classes('text-sm text-gray-500 mb-1')
                            with ui.row().classes('items-center'):
                                ui.icon(icon).classes('text-gray-400 mr-2')
                                if label == 'Website':
                                    ui.link(value, f'https://{value}', new_tab=True).classes('text-blue-600 hover:underline')
                                elif label == 'Email':
                                    ui.link(value, f'mailto:{value}').classes('text-blue-600 hover:underline')
                                elif label == 'Phone':
                                    ui.link(value, f'tel:{value}').classes('text-blue-600 hover:underline')
                                else:
                                    ui.label(value).classes('text-gray-900 font-medium')
                
                # Social Links
                with ui.card().classes('w-full p-6'):
                    ui.label('Follow Us').classes('text-xl font-semibold text-gray-900 mb-4')
                    with ui.row().classes('space-x-3'):
                        for platform, url in company['social_links'].items():
                            icon_map = {
                                'linkedin': 'fab fa-linkedin-in',
                                'twitter': 'fab fa-twitter',
                                'facebook': 'fab fa-facebook-f',
                                'instagram': 'fab fa-instagram'
                            }
                            ui.button(
                                icon=icon_map.get(platform, 'link'),
                                on_click=lambda url=url: ui.navigate.to(url, new_tab=True)
                            ).props('flat round').classes('text-gray-600 hover:text-blue-600')
                
                # Quick Actions
                with ui.card().classes('w-full p-6'):
                    ui.label('Quick Actions').classes('text-xl font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-3'):
                        ui.button('View All Jobs', icon='work', on_click=lambda: ui.navigate.to('/jobs')).props('unelevated').classes('w-full bg-blue-600 text-white')
                        ui.button('Follow Company', icon='favorite').props('outline').classes('w-full border-gray-300 text-gray-700')
                        ui.button('Share Profile', icon='share').props('outline').classes('w-full border-gray-300 text-gray-700')
        
        # Open Positions Section
        with ui.column().classes('w-full max-w-7xl mx-auto p-8'):
            with ui.card().classes('w-full p-6'):
                with ui.row().classes('w-full justify-between items-center mb-6'):
                    ui.label('Open Positions').classes('text-2xl font-semibold text-gray-900')
                    ui.button('View All Jobs', on_click=lambda: ui.navigate.to('/jobs')).props('flat').classes('text-blue-600')
                
                # Job Listings
                company_jobs = [job for job in global_job_listings if 'TechCorp' in job.get('company', '')][:3]
                
                if company_jobs:
                    with ui.column().classes('space-y-4'):
                        for job in company_jobs:
                            with ui.card().classes('p-4 hover:shadow-md transition-shadow cursor-pointer'):
                                with ui.row().classes('w-full justify-between items-start'):
                                    with ui.column().classes('flex-1'):
                                        ui.label(job['title']).classes('text-lg font-semibold text-gray-900 mb-1')
                                        with ui.row().classes('items-center space-x-4 text-sm text-gray-600 mb-2'):
                                            ui.label(f"📍 {job.get('location', 'Remote')}")
                                            ui.label(f"💼 {job.get('type', 'Full-time')}")
                                            ui.label(f"💰 {job.get('salary', '$80k - $120k')}")
                                        ui.label(job.get('description', '')[:150] + '...').classes('text-gray-700 text-sm')
                                    
                                    with ui.column().classes('text-right'):
                                        ui.button('Apply Now', on_click=lambda job_id=job['id']: ui.navigate.to(f'/jobs/{job_id}')).props('unelevated').classes('bg-blue-600 text-white')
                else:
                    with ui.column().classes('text-center py-8'):
                        ui.icon('work_off').classes('text-6xl text-gray-300 mb-4')
                        ui.label('No open positions at the moment').classes('text-gray-500')
                        ui.label('Check back later for new opportunities!').classes('text-sm text-gray-400')
    
    show_footer()

def show_company_list_page():
    """Display list of companies."""
    show_header()
    
    with ui.column().classes('w-full max-w-7xl mx-auto p-4 md:p-8'):
        # Header
        with ui.row().classes('w-full justify-between items-center mb-8'):
            ui.label('Companies').classes('text-4xl font-bold text-gray-900')
            
            # Filters
            with ui.row().classes('space-x-4'):
                ui.select(['All Industries', 'Technology', 'Finance', 'Healthcare'], value='All Industries').classes('min-w-48')
                ui.select(['All Sizes', 'Startup', 'Mid-size', 'Enterprise'], value='All Sizes').classes('min-w-48')
        
        # Company Grid
        with ui.grid(columns=2).classes('w-full gap-6'):
            # Sample companies
            companies = [
                {'name': 'TechCorp Solutions', 'industry': 'Technology', 'employees': '500-1000', 'jobs': 12},
                {'name': 'FinanceFlow Inc', 'industry': 'Finance', 'employees': '200-500', 'jobs': 8},
                {'name': 'HealthTech Pro', 'industry': 'Healthcare', 'employees': '100-200', 'jobs': 15},
                {'name': 'DataDrive Systems', 'industry': 'Technology', 'employees': '50-100', 'jobs': 6},
                {'name': 'GreenEnergy Co', 'industry': 'Energy', 'employees': '1000+', 'jobs': 20},
                {'name': 'EduTech Solutions', 'industry': 'Education', 'employees': '200-500', 'jobs': 10}
            ]
            
            for i, company in enumerate(companies):
                with ui.card().classes('p-6 hover:shadow-lg transition-shadow cursor-pointer'):
                    with ui.row().classes('items-start mb-4'):
                        # Company Logo
                        ui.image(f'https://images.unsplash.com/photo-156047235{i+1}-b33ff0c44a43?auto=format&fit=crop&w=100&q=80').classes('w-16 h-16 rounded-lg object-cover mr-4')
                        
                        # Company Info
                        with ui.column().classes('flex-1'):
                            ui.label(company['name']).classes('text-xl font-semibold text-gray-900 mb-1')
                            ui.label(company['industry']).classes('text-gray-600 mb-2')
                            
                            with ui.row().classes('text-sm text-gray-500 space-x-4'):
                                ui.label(f"👥 {company['employees']}")
                                ui.label(f"💼 {company['jobs']} open jobs")
                    
                    # View Company Button
                    ui.button('View Company', on_click=lambda: ui.navigate.to('/company-profile/1')).props('flat').classes('w-full text-blue-600')
    
    show_footer()
