from nicegui import ui
from components.header import show_header
# Removed page_header import as it's no longer needed

# Sample candidates data
sample_candidates = [
    {
        'id': '1',
        'name': 'Alex Johnson',
        'title': 'Senior Software Engineer',
        'experience': '8 years',
        'skills': ['Python', 'JavaScript', 'React', 'Node.js', 'AWS'],
        'location': 'San Francisco, CA',
        'availability': 'Available in 2 weeks',
        'rate': '$120-150/hr',
        'image': 'https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=200&q=80',
        'bio': 'Experienced full-stack developer with a passion for building scalable web applications.'
    },
    {
        'id': '2',
        'name': 'Sarah Williams',
        'title': 'UX/UI Designer',
        'experience': '5 years',
        'skills': ['Figma', 'Sketch', 'Adobe XD', 'User Research', 'Prototyping'],
        'location': 'New York, NY',
        'availability': 'Available now',
        'rate': '$90-120/hr',
        'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=200&q=80',
        'bio': 'Creative designer focused on creating intuitive and beautiful user experiences.'
    },
    {
        'id': '3',
        'name': 'Michael Chen',
        'title': 'Data Scientist',
        'experience': '6 years',
        'skills': ['Python', 'Machine Learning', 'TensorFlow', 'SQL', 'Data Visualization'],
        'location': 'Remote',
        'availability': 'Available in 1 month',
        'rate': '$130-170/hr',
        'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80',
        'bio': 'Data scientist with expertise in machine learning and data-driven decision making.'
    }
]

def create_candidate_card(candidate):
    """Create a candidate card component."""
    with ui.card().classes('w-full hover:shadow-lg transition-shadow duration-300'):
        with ui.row().classes('w-full items-start'):
            # Candidate Image
            ui.image(candidate['image']).classes('w-20 h-20 rounded-full object-cover')
            
            # Candidate Info
            with ui.column().classes('ml-4 flex-1'):
                ui.label(candidate['name']).classes('text-xl font-semibold')
                ui.label(candidate['title']).classes('text-gray-600')
                
                # Skills
                with ui.row().classes('flex-wrap gap-2 mt-2'):
                    for skill in candidate['skills'][:4]:
                        ui.label(skill).classes('px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full')
                
                # Location and Availability
                with ui.row().classes('items-center text-sm text-gray-600 mt-2'):
                    ui.icon('location_on', size='1rem')
                    ui.label(candidate['location'])
                    ui.icon('schedule', size='1rem').classes('ml-3')
                    ui.label(candidate['availability'])
                
                # Bio
                ui.label(candidate['bio']).classes('text-gray-700 mt-2 text-sm')
            
            # Rate and Action
            with ui.column().classes('items-end justify-between'):
                ui.label(candidate['rate']).classes('text-lg font-semibold text-emerald-600')
                ui.button('View Profile', on_click=lambda c=candidate: show_candidate_profile(c['id'])) \
                    .classes('bg-emerald-600 text-white hover:bg-emerald-700')

def show_candidates_page():
    """Display the candidates listing page."""
    show_header()
    
    # Page header with background
    with ui.column().classes('w-full relative h-80 bg-cover bg-center'):
        ui.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1920&q=80") \
            .classes('absolute inset-0 w-full h-full object-cover')
        ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20')
        with ui.column().classes('relative z-10 h-full flex items-center'):
            with ui.column().classes('container mx-auto px-4 sm:px-6 lg:px-8 py-12'):
                ui.label("Find Top Talent").classes('text-4xl md:text-5xl font-bold text-white')
                ui.label("Connect with skilled professionals ready to join your team").classes('mt-2 text-lg md:text-xl text-white/90 max-w-3xl')
    
    # Main content
    with ui.column().classes('w-full bg-gray-50 -mt-20'):
        # Search and filters
        with ui.column().classes('w-full max-w-7xl mx-auto px-4 lg:px-8 py-8'):
            with ui.card().classes('w-full p-6'):
                with ui.row().classes('w-full items-end gap-4'):
                    # Search input
                    with ui.column().classes('flex-1'):
                        ui.label('Search candidates').classes('text-sm font-medium text-gray-700')
                        ui.input(placeholder='Job title, skills, or keywords').classes('w-full')
                    
                    # Location filter
                    with ui.column().classes('w-64'):
                        ui.label('Location').classes('text-sm font-medium text-gray-700')
                        ui.select(
                            options=['All Locations', 'Remote', 'New York', 'San Francisco', 'London', 'Berlin'],
                            value='All Locations'
                        ).classes('w-full')
                    
                    # Experience filter
                    with ui.column().classes('w-48'):
                        ui.label('Experience').classes('text-sm font-medium text-gray-700')
                        ui.select(
                            options=['Any', 'Entry Level', 'Mid Level', 'Senior', 'Lead'],
                            value='Any'
                        ).classes('w-full')
                    
                    # Search button
                    ui.button('Search', icon='search').classes('h-10 bg-emerald-600 text-white')
        
        # Candidates list
        with ui.column().classes('w-full max-w-7xl mx-auto px-4 lg:px-8 pb-12'):
            with ui.row().classes('w-full items-center justify-between mb-6'):
                ui.label('Available Candidates').classes('text-2xl font-bold text-gray-900')
                ui.label(f'Showing {len(sample_candidates)} candidates').classes('text-gray-500')
            
            # Candidates grid
            with ui.column().classes('w-full space-y-4'):
                for candidate in sample_candidates:
                    create_candidate_card(candidate)

def show_candidate_profile(candidate_id: str):
    """Display a single candidate's profile."""
    candidate = next((c for c in sample_candidates if c['id'] == candidate_id), None)
    
    if not candidate:
        with ui.column().classes('w-full h-screen flex items-center justify-center'):
            ui.label('Candidate not found').classes('text-2xl text-gray-500')
            ui.button('Back to Candidates', on_click=lambda: ui.navigate.to('/candidates'))
        return
    
    show_header()
    
    # Candidate header with background
    with ui.column().classes('w-full relative h-80 bg-cover bg-center'):
        ui.image("https://images.unsplash.com/photo-1521737711867-a3b9057faa50?auto=format&fit=crop&w=1920&q=80") \
            .classes('absolute inset-0 w-full h-full object-cover')
        ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20')
        with ui.column().classes('relative z-10 h-full flex items-center'):
            with ui.column().classes('container mx-auto px-4 sm:px-6 lg:px-8 py-12'):
                ui.label(candidate['name']).classes('text-4xl md:text-5xl font-bold text-white')
                ui.label(candidate['title']).classes('mt-2 text-lg md:text-xl text-white/90')
    
    with ui.column().classes('w-full min-h-screen bg-gray-50 -mt-20'):
        # Candidate info card floating over the header
        with ui.column().classes('w-full max-w-7xl mx-auto px-4 lg:px-8 relative z-10'):
            with ui.row().classes('bg-white rounded-xl shadow-lg p-6 items-start -mt-16'):
                # Candidate Image
                ui.image(candidate['image']).classes('w-32 h-32 rounded-full bg-white p-1 border-4 border-white shadow-lg')
                
                # Candidate Info
                with ui.column().classes('ml-6 flex-1'):
                    ui.label(candidate['name']).classes('text-3xl font-bold text-gray-900')
                    ui.label(candidate['title']).classes('text-xl text-gray-600 mb-4')
                    
                    with ui.row().classes('items-center space-x-6'):
                        with ui.row().classes('items-center'):
                            ui.icon('location_on', color='gray-500')
                            ui.label(candidate['location']).classes('text-gray-700')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('work', color='gray-500')
                            ui.label(f"{candidate['experience']} experience").classes('text-gray-700')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('schedule', color='gray-500')
                            ui.label(candidate['availability']).classes('text-gray-700')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('attach_money', color='gray-500')
                            ui.label(candidate['rate']).classes('text-gray-700 font-medium')
                    
                    # Action buttons
                    with ui.row().classes('mt-4 space-x-3'):
                        ui.button('Contact Candidate', icon='email').classes('bg-emerald-600 text-white')
                        ui.button('Download CV', icon='file_download').props('outline')
        
        # Main Content
        with ui.row().classes('w-full max-w-7xl mx-auto p-8 gap-8'):
            # Left Content
            with ui.column().classes('w-full lg:w-2/3 space-y-6'):
                # About Section
                with ui.card().classes('w-full p-6'):
                    ui.label('About').classes('text-2xl font-semibold text-gray-900 mb-4')
                    ui.label(candidate['bio']).classes('text-gray-700 leading-relaxed')
                
                # Skills Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Skills & Expertise').classes('text-2xl font-semibold text-gray-900 mb-4')
                    with ui.row().classes('flex-wrap gap-2'):
                        for skill in candidate['skills']:
                            ui.label(skill).classes('px-3 py-1.5 bg-blue-100 text-blue-800 text-sm rounded-full')
                
                # Experience Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Work Experience').classes('text-2xl font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-4'):
                        # Example experience item
                        with ui.column():
                            ui.label('Senior Software Engineer').classes('text-lg font-medium text-gray-900')
                            ui.label('TechCorp Solutions • 2019 - Present').classes('text-gray-600')
                            ui.label('San Francisco, CA').classes('text-gray-600 text-sm')
                            ui.label('Led a team of developers to build scalable web applications using React and Node.js.').classes('text-gray-700 mt-2')
            
            # Right Sidebar
            with ui.column().classes('w-full lg:w-1/3 space-y-6'):
                # Contact Information
                with ui.card().classes('w-full p-6'):
                    ui.label('Contact Information').classes('text-xl font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-3'):
                        with ui.row().classes('items-center'):
                            ui.icon('email', color='gray-500')
                            ui.label('email@example.com').classes('text-gray-700')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('phone', color='gray-500')
                            ui.label('+1 (555) 123-4567').classes('text-gray-700')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('language', color='gray-500')
                            ui.label('www.example.com').classes('text-blue-600 hover:underline cursor-pointer')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('location_on', color='gray-500')
                            ui.label(candidate['location']).classes('text-gray-700')
                
                # Social Links
                with ui.card().classes('w-full p-6'):
                    ui.label('Connect').classes('text-xl font-semibold text-gray-900 mb-4')
                    with ui.row().classes('space-x-4'):
                        ui.button(icon='linkedin').props('flat color=primary')
                        ui.button(icon='github').props('flat color=primary')
                        ui.button(icon='twitter').props('flat color=primary')
                
                # Similar Candidates
                with ui.card().classes('w-full p-6'):
                    ui.label('Similar Candidates').classes('text-xl font-semibold text-gray-900 mb-4')
                    with ui.column().classes('space-y-4'):
                        for similar in [c for c in sample_candidates if c['id'] != candidate_id]:
                            with ui.row().classes('items-center space-x-3 p-2 hover:bg-gray-50 rounded-lg cursor-pointer'):
                                ui.image(similar['image']).classes('w-12 h-12 rounded-full')
                                with ui.column().classes('flex-1'):
                                    ui.label(similar['name']).classes('font-medium')
                                    ui.label(similar['title']).classes('text-sm text-gray-600')
                                ui.icon('chevron_right', color='gray-400')

# Register routes
ui.page('/candidates')(show_candidates_page)
ui.page('/candidates/{candidate_id}')(show_candidate_profile)
