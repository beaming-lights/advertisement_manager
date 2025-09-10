from nicegui import ui
from pages.add_event import global_job_listings
from utils import create_jobcamp_job_card

def show_featured_jobs_section():
    with ui.row().classes('w-full py-20 px-4 bg-white'):
        with ui.column().classes('w-full max-w-7xl mx-auto'):
            ui.label('Featured Jobs').classes(
                'text-4xl lg:text-5xl font-bold text-gray-900 text-center mb-16'
            )

            if not global_job_listings:
                with ui.card().classes('w-full p-12 text-center border border-gray-200'):
                    ui.icon('work_off', size='xl', color='gray-400').classes('mx-auto mb-4')
                    ui.label('No jobs posted yet').classes('text-xl font-medium text-gray-600 mb-2')
                    ui.label('Be the first to post a job and find great talent!').classes('text-gray-500 mb-4')
                    ui.button('Post Your First Job', on_click=lambda: ui.navigate.to('/post-job'), color='primary').classes('px-8 py-3')
            else:
                with ui.row().classes('w-full gap-6 flex-wrap'):
                    for job in global_job_listings[:6]:
                        create_jobcamp_job_card(job)

            with ui.row().classes('w-full justify-center mt-12'):
                ui.button('View All Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes(
                    'btn btn-primary'
                )
