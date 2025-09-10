from nicegui import ui
from components.header import show_header
from components.footer import show_footer

def show_candidate_profile_page(candidate_id: str = None):
    """Simplified candidate profile page for testing."""
    show_header()
    
    with ui.column().classes('w-full max-w-4xl mx-auto p-8'):
        ui.label('Candidate Profile').classes('text-3xl font-bold mb-6')
        
        with ui.card().classes('p-6'):
            ui.label('David Henricks').classes('text-2xl font-semibold mb-2')
            ui.label('Senior Product Designer').classes('text-lg text-gray-600 mb-4')
            ui.label('New York, USA').classes('text-gray-500 mb-4')
            
            ui.label('About').classes('text-xl font-semibold mb-2')
            ui.label('A talented professional with experience in product design.').classes('text-gray-700 mb-4')
            
            ui.label('Skills').classes('text-xl font-semibold mb-2')
            with ui.row().classes('gap-2 mb-4'):
                skills = ['UI/UX Design', 'Figma', 'Prototyping']
                for skill in skills:
                    ui.label(skill).classes('bg-blue-100 text-blue-800 px-3 py-1 rounded')
    
    show_footer()

def show_candidate_list_page():
    """Simplified candidate list page for testing."""
    show_header()
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-8'):
        ui.label('Candidates').classes('text-3xl font-bold mb-6')
        
        with ui.row().classes('gap-6'):
            for i in range(3):
                with ui.card().classes('p-4 w-64'):
                    ui.label(f'Candidate {i+1}').classes('text-lg font-semibold mb-2')
                    ui.label('Product Designer').classes('text-gray-600 mb-2')
                    ui.button('View Profile', on_click=lambda: ui.navigate.to('/candidate-profile/1')).classes('w-full')
    
    show_footer()
