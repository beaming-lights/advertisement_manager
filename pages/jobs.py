from nicegui import ui
from components.header import show_header
from components.footer import show_footer
from pages.add_event import global_job_listings

def show_jobs_page():
    """Creates the page for displaying all job listings."""
    show_header()

    with ui.column().classes('w-full max-w-7xl mx-auto p-4 md:p-8'):
        ui.label('All Jobs').classes('text-4xl lg:text-5xl font-bold text-gray-900 text-center mb-16')

        if not global_job_listings:
            with ui.card().classes('w-full p-12 text-center border border-gray-200'):
                ui.icon('work_off', size='xl', color='gray-400').classes('mx-auto mb-4')
                ui.label('No jobs posted yet').classes('text-xl font-medium text-gray-600 mb-2')
                ui.label('Be the first to post a job and find the best talent!').classes('text-gray-500')
                ui.button('Post a Job', on_click=lambda: ui.navigate.to('/post-job')).classes('btn btn-primary mt-6')
        else:
            with ui.column().classes('w-full gap-6'):
                for job in global_job_listings:
                    with ui.card().classes('w-full p-6 hover:shadow-lg transition-shadow duration-300'):
                        with ui.row().classes('w-full items-start'):
                            with ui.column().classes('flex-1'):
                                ui.label(job.get('title', 'Job Title')).classes('text-xl font-bold text-gray-900')
                                ui.label(job.get('company', 'Company Name')).classes('text-gray-600')
                                
                                with ui.row().classes('mt-2 space-x-4'):
                                    if job.get('location'):
                                        with ui.row().classes('items-center text-gray-500'):
                                            ui.icon('location_on', size='sm')
                                            ui.label(job['location']).classes('text-sm')
                                    
                                    if job.get('type'):
                                        with ui.row().classes('items-center text-gray-500'):
                                            ui.icon('work', size='sm')
                                            ui.label(job['type']).classes('text-sm')
                                
                                if job.get('description'):
                                    with ui.expansion('View Details', icon='info').classes('w-full mt-3'):
                                        ui.markdown(job['description']).classes('text-sm text-gray-600')
                            
                            ui.button('Apply', on_click=lambda j=job: ui.navigate.to(f"/jobs/{j.get('id', '')}")) \
                                .classes('mt-4 bg-emerald-600 hover:bg-emerald-700 text-white')
            with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
                for job in global_job_listings:
                    create_jobcamp_job_card(job)

    show_footer()
