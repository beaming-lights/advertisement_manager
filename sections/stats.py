from nicegui import ui

def show_stats_section():
    with ui.row().classes('w-full py-20 px-4 relative overflow-hidden'):
        with ui.element('div').classes('absolute inset-0 bg-blue-600'):
            pass

        ui.image(
            'https://images.unsplash.com/photo-1551434678-e076c223a692'
            '?ixlib=rb-4.0.3&auto=format&fit=crop&w=1280&q=80'
        ).classes('absolute inset-0 w-full h-full object-cover opacity-30')

        with ui.column().classes('w-full max-w-7xl mx-auto text-center relative z-10'):
            ui.label('Over 50k+ people landed their first job from Jobcamp.').classes(
                'text-3xl lg:text-4xl font-bold text-white mb-4'
            )
            ui.label('Join companies from anywhere in the world.').classes(
                'text-xl text-blue-100 mb-12'
            )

            stats = [
                ('50,000+', 'Jobs Posted'),
                ('25,000+', 'Companies'),
                ('100,000+', 'Happy Candidates'),
            ]
            with ui.row().classes('w-full justify-center gap-16'):
                for number, label in stats:
                    with ui.column().classes('text-center'):
                        ui.label(number).classes('text-4xl font-bold text-white')
                        ui.label(label).classes('text-blue-200')
