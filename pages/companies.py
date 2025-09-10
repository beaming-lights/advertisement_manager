from nicegui import ui
from components.header import show_header
from components.footer import show_footer

def show_companies_page():
    """Creates the page for displaying all companies."""
    show_header()

    companies = [
        {'name': 'TechCorp Inc.', 'logo': 'https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=100&q=80', 'jobs': 25},
        {'name': 'MarketPro Agency', 'logo': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?auto=format&fit=crop&w=100&q=80', 'jobs': 15},
        {'name': 'Creative Studios', 'logo': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?auto=format&fit=crop&w=100&q=80', 'jobs': 12},
        {'name': 'FinancePlus', 'logo': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=100&q=80', 'jobs': 18},
        {'name': 'InnovateTech', 'logo': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=100&q=80', 'jobs': 30},
        {'name': 'WebCraft Solutions', 'logo': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=100&q=80', 'jobs': 22},
    ]

    with ui.column().classes('w-full max-w-7xl mx-auto p-4 md:p-8'):
        ui.label('All Companies').classes('text-4xl lg:text-5xl font-bold text-gray-900 text-center mb-16')

        with ui.row().classes('w-full gap-8 flex-wrap justify-center'):
            for company in companies:
                with ui.card().classes('w-64 p-6 bg-white rounded-2xl shadow hover:shadow-lg transition text-center'):
                    ui.image(company['logo']).classes('w-16 h-16 rounded-xl mx-auto mb-4')
                    ui.label(company['name']).classes('text-lg font-semibold text-gray-900 mb-2')
                    ui.label(f"{company['jobs']} Open Positions").classes('text-gray-600')
                    ui.button('View Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('mt-4 btn btn-primary')

    show_footer()
