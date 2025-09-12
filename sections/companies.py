from nicegui import ui

def show_companies_section():
    companies = [
        {
            'name': 'TechCorp Inc.', 
            'logo': 'https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=100&q=80', 
            'jobs': 25,
            'category': 'Technology'
        },
        {
            'name': 'MarketPro', 
            'logo': 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?auto=format&fit=crop&w=100&q=80', 
            'jobs': 18,
            'category': 'Marketing'
        },
        {
            'name': 'CreativeMinds', 
            'logo': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?auto=format&fit=crop&w=100&q=80', 
            'jobs': 12,
            'category': 'Design'
        },
        {
            'name': 'FinancePlus', 
            'logo': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=100&q=80', 
            'jobs': 15,
            'category': 'Finance'
        }
    ]
    
    with ui.column().classes('w-full bg-gray-50 py-16 px-4'):
        with ui.column().classes('w-full max-w-7xl mx-auto'):
            # Section Header
            with ui.column().classes('text-center mb-12'):
                ui.label('Top Companies').classes('text-3xl md:text-4xl font-bold text-gray-900 mb-4')
                ui.label('Explore opportunities from leading companies').classes('text-gray-600 text-lg')
            
            # Companies Grid
            with ui.grid(columns=1).classes('w-full gap-6 sm:grid-cols-2 lg:grid-cols-4'):
                for company in companies:
                    with ui.card().classes('w-full h-full flex flex-col p-6 bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 border border-gray-100'):
                        # Company Logo
                        with ui.row().classes('justify-center mb-4'):
                            ui.image(company['logo']).classes('w-20 h-20 rounded-lg object-cover border border-gray-200 p-1')
                        
                        # Company Info
                        with ui.column().classes('text-center flex-grow'):
                            ui.label(company['name']).classes('text-lg font-semibold text-gray-900 mb-1')
                            ui.label(company['category']).classes('text-blue-600 text-sm font-medium mb-3')
                            
                            # Jobs Badge
                            with ui.row().classes('justify-center items-center bg-blue-50 text-blue-700 text-sm font-medium px-3 py-1 rounded-full mx-auto'):
                                ui.icon('work_outline').classes('text-blue-500 mr-1')
                                ui.label(f"{company['jobs']} Open Positions").classes('text-sm')
                        
                        # View Button
                        ui.button('View Openings', on_click=lambda: ui.navigate.to('/jobs')) \
                            .classes('mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white transition-colors')
