from nicegui import ui
from typing import Optional

# Global state
is_logged_in = False  # This would come from your auth system

def handle_logout():
    """Handle user logout."""
    global is_logged_in
    is_logged_in = False
    ui.navigate.to('/')
    ui.notify('You have been logged out', type='positive')

def show_mobile_menu():
    """Show mobile menu as a dialog instead of drawer to avoid nesting issues."""
    with ui.dialog() as mobile_dialog:
        with ui.card().classes('w-72 max-h-screen overflow-y-auto'):
            with ui.column().classes('w-full'):
                # User profile section
                with ui.column().classes('p-6 bg-gradient-to-r from-emerald-50 to-white'):
                    if is_logged_in:
                        with ui.row().classes('items-center space-x-3'):
                            ui.icon('account_circle', size='2.5rem', color='emerald-600')
                            with ui.column():
                                ui.label('John Doe').classes('font-medium text-gray-800')
                                ui.label('john@example.com').classes('text-xs text-gray-500')
                    else:
                        ui.label('Welcome!').classes('text-lg font-medium text-gray-800')
                        ui.label('Sign in to access your account').classes('text-sm text-gray-500')
                
                # Navigation links
                with ui.column().classes('p-4 space-y-1'):
                    nav_links = [
                        ('work', 'Jobs', '/jobs'),
                        ('business_center', 'Companies', '/companies'),
                        ('people', 'Candidates', '/candidates')
                    ]
                    
                    for icon, text, target in nav_links:
                        with ui.link().classes('w-full').on('click', lambda e, t=target: ui.navigate.to(t)):
                            with ui.row().classes('w-full items-center p-3 rounded-lg hover:bg-gray-50 transition-colors'):
                                ui.icon(icon, color='emerald-600').classes('text-lg')
                                ui.label(text).classes('ml-3 text-gray-700')
                    
                    # Auth buttons (only show when not logged in)
                    if not is_logged_in:
                        with ui.column().classes('w-full pt-4 mt-4 border-t border-gray-100 space-y-2'):
                            ui.button('Log In', on_click=lambda: ui.navigate.to('/login')) \
                                .classes('w-full bg-white text-emerald-600 border border-emerald-600 hover:bg-emerald-50')
                            ui.button('Sign Up', on_click=lambda: ui.navigate.to('/signup')) \
                                .classes('w-full bg-gradient-to-r from-emerald-600 to-teal-500 text-white hover:shadow-md')
                    else:
                        # User menu items
                        user_links = [
                            ('person', 'My Profile', '/candidate-profile/1'),
                            ('business', 'Company Profile', '/company-profile/1'),
                            ('settings', 'Settings', '/settings'),
                            ('help', 'Help & Support', '/help')
                        ]
                        
                        for icon, text, target in user_links:
                            with ui.link().classes('w-full').on('click', lambda e, t=target: ui.navigate.to(t)):
                                with ui.row().classes('w-full items-center p-3 rounded-lg hover:bg-gray-50 transition-colors'):
                                    ui.icon(icon, color='emerald-600').classes('text-lg')
                                    ui.label(text).classes('ml-3 text-gray-700')
                        
                        # Logout button
                        with ui.row().classes('w-full p-3 rounded-lg hover:bg-red-50 cursor-pointer', 
                                            on_click=handle_logout):
                            ui.icon('logout', color='red-500').classes('text-lg')
                            ui.label('Logout').classes('ml-3 text-red-600')
    
    mobile_dialog.open()

def show_header():
    """Creates a modern job board header with glassmorphism effect."""
    with ui.element('header').classes('w-full bg-white/90 backdrop-blur-lg fixed top-0 left-0 right-0 z-50 transition-all duration-300 border-b border-gray-200 shadow-sm'):
        with ui.row().classes('w-full max-w-7xl mx-auto px-4 lg:px-6 h-16 items-center'):
            # Logo and Brand
            with ui.link(target='#').classes('flex items-center space-x-3 no-underline group'):
                with ui.row().classes('w-9 h-9 bg-gradient-to-br from-emerald-500 to-teal-500 rounded-lg flex items-center justify-center transform transition-transform group-hover:rotate-12'):
                    ui.icon('work', color='white', size='1.2rem')
                ui.label('JobCamp').classes('text-xl font-bold text-gray-800')
                ui.element('a').props('href=/')
            
            # Add click handler for the logo
            ui.run_javascript("""
                document.querySelector('a[href="#"]').addEventListener('click', function(e) {
                    e.preventDefault();
                    window.location.href = '/';
                });
            """)
            
            # Desktop Navigation
            with ui.row().classes('hidden md:flex items-center space-x-8 ml-10'):
                # Simple text links
                nav_links = [
                    ('Jobs', '/jobs'),
                    ('Companies', '/companies'),
                    ('Candidates', '/candidates')
                ]
                
                for text, target in nav_links:
                    ui.link(text, target).classes('text-gray-700 hover:text-emerald-600 font-medium transition-colors hover:bg-gray-100 px-3 py-2 rounded-lg')
                
                #  # About Link
                # with ui.button_group().classes('relative group').on('click', lambda: ui.navigate.to('/about')):
                #     with ui.row().classes('px-4 py-2 items-center text-gray-600 hover:text-emerald-600 transition-colors'):
                #         ui.icon('info', size='1.1rem').classes('mr-2')
                #         ui.label('About').classes('font-medium')
                
                # # Contact Link
                # with ui.button_group().classes('relative group').on('click', lambda: ui.navigate.to('/contact')):
                #     with ui.row().classes('px-4 py-2 items-center text-gray-600 hover:text-emerald-600 transition-colors'):
                #         ui.icon('email', size='1.1rem').classes('mr-2')
                #         ui.label('Contact').classes('font-medium')
            
            # Right side - Auth/User controls
            with ui.row().classes('flex-1 justify-end items-center'):
                # Desktop Auth Buttons
                with ui.row().classes('md:flex items-center space-x-4'):
                    ui.link('Log In', '/login').classes('text-gray-600 hover:text-emerald-600 px-4 py-2')
                    ui.link('Sign Up', '/signup').classes('bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-4 py-2 rounded hover:shadow-md transition-all')
                
                # Mobile menu button
                with ui.button(icon='menu', on_click=show_mobile_menu).props('flat').classes('md:hidden'):
                    ui.tooltip('Menu')
                    
                # Search button (mobile only)
                with ui.button(icon='search', on_click=None).props('flat').classes('md:hidden'):
                    ui.tooltip('Search jobs')
                
                # Post a job button
                with ui.link().on('click', lambda: ui.navigate.to('/post-job')).classes(''):
                    ui.button('Post a Job', icon='add') \
                        .props('unelevated') \
                        .classes('bg-gradient-to-r from-emerald-600 to-teal-500 text-white hover:shadow-md transition-all')
                
                # Auth buttons or user menu
                if not is_logged_in:
                    with ui.row().classes('hidden md:flex items-center space-x-3 ml-4'):
                        ui.button('Log In', on_click=lambda: ui.navigate.to('/login')) \
                            .props('flat') \
                            .classes('text-emerald-600 hover:bg-emerald-50')
                        ui.button('Sign Up', on_click=lambda: ui.navigate.to('/signup')) \
                            .classes('bg-gradient-to-r from-emerald-600 to-teal-500 text-white hover:shadow-md')
                else:
                    # User menu
                    with ui.menu() as user_menu:
                        with ui.menu_items():
                            with ui.menu_item('My Profile', on_click=lambda: ui.navigate.to('/candidate-profile/1')):
                                ui.icon('person')
                            with ui.menu_item('Settings', on_click=lambda: ui.navigate.to('/settings')):
                                ui.icon('settings')
                            with ui.menu_item('Logout', on_click=handle_logout):
                                ui.icon('logout')
                    
                    with ui.button(on_click=user_menu.open).props('flat').classes('ml-4'):
                        with ui.avatar():
                            ui.icon('account_circle', size='2rem', color='emerald-600')
                        ui.icon('expand_more').classes('ml-1 text-gray-500')

def show_search_modal():
    """Show a modern search modal with filters."""
    with ui.dialog() as search_dialog, ui.card().classes('w-full max-w-2xl'):
        with ui.column().classes('w-full space-y-4 p-6'):
            ui.label('🔍 Search Jobs').classes('text-2xl font-bold text-gray-800')
            
            # Search inputs
            with ui.row().classes('w-full space-x-4'):
                search_input = ui.input('Job title, keywords, or company').classes('flex-1')
                location_input = ui.input('Location').classes('w-48')
            
            # Quick filters
            with ui.row().classes('w-full flex-wrap gap-2'):
                ui.label('Quick filters:').classes('text-sm font-medium text-gray-600')
                for filter_tag in ['Remote', 'Full-time', 'Part-time', 'Contract', 'Entry Level', 'Senior']:
                    ui.chip(filter_tag, removable=True).classes('bg-gray-100 hover:bg-blue-600 hover:text-white transition-colors cursor-pointer')
            
            # Action buttons
            with ui.row().classes('w-full justify-end space-x-2 pt-4'):
                ui.button('Cancel', on_click=search_dialog.close).props('flat')
                ui.button('Search', on_click=lambda: perform_search(search_input.value, location_input.value)).classes('bg-blue-600 text-white')
    
    search_dialog.open()

def perform_search(query, location):
    """Perform search and redirect to results."""
    ui.notify(f'Searching for "{query}" in "{location}"...', type='info')
    ui.navigate.to(f'/jobs?q={query}&location={location}')