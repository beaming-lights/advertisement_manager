from nicegui import ui

def create_jobcamp_job_card(job):
    """Create a job card component in the JobCamp style.
    
    Args:
        job (dict): Dictionary containing job details
            - title: Job title
            - company: Company name
            - location: Job location
            - type: Job type (Full-time, Part-time, etc.)
            - salary: Salary range
            - posted: When the job was posted
            - description: Job description
            - company_logo: URL to company logo (optional)
    
    Returns:
        ui.card: A NiceGUI card component for the job listing
    """
    with ui.card().classes('w-full max-w-md hover:shadow-lg transition-shadow duration-300 border border-gray-100'):
        with ui.row().classes('w-full items-start'):
            # Company logo
            if job.get('company_logo'):
                ui.image(job['company_logo']).classes('w-16 h-16 object-contain mr-4')
            
            # Job details
            with ui.column().classes('flex-1'):
                # Job title and company
                ui.label(job.get('title', 'Job Title')).classes('text-lg font-bold text-gray-900')
                ui.label(job.get('company', 'Company Name')).classes('text-gray-600')
                
                # Location and job type
                with ui.row().classes('mt-2 space-x-4'):
                    if job.get('location'):
                        with ui.row().classes('items-center text-gray-500'):
                            ui.icon('location_on', size='sm')
                            ui.label(job['location']).classes('text-sm')
                    
                    if job.get('type'):
                        with ui.row().classes('items-center text-gray-500'):
                            ui.icon('work', size='sm')
                            ui.label(job['type']).classes('text-sm')
                
                # Salary and posted date
                with ui.row().classes('mt-2 justify-between items-center'):
                    if job.get('salary'):
                        ui.label(f"${job['salary']}").classes('font-medium text-emerald-600')
                    
                    if job.get('posted'):
                        ui.label(f"Posted {job['posted']}").classes('text-sm text-gray-500')
                
                # Job description (truncated)
                if job.get('description'):
                    with ui.expansion('View Details', icon='info').classes('w-full mt-3'):
                        ui.markdown(job['description']).classes('text-sm text-gray-600')
                
                # Apply button
                ui.button('Apply Now', on_click=lambda: ui.navigate.to(f"/jobs/{job.get('id', '')}")) \
                    .classes('mt-4 bg-emerald-600 hover:bg-emerald-700 text-white')
    
    # Add some spacing between cards
    ui.space().classes('h-6')
    return None  # The card is added to the UI tree automatically
