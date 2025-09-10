from nicegui import ui

def show_how_it_works_section():
    with ui.row().classes('w-full py-24 px-4 bg-gradient-to-b from-white to-gray-50'):
        with ui.column().classes('w-full max-w-7xl mx-auto text-center'):
            with ui.column().classes('max-w-3xl mx-auto mb-16'):
                ui.label('HOW IT WORKS').classes('text-sm font-semibold text-emerald-600 tracking-wider mb-4')
                ui.label('Get Hired in 3 Simple Steps').classes(
                    'text-4xl lg:text-5xl font-bold text-gray-900 mb-4'
                )
                ui.label('Join thousands of professionals who found their dream jobs through our platform').classes('text-gray-500 text-lg')

            steps = [
                ('person_add_alt_1', 'from-blue-500 to-cyan-400', 'Create Your Profile',
                 'Set up your professional profile in minutes. Showcase your skills, experience, and career goals to stand out to employers.'),
                ('work_outline', 'from-emerald-500 to-teal-400', 'Find Your Dream Job',
                 'Browse thousands of job listings and apply with a single click. Our smart matching system connects you with the best opportunities.'),
                ('celebration', 'from-purple-500 to-indigo-400', 'Start Your New Role',
                 'Get hired faster with direct connections to top companies. Many candidates receive offers within days of applying.')
            ]

            with ui.grid(columns=1).classes('w-full gap-8 lg:grid-cols-3 px-4'):
                for icon, gradient, title, desc in steps:
                    with ui.column().classes('group relative bg-white p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 overflow-hidden'):
                        # Light overlay on hover
                        with ui.element('div').classes('absolute inset-0 bg-gradient-to-br from-emerald-50/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0'):
                            pass
                            
                        # Card content container
                        with ui.column().classes('relative z-10'):
                            # Step number with gradient background
                            step_num = steps.index((icon, gradient, title, desc)) + 1
                            with ui.element('div').classes(f'absolute -top-4 -left-4 w-10 h-10 rounded-full bg-gradient-to-br {gradient} flex items-center justify-center shadow-lg'):
                                ui.label(str(step_num)).classes('font-bold text-white text-lg')
                            
                            # Icon container with subtle shadow and hover effect
                            with ui.element('div').classes(f'w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br {gradient} flex items-center justify-center text-white transform transition-all duration-300 group-hover:scale-110 shadow-lg'):
                                ui.icon(icon, size='2rem').classes('drop-shadow-md')
                            
                            # Content
                            ui.label(title).classes('text-2xl font-bold text-gray-900 mb-4 mt-2')
                            ui.label(desc).classes('text-gray-600 leading-relaxed mb-6')
                            
                            # Learn more link
                            with ui.link().classes('text-emerald-600 hover:text-emerald-700 font-medium inline-flex items-center group-hover:translate-x-1 transition-transform'):
                                ui.label('Learn more')
                                ui.icon('arrow_forward', size='sm').classes('ml-1')
