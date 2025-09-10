from nicegui import ui

def show_footer():
    """Creates a footer with navigation links and copyright."""
    try:
        footer_container = ui.element('footer').classes('w-full bg-gray-900 text-white py-6')
        
        with footer_container:
            with ui.column().classes('w-full max-w-7xl mx-auto px-4'):
                # Navigation Links
                with ui.row().classes('w-full justify-center mb-4'):
                    nav_links = [
                        ('Home', '/'),
                        ('Jobs', '/jobs'),
                        ('Companies', '/companies'),
                        ('Post a Job', '/post-job'),
                        ('Contact', '/contact')
                    ]
                    
                    for i, (text, url) in enumerate(nav_links):
                        ui.link(text, url).classes('text-gray-300 hover:text-white px-3 py-2 text-sm font-medium transition-colors')
                        if i < len(nav_links) - 1:
                            ui.element('span').classes('text-gray-600')
                
                # Copyright and Logo
                with ui.row().classes('w-full items-center justify-center space-x-2 pt-4 border-t border-gray-800'):
                    # Logo
                    with ui.row().classes('flex items-center'):
                        ui.icon('work', size='sm', color='white')
                        ui.label('JobBoard').classes('font-bold')
                    # Copyright
                    ui.label('•').classes('text-gray-600')
                    ui.label('© 2023 All rights reserved').classes('text-gray-400 text-sm')
        
        return footer_container
        
    except Exception as e:
        print(f"Error in show_footer: {str(e)}")
        return ui.element('div')

