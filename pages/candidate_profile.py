from nicegui import ui
from components.header import show_header
from components.footer import show_footer

# Sample candidate data
sample_candidate = {
    'id': '1',
    'name': 'David Henricks',
    'title': 'Senior Product Designer',
    'location': 'New York, USA',
    'email': 'david.henricks@email.com',
    'phone': '+1 (555) 123-4567',
    'website': 'www.davidhenricks.com',
    'avatar': '/static/images/default-avatar.svg',
    'resume': None,  # Will store path to resume file
    'portfolio_url': 'www.davidhenricks.com/portfolio',
    'availability': 'Available for freelance work',
    'hourly_rate': 75,
    'preferred_work_type': ['Full-time', 'Remote', 'Contract'],
    'languages': ['English (Native)', 'Spanish (Intermediate)'],
    'about': 'A talented professional with an academic background in IT and proven commercial development experience as a Product Designer since 2015. Has a sound knowledge of the software development life cycle and user experience design. Was involved in more than 50+ design projects.',
    'achievements': [
        'Led a team of 5 designers to deliver a major product redesign',
        'Increased user engagement by 40% through improved UX',
        'Speaker at DesignConf 2023',
    ],
    'skills': ['UI/UX Design', 'Figma', 'Adobe Creative Suite', 'Prototyping', 'Wireframing', 'User Research', 'Agile', 'Design Systems'],
    'experience': [
        {
            'title': 'Lead Product Designer',
            'company': 'Airbnb',
            'duration': 'Jun 2020 - Present',
            'location': 'San Francisco, USA',
            'logo': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?auto=format&fit=crop&w=100&q=80'
        },
        {
            'title': 'Senior UI/UX Designer',
            'company': 'Google Inc',
            'duration': 'Mar 2018 - May 2020',
            'location': 'Mountain View, USA',
            'logo': 'https://images.unsplash.com/photo-1573804633927-bfcbcd909acd?auto=format&fit=crop&w=100&q=80'
        },
        {
            'title': 'Product Designer',
            'company': 'Spotify',
            'duration': 'Jan 2016 - Feb 2018',
            'location': 'New York, USA',
            'logo': 'https://images.unsplash.com/photo-1611532736597-de2d4265fba3?auto=format&fit=crop&w=100&q=80'
        }
    ],
    'education': [
        {
            'degree': 'Masters in Design',
            'school': 'Harvard University',
            'duration': '2014 - 2016',
            'location': 'Cambridge, USA',
            'logo': 'https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=100&q=80'
        },
        {
            'degree': 'Bachelor in Computer Science',
            'school': 'MIT',
            'duration': '2010 - 2014',
            'location': 'Cambridge, USA',
            'logo': 'https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=100&q=80'
        }
    ],
    'social_links': {
        'linkedin': 'https://linkedin.com/in/davidhenricks',
        'twitter': 'https://twitter.com/davidhenricks',
        'github': 'https://github.com/davidhenricks',
        'dribbble': 'https://dribbble.com/davidhenricks',
        'behance': 'https://behance.net/davidhenricks',
        'portfolio': 'https://davidhenricks.com',
        'medium': 'https://medium.com/@davidhenricks',
        'youtube': 'https://youtube.com/davidhenricks'
    }
}

def show_candidate_profile_page(candidate_id: str = None):
    """Display candidate profile page."""
    show_header()
    
    # Use sample data for now, but filter by candidate_id if provided
    candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
    
    if not candidate:
        with ui.column().classes('w-full h-screen flex items-center justify-center'):
            ui.label('Candidate not found').classes('text-2xl text-gray-500')
            ui.button('Back to Candidates', on_click=lambda: ui.navigate.to('/candidates'))
        return
    
    with ui.column().classes('w-full min-h-screen bg-gray-50'):
        # Edit button (top right)
        with ui.row().classes('w-full max-w-7xl mx-auto justify-end p-4'):
            ui.button('Edit Profile', on_click=lambda: ui.navigate.to(f'/candidate-profile/{candidate_id}/edit')) \
                .props('outline')
        # Main container
        with ui.row().classes('w-full max-w-7xl mx-auto p-4 md:p-8 gap-8'):
            # Left Sidebar - Contact Info
            with ui.column().classes('w-full lg:w-1/3 space-y-6'):
                # Profile Card
                with ui.card().classes('w-full p-6 text-center'):
                    # Profile Image
                    avatar_url = candidate.get('avatar', '/static/images/default-avatar.svg')
                    ui.image(avatar_url).classes('w-24 h-24 rounded-full mx-auto mb-4 object-cover')
                    
                    # Name and Title
                    ui.label(candidate['name']).classes('text-2xl font-bold text-gray-900 mb-2')
                    ui.label(candidate['title']).classes('text-lg text-gray-600 mb-4')
                    
                    # Social Links
                    with ui.row().classes('justify-center space-x-3 mb-6'):
                        for platform, url in candidate['social_links'].items():
                            icon_map = {
                                'linkedin': 'fab fa-linkedin-in',
                                'twitter': 'fab fa-twitter',
                                'github': 'fab fa-github',
                                'dribbble': 'fab fa-dribbble',
                                'behance': 'fab fa-behance',
                                'portfolio': 'fas fa-globe',
                                'medium': 'fab fa-medium',
                                'youtube': 'fab fa-youtube'
                            }
                            if platform in icon_map and url:
                                ui.button(
                                    icon=icon_map[platform],
                                    on_click=lambda url=url: ui.navigate.to(url, new_tab=True)
                                ).props('flat round').classes('text-gray-600 hover:text-blue-600')
                    
                    # Contact Info
                    with ui.column().classes('space-y-3 text-left'):
                        if candidate.get('email'):
                            with ui.row().classes('items-center'):
                                ui.icon('email').classes('text-gray-500')
                                ui.link(candidate['email'], f'mailto:{candidate["email"]}').classes('ml-2 text-gray-700 hover:text-blue-600')
                        
                        if candidate.get('phone'):
                            with ui.row().classes('items-center'):
                                ui.icon('phone').classes('text-gray-500')
                                ui.link(candidate['phone'], f'tel:{candidate["phone"].replace(" ", "")}').classes('ml-2 text-gray-700 hover:text-blue-600')
                        
                        if candidate.get('website'):
                            with ui.row().classes('items-center'):
                                ui.icon('language').classes('text-gray-500')
                                ui.link(candidate['website'], candidate['website'], new_tab=True).classes('ml-2 text-gray-700 hover:text-blue-600')
                        
                        if candidate.get('location'):
                            with ui.row().classes('items-center'):
                                ui.icon('location_on').classes('text-gray-500')
                                ui.label(candidate['location']).classes('ml-2 text-gray-700')
                    
                    # Resume Download
                    if candidate.get('resume'):
                        with ui.row().classes('w-full mt-6 justify-center'):
                            ui.button(
                                'Download Resume',
                                on_click=lambda: ui.navigate.to(candidate['resume']),
                                icon='file_download'
                            ).classes('w-full bg-blue-600 text-white hover:bg-blue-700')
                
                # Skills Card
                with ui.card().classes('w-full p-6'):
                    ui.label('Skills & Expertise').classes('text-lg font-semibold text-gray-900 mb-4')
                    with ui.row().classes('flex-wrap gap-2'):
                        for skill in candidate['skills']:
                            ui.label(skill).classes('px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm')
                
                # Work Preferences
                with ui.card().classes('w-full p-6'):
                    ui.label('Work Preferences').classes('text-lg font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-2'):
                        if candidate.get('preferred_work_type'):
                            with ui.row().classes('items-center'):
                                ui.icon('work').classes('text-gray-500')
                                ui.label(', '.join(candidate['preferred_work_type'])).classes('ml-2 text-gray-700')
                        
                        if candidate.get('hourly_rate'):
                            with ui.row().classes('items-center'):
                                ui.icon('attach_money').classes('text-gray-500')
                                ui.label(f"${candidate['hourly_rate']}/hr").classes('ml-2 text-gray-700')
                        
                        if candidate.get('availability'):
                            with ui.row().classes('items-center'):
                                ui.icon('event_available').classes('text-gray-500')
                                ui.label(candidate['availability']).classes('ml-2 text-gray-700')
                        
                        if candidate.get('languages'):
                            with ui.row().classes('items-start'):
                                ui.icon('language').classes('text-gray-500 mt-1')
                                with ui.column().classes('ml-2'):
                                    for lang in candidate['languages']:
                                        ui.label(lang).classes('text-gray-700')
            
            # Main Content
            with ui.column().classes('w-full lg:w-2/3 space-y-6'):
                # About Section
                with ui.card().classes('w-full p-6'):
                    ui.label('About Me').classes('text-xl font-semibold text-gray-900 mb-4')
                    ui.label(candidate['about']).classes('text-gray-700')
                
                # Experience Section
                with ui.card().classes('w-full p-6'):
                    with ui.row().classes('w-full justify-between items-center mb-4'):
                        ui.label('Work Experience').classes('text-xl font-semibold text-gray-900')
                    
                    for exp in candidate['experience']:
                        with ui.row().classes('w-full mb-6 pb-6 border-b border-gray-100 last:border-0 last:mb-0 last:pb-0'):
                            if exp.get('logo'):
                                ui.image(exp['logo']).classes('w-12 h-12 rounded-md object-cover mr-4')
                            
                            with ui.column().classes('flex-1'):
                                ui.label(exp['title']).classes('text-lg font-medium text-gray-900')
                                ui.label(exp['company']).classes('text-gray-700')
                                with ui.row().classes('items-center text-sm text-gray-500'):
                                    ui.icon('event').classes('text-sm')
                                    ui.label(exp['duration'])
                                    
                                    if exp.get('location'):
                                        ui.icon('location_on').classes('ml-4 text-sm')
                                        ui.label(exp['location'])
                
                # Education Section
                with ui.card().classes('w-full p-6'):
                    with ui.row().classes('w-full justify-between items-center mb-4'):
                        ui.label('Education').classes('text-xl font-semibold text-gray-900')
                    
                    for edu in candidate['education']:
                        with ui.row().classes('w-full mb-6 pb-6 border-b border-gray-100 last:border-0 last:mb-0 last:pb-0'):
                            if edu.get('logo'):
                                ui.image(edu['logo']).classes('w-12 h-12 rounded-md object-cover mr-4')
                            
                            with ui.column().classes('flex-1'):
                                ui.label(edu['degree']).classes('text-lg font-medium text-gray-900')
                                ui.label(edu['school']).classes('text-gray-700')
                                with ui.row().classes('items-center text-sm text-gray-500'):
                                    ui.icon('event').classes('text-sm')
                                    ui.label(edu['duration'])
                                    
                                    if edu.get('location'):
                                        ui.icon('location_on').classes('ml-4 text-sm')
                                        ui.label(edu['location'])
                
                # Portfolio/Projects Section
                if candidate.get('portfolio_url'):
                    with ui.card().classes('w-full p-6'):
                        with ui.row().classes('w-full justify-between items-center'):
                            ui.label('Portfolio').classes('text-xl font-semibold text-gray-900')
                            ui.link('View All', candidate['portfolio_url'], new_tab=True).classes('text-blue-600 hover:underline')
                        
                        # Add portfolio items grid here
                        with ui.row().classes('w-full mt-4 grid grid-cols-1 md:grid-cols-2 gap-4'):
                            # Sample portfolio items
                            portfolio_items = [
                                {'title': 'E-commerce Redesign', 'image': 'https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=500&q=80'},
                                {'title': 'Mobile App UI Kit', 'image': 'https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=500&q=80'},
                                {'title': 'Brand Identity', 'image': 'https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?auto=format&fit=crop&w=500&q=80'},
                                {'title': 'Web Dashboard', 'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=80'},
                            ]
                            
                            for item in portfolio_items:
                                with ui.column().classes('relative group cursor-pointer'):
                                    ui.image(item['image']).classes('w-full h-40 object-cover rounded-lg')
                                    with ui.column().classes('absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center rounded-lg'):
                                        ui.label(item['title']).classes('text-white font-medium')
                
                # Achievements Section
                if candidate.get('achievements'):
                    with ui.card().classes('w-full p-6'):
                        ui.label('Achievements').classes('text-xl font-semibold text-gray-900 mb-4')
                        with ui.column().classes('space-y-2'):
                            for achievement in candidate['achievements']:
                                with ui.row().classes('items-start'):
                                    ui.icon('check_circle').classes('text-green-500 mt-1')
                                    ui.label(achievement).classes('ml-2 text-gray-700')
    
    show_footer()

def show_candidate_list_page():
    """Display list of candidates."""
    show_header()
    
    with ui.column().classes('w-full max-w-7xl mx-auto p-4 md:p-8'):
        # Header
        with ui.row().classes('w-full justify-between items-center mb-8'):
            ui.label('Candidates').classes('text-4xl font-bold text-gray-900')
            
            # Filters
            with ui.row().classes('space-x-4'):
                ui.select(['All Positions', 'Designer', 'Developer', 'Manager'], value='All Positions').classes('min-w-48')
                ui.select(['All Locations', 'New York', 'San Francisco', 'Remote'], value='All Locations').classes('min-w-48')
        
        # Candidate Grid
        with ui.grid(columns=3).classes('w-full gap-6'):
            # Sample candidates
            for i in range(6):
                with ui.card().classes('p-6 hover:shadow-lg transition-shadow cursor-pointer'):
                    # Profile Image
                    ui.image(f'https://images.unsplash.com/photo-150700321{i+1}-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80').classes('w-20 h-20 rounded-full mx-auto mb-4 object-cover')
                    
                    # Name and Title
                    ui.label(f'Candidate {i+1}').classes('text-lg font-semibold text-gray-900 text-center mb-1')
                    ui.label('Product Designer').classes('text-gray-600 text-center mb-3')
                    
                    # Location
                    with ui.row().classes('justify-center items-center mb-4'):
                        ui.icon('location_on').classes('text-gray-400 text-sm mr-1')
                        ui.label('New York, USA').classes('text-sm text-gray-500')
                    
                    # Skills
                    with ui.row().classes('justify-center flex-wrap gap-1 mb-4'):
                        for skill in ['UI/UX', 'Figma', 'React']:
                            ui.label(skill).classes('text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded')
                    
                    # View Profile Button
                    ui.button('View Profile', on_click=lambda: ui.navigate.to('/candidate-profile/1')).props('flat').classes('w-full text-blue-600')
    
    show_footer()
