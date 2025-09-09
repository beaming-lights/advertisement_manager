from nicegui import ui

def show_header():
    """Creates a JobCamp-style header with clean navigation."""
    with ui.header().classes('bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm') as header:
        with ui.row().classes('w-full max-w-7xl mx-auto px-4 py-4 justify-between items-center'):
            # Logo and Brand - JobCamp style
            with ui.row().classes('items-center space-x-3'):
                ui.link('Jobcamp', '/').classes('text-2xl font-bold text-gray-900 hover:text-blue-600 transition-colors')
            
            # Desktop Navigation - JobCamp style
            with ui.row().classes('hidden lg:flex items-center space-x-8') as desktop_nav:
                # Home dropdown placeholder
                with ui.row().classes('items-center space-x-1 cursor-pointer hover:text-blue-600 transition-colors'):
                    ui.link('Home', '/').classes('text-gray-700 hover:text-blue-600 font-medium')
                    ui.icon('keyboard_arrow_down', size='sm').classes('text-gray-500')
                
                # Pages dropdown placeholder  
                with ui.row().classes('items-center space-x-1 cursor-pointer hover:text-blue-600 transition-colors'):
                    ui.label('Pages').classes('text-gray-700 hover:text-blue-600 font-medium cursor-pointer')
                    ui.icon('keyboard_arrow_down', size='sm').classes('text-gray-500')
                
                ui.link('Jobs', '/jobs').classes('text-gray-700 hover:text-blue-600 font-medium transition-colors')
                ui.link('Companies', '/companies').classes('text-gray-700 hover:text-blue-600 font-medium transition-colors')
                ui.link('Contact', '/contact').classes('text-gray-700 hover:text-blue-600 font-medium transition-colors')
            
            # Action Buttons - JobCamp style
            with ui.row().classes('items-center space-x-4'):
                # Sign In Button
                ui.button('Sign In', on_click=lambda: ui.notify('Sign in feature coming soon!', type='info')).classes('text-gray-700 hover:text-blue-600 font-medium bg-transparent border-0 px-4 py-2')
                
                # Post Job CTA - JobCamp style
                ui.button('Post a Job', on_click=lambda: ui.open('/post-job')).classes('bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-xl transition-colors')
                
                # Mobile Menu Toggle
                mobile_menu = ui.button(icon='menu', on_click=lambda: mobile_nav.classes(toggle='hidden')).props('flat round').classes('lg:hidden text-gray-600 hover:text-blue-600')
        
        # Mobile Navigation - JobCamp style
        with ui.column().classes('lg:hidden hidden w-full bg-white border-t border-gray-200 px-4 py-4 space-y-3') as mobile_nav:
            ui.link('Home', '/').classes('text-gray-700 hover:text-blue-600 font-medium py-2 block')
            ui.link('Jobs', '/jobs').classes('text-gray-700 hover:text-blue-600 font-medium py-2 block')
            ui.link('Companies', '/companies').classes('text-gray-700 hover:text-blue-600 font-medium py-2 block')
            ui.link('Contact', '/contact').classes('text-gray-700 hover:text-blue-600 font-medium py-2 block')
            ui.separator()
            ui.button('Sign In', on_click=lambda: ui.notify('Sign in feature coming soon!', type='info')).classes('w-full text-blue-600 border border-blue-600 hover:bg-blue-600 hover:text-white transition-all py-2 rounded-xl')
            ui.button('Post a Job', on_click=lambda: ui.open('/post-job')).classes('w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-colors mt-2')
        
        # Close mobile menu when clicking outside
        mobile_menu.on('click', lambda: mobile_nav.classes(toggle='hidden'))

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
                    ui.chip(filter_tag, removable=True).classes('bg-gray-100 hover:bg-primary hover:text-white transition-colors cursor-pointer')
            
            # Action buttons
            with ui.row().classes('w-full justify-end space-x-2 pt-4'):
                ui.button('Cancel', on_click=search_dialog.close).props('flat')
                ui.button('Search', on_click=lambda: perform_search(search_input.value, location_input.value)).classes('bg-primary text-white')
    
    search_dialog.open()

def perform_search(query, location):
    """Perform search and redirect to results."""
    ui.notify(f'Searching for "{query}" in "{location}"...', type='info')
    ui.open(f'/jobs?q={query}&location={location}')