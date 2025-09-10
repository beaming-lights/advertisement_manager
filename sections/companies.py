from nicegui import ui

def show_companies_section():
    companies = [
        {'name': 'TechCorp Inc.', 'logo': 'https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=100&q=80', 'jobs': 25},
        {'name': 'MarketPro Agency', 'logo': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?auto=format&fit=crop&w=100&q=80', 'jobs': 15},
        {'name': 'Creative Studios', 'logo': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?auto=format&fit=crop&w=100&q=80', 'jobs': 12},
        {'name': 'FinancePlus', 'logo': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=100&q=80', 'jobs': 18},
    ]
    
    with ui.row().classes('w-full py-20 px-4 bg-white'):
        with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
            ui.label('Top Companies').classes('text-4xl font-bold text-gray-900 mb-16')
            
            with ui.row().classes('w-full justify-center gap-8 flex-wrap'):
                for company in companies:
                    with ui.card().classes('w-64 p-6 bg-white rounded-2xl shadow hover:shadow-lg transition'):
                        ui.image(company['logo']).classes('w-16 h-16 rounded-xl mx-auto mb-4')
                        ui.label(company['name']).classes('text-lg font-semibold text-gray-900 mb-2')
                        ui.label(f"{company['jobs']} Open Positions").classes('text-gray-600')
                        ui.button('View Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('mt-4 btn btn-primary')
