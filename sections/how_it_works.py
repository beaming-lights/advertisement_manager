from nicegui import ui

def show_how_it_works_section():
    with ui.row().classes('w-full py-20 px-4 bg-gray-50'):
        with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
            ui.label('Easy steps to land your next job').classes(
                'text-4xl lg:text-5xl font-bold text-gray-900 mb-16'
            )

            steps = [
                ('person_add', 'blue-600', 'Register Your Account',
                 'Capitalize on low hanging fruit to identify a ballpark value added activity to beta test.'),
                ('search', 'green-600', 'Apply for New Jobs',
                 'Leverage agile frameworks to provide a robust synopsis for high level overviews.'),
                ('celebration', 'purple-600', 'Get Hired Immediately',
                 'Override the digital divide with additional clickthroughs from DevOps.')
            ]

            with ui.row().classes('w-full justify-center gap-8 lg:gap-12'):
                for icon, color, title, desc in steps:
                    with ui.column().classes('text-center max-w-sm'):
                        with ui.card().classes(
                            f'w-20 h-20 mx-auto mb-6 bg-{color.split("-")[0]}-100 '
                            'border-0 flex items-center justify-center rounded-2xl'
                        ):
                            ui.icon(icon, size='xl', color=color)
                        ui.label(title).classes('text-2xl font-bold text-gray-900 mb-4')
                        ui.label(desc).classes('text-gray-600 leading-relaxed')
