from nicegui import ui
from pages.add_event import global_job_listings
from utils import create_jobcamp_job_card

def show_featured_jobs_section():
    with ui.column().classes('w-full py-12 md:py-20 px-4 sm:px-6 lg:px-8 bg-white'):
        with ui.column().classes('w-full max-w-7xl mx-auto'):
            # Section Header
            with ui.column().classes('w-full text-center mb-10 md:mb-16'):
                ui.label('Featured Jobs').classes(
                    'text-3xl sm:text-4xl lg:text-5xl font-bold text-gray-900 mb-4'
                )
                ui.separator().classes('w-24 h-1 bg-gradient-to-r from-emerald-500 to-teal-600 mx-auto rounded-full')
                ui.label('Browse through our latest job opportunities').classes('text-gray-600 mt-4 text-lg')

            # Jobs Grid
            if not global_job_listings:
                with ui.card().classes('w-full max-w-2xl mx-auto p-8 sm:p-12 text-center border border-gray-200 rounded-xl shadow-sm'):
                    ui.icon('work_off', size='xl', color='gray-400').classes('mx-auto mb-4')
                    ui.label('No jobs posted yet').classes('text-xl font-medium text-gray-700 mb-2')
                    ui.label('Be the first to post a job and find great talent!').classes('text-gray-500 mb-6')
                    ui.button('Post Your First Job', 
                            on_click=lambda: ui.navigate.to('/post-job'), 
                            color='primary').classes('px-6 sm:px-8 py-3 text-sm sm:text-base')
            else:
                with ui.grid(columns=1).classes('w-full gap-4 sm:gap-6'):
                    for job in global_job_listings[:6]:
                        create_jobcamp_job_card(job)

            # View All Button
            with ui.row().classes('w-full justify-center mt-10 sm:mt-12'):
                ui.button('View All Jobs', 
                         on_click=lambda: ui.navigate.to('/jobs'),
                         color='primary',
                         icon='arrow_forward').classes('px-8 py-3 text-sm sm:text-base hover:shadow-lg transition-shadow')
