from nicegui import ui

def show_footer():
    """Creates a JobCamp-style footer with links and company information."""
    with ui.column().classes('w-full bg-gray-900 text-white'):
        # Main Footer Content
        with ui.row().classes('w-full py-16 px-4'):
            with ui.column().classes('w-full max-w-7xl mx-auto'):
                with ui.row().classes('w-full gap-8 lg:gap-16'):
                    # Company Info Column
                    with ui.column().classes('flex-1 space-y-4'):
                        ui.label('Jobcamp').classes('text-2xl font-bold text-white mb-4')
                        ui.label('Most comprehensive job portal. Find your dream job from thousands of opportunities worldwide.').classes('text-gray-300 leading-relaxed max-w-sm')
                        
                        # Social Media Links
                        with ui.row().classes('space-x-4 mt-6'):
                            ui.button(icon='facebook').props('flat round').classes('text-gray-400 hover:text-white hover:bg-blue-600 transition-colors')
                            ui.button(icon='twitter').props('flat round').classes('text-gray-400 hover:text-white hover:bg-blue-400 transition-colors')  
                            ui.button(icon='linkedin').props('flat round').classes('text-gray-400 hover:text-white hover:bg-blue-700 transition-colors')
                            ui.button(icon='instagram').props('flat round').classes('text-gray-400 hover:text-white hover:bg-pink-600 transition-colors')
                    
                    # Quick Links Column
                    with ui.column().classes('flex-1 space-y-4'):
                        ui.label('Quick Links').classes('text-lg font-semibold text-white mb-4')
                        footer_links = [
                            ('Home', '/'),
                            ('Browse Jobs', '/jobs'),
                            ('Companies', '/companies'),
                            ('Post a Job', '/post-job'),
                            ('About Us', '/about'),
                            ('Contact', '/contact')
                        ]
                        for link_text, link_url in footer_links:
                            ui.link(link_text, link_url).classes('text-gray-300 hover:text-white transition-colors block py-1')
                    
                    # For Job Seekers Column
                    with ui.column().classes('flex-1 space-y-4'):
                        ui.label('For Job Seekers').classes('text-lg font-semibold text-white mb-4')
                        seeker_links = [
                            ('Search Jobs', '/jobs'),
                            ('Career Advice', '/advice'),
                            ('Resume Builder', '/resume'),
                            ('Salary Guide', '/salary'),
                            ('Job Alerts', '/alerts'),
                            ('Success Stories', '/stories')
                        ]
                        for link_text, link_url in seeker_links:
                            ui.link(link_text, link_url).classes('text-gray-300 hover:text-white transition-colors block py-1')
                    
                    # For Employers Column
                    with ui.column().classes('flex-1 space-y-4'):
                        ui.label('For Employers').classes('text-lg font-semibold text-white mb-4')
                        employer_links = [
                            ('Post Jobs', '/post-job'),
                            ('Search Candidates', '/candidates'),
                            ('Pricing Plans', '/pricing'),
                            ('Employer Resources', '/resources'),
                            ('Recruitment Tips', '/tips'),
                            ('Company Profiles', '/profiles')
                        ]
                        for link_text, link_url in employer_links:
                            ui.link(link_text, link_url).classes('text-gray-300 hover:text-white transition-colors block py-1')
        
        # Bottom Footer Bar
        with ui.row().classes('w-full border-t border-gray-700 py-6 px-4'):
            with ui.row().classes('w-full max-w-7xl mx-auto justify-between items-center'):
                ui.label('© 2024 Jobcamp. All rights reserved.').classes('text-gray-400')
                
                # Legal Links
                with ui.row().classes('space-x-6'):
                    ui.link('Privacy Policy', '/privacy').classes('text-gray-400 hover:text-white transition-colors')
                    ui.link('Terms of Service', '/terms').classes('text-gray-400 hover:text-white transition-colors')
                    ui.link('Cookie Policy', '/cookies').classes('text-gray-400 hover:text-white transition-colors')

def show_newsletter_section():
    """Creates a newsletter signup section with background image."""
    with ui.row().classes('w-full py-16 px-4 relative overflow-hidden'):
        # Background gradient as fallback
        with ui.element('div').classes('absolute inset-0 bg-blue-50'):
            pass
        
        # Background image using ui.image
        ui.image('https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1280&q=80').classes('absolute inset-0 w-full h-full object-cover opacity-20')
        
        with ui.column().classes('w-full max-w-4xl mx-auto text-center relative z-10'):
            ui.label('Stay Updated with Latest Jobs').classes('text-3xl lg:text-4xl font-bold text-gray-900 mb-4')
            ui.label('Get notified about new job opportunities that match your skills and preferences.').classes('text-xl text-gray-600 mb-8 max-w-2xl mx-auto')
            
            # Newsletter Signup Form
            with ui.card().classes('w-full max-w-2xl mx-auto bg-white/95 backdrop-blur border border-gray-200 shadow-lg rounded-2xl p-2'):
                with ui.row().classes('w-full gap-2'):
                    email_input = ui.input('Enter your email address').classes('flex-1 border-0 bg-gray-50 rounded-xl px-4 py-3 text-gray-800').props('outlined=false')
                    ui.button('Subscribe', on_click=lambda: subscribe_newsletter(email_input.value)).classes('bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-xl transition-colors')
            
            ui.label('Join 50,000+ professionals already subscribed').classes('text-sm text-gray-500 mt-4')

def subscribe_newsletter(email):
    """Handle newsletter subscription."""
    if email and '@' in email:
        ui.notify(f'Thank you! We\'ve subscribed {email} to our newsletter.', type='positive')
    else:
        ui.notify('Please enter a valid email address.', type='warning')
