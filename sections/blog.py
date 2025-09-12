from nicegui import ui

def show_blog_section():
    blogs = [
        {
            'title': 'Top 10 Tips for Acing Your Next Interview',
            'image': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80',
            'date': '2025-09-01',
            'excerpt': 'Learn the essential strategies to impress recruiters and secure your dream job.'
        },
        {
            'title': 'Remote Work Trends in 2025',
            'image': 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&w=800&q=80',
            'date': '2025-08-15',
            'excerpt': 'Discover how remote work is reshaping industries and creating new opportunities.'
        },
        {
            'title': 'Building a Career in Tech',
            'image': 'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?auto=format&fit=crop&w=800&q=80',
            'date': '2025-07-20',
            'excerpt': 'Step-by-step guide to launching and growing a successful career in technology.'
        },
    ]
    
    with ui.row().classes('w-full py-20 px-4 bg-gray-50'):
        with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
            ui.label('Latest Articles').classes('text-4xl font-bold text-gray-900 mb-16 w-full text-center')
            
            with ui.row().classes('w-full justify-center gap-8 flex-wrap'):
                for blog in blogs:
                    with ui.card().classes('w-80 bg-white rounded-2xl shadow hover:shadow-lg transition overflow-hidden'):
                        ui.image(blog['image']).classes('w-full h-48 object-cover')
                        with ui.column().classes('p-6 text-left'):
                            ui.label(blog['title']).classes('text-xl font-bold text-gray-900 mb-2')
                            ui.label(blog['excerpt']).classes('text-gray-600 mb-4')
                            ui.button('Read More', on_click=lambda: ui.notify('Blog feature coming soon!', type='info')).classes('btn btn-primary')
