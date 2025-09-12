from nicegui import ui

def show_how_it_works_section():
    with ui.column().classes('w-full py-16 sm:py-20 lg:py-24 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-white to-gray-50'):
        with ui.column().classes('w-full max-w-7xl mx-auto'):
            # Section Header
            with ui.column().classes('w-full max-w-4xl mx-auto text-center mb-12 sm:mb-16'):
                ui.label('HOW IT WORKS').classes('text-xs sm:text-sm font-semibold text-emerald-600 tracking-wider mb-3')
                ui.label('Get Hired in 3 Simple Steps').classes(
                    'text-3xl sm:text-4xl lg:text-5xl font-bold text-gray-900 mb-4 leading-tight'
                )
                ui.label('Join thousands of professionals who found their dream jobs through our platform')\
                    .classes('text-gray-500 text-base sm:text-lg max-w-3xl mx-auto')

            # Steps Grid
            steps = [
                ('person_add_alt_1', 'from-blue-500 to-cyan-400', 'Create Your Profile',
                 'Set up your professional profile in minutes. Showcase your skills, experience, and career goals to stand out to employers.'),
                ('work_outline', 'from-emerald-500 to-teal-400', 'Find Your Dream Job',
                 'Browse thousands of job listings and apply with a single click. Our smart matching system connects you with the best opportunities.'),
                ('celebration', 'from-purple-500 to-indigo-400', 'Start Your New Role',
                 'Get hired faster with direct connections to top companies. Many candidates receive offers within days of applying.')
            ]

            with ui.grid(columns=1, rows=3).classes('w-full gap-6 sm:gap-8 lg:grid-cols-3 lg:grid-rows-1'):
                for icon, gradient, title, desc in steps:
                    with ui.column().classes('group relative bg-white p-6 sm:p-8 rounded-xl sm:rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1 overflow-hidden'):
                        # Light overlay on hover
                        with ui.element('div').classes('absolute inset-0 bg-gradient-to-br from-emerald-50/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0'):
                            pass
                            
                        # Card content container
                        with ui.column().classes('relative z-10 h-full flex flex-col'):
                            # Step number with gradient background
                            step_num = steps.index((icon, gradient, title, desc)) + 1
                            with ui.element('div').classes(f'absolute -top-3 -left-3 w-8 h-8 sm:w-10 sm:h-10 rounded-full bg-gradient-to-br {gradient} flex items-center justify-center shadow-md'):
                                ui.label(str(step_num)).classes('font-bold text-white text-sm sm:text-base')
                            
                            # Icon container
                            with ui.element('div').classes(f'w-16 h-16 sm:w-20 sm:h-20 mx-auto mb-4 sm:mb-6 rounded-xl sm:rounded-2xl bg-gradient-to-br {gradient} flex items-center justify-center text-white transform transition-all duration-300 group-hover:scale-105 shadow-lg'):
                                ui.icon(icon, size='1.75rem').classes('drop-shadow-md')
                            
                            # Content
                            with ui.column().classes('flex-1'):
                                ui.label(title).classes('text-xl sm:text-2xl font-bold text-gray-900 mb-3 sm:mb-4')
                                ui.label(desc).classes('text-sm sm:text-base text-gray-600 leading-relaxed mb-4 sm:mb-6')
                            
                            # Learn more link
                            with ui.link().classes('mt-auto text-emerald-600 hover:text-emerald-700 font-medium inline-flex items-center text-sm sm:text-base group-hover:translate-x-1 transition-transform'):
                                ui.label('Learn more')
                                ui.icon('arrow_forward', size='sm').classes('ml-1')
