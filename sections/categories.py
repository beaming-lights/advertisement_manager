from nicegui import ui

def show_categories_section():
    categories = [
        {'name': 'Technology', 'jobs': 120, 'icon': 'computer'},
        {'name': 'Design', 'jobs': 80, 'icon': 'palette'},
        {'name': 'Marketing', 'jobs': 95, 'icon': 'campaign'},
        {'name': 'Finance', 'jobs': 60, 'icon': 'savings'},
        {'name': 'Healthcare', 'jobs': 45, 'icon': 'health_and_safety'},
        {'name': 'Education', 'jobs': 70, 'icon': 'school'},
    ]
    
    with ui.row().classes('w-full py-20 px-4 bg-gray-50'):
        with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
            ui.label('Browse by Categories').classes('text-4xl font-bold text-gray-900 mb-16')
            
            with ui.row().classes('w-full justify-center gap-6 flex-wrap'):
                for cat in categories:
                    with ui.card().classes('w-64 bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition cursor-pointer group'):
                        ui.icon(cat['icon'], size='xl', color='blue-600').classes('mb-4 group-hover:scale-110 transition')
                        ui.label(cat['name']).classes('text-xl font-semibold text-gray-900 mb-2')
                        ui.label(f"{cat['jobs']} Jobs Available").classes('text-gray-600')
