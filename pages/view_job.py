from nicegui import ui
from components.header import show_header
from utils.api_client import api_client

import asyncio
from typing import Dict, Any, List, Optional

def show_view_job_page(job_id: str):
    """Show detailed view of a single job."""
    show_header()
    
    if not job_id:
        with ui.column().classes('max-w-2xl mx-auto p-6'):
            ui.label('Job ID is required').classes('text-xl font-bold text-red-600 mb-4')
            ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('bg-gray-500 text-white')
        return
    
    # Create a container for the content
    container = ui.column().classes('w-full max-w-6xl mx-auto p-4')
    
    # Show loading state
    with container:
        ui.spinner(size='lg')
        ui.label('Loading job details...').classes('text-lg font-medium mt-2')
    
    async def load_job():
        try:
            # Get job data
            job = await asyncio.to_thread(api_client.get_job_by_id, job_id)
            if not job:
                raise Exception('Job not found')
            
            # Clear the loading state and show job details
            container.clear()
            with container:
                create_job_view(job, job_id)
            
        except Exception as e:
            container.clear()
            with container:
                ui.notify(f'Error loading job: {str(e)}', type='negative')
                with ui.column().classes('max-w-2xl mx-auto p-6'):
                    ui.label('Error loading job details').classes('text-xl font-bold text-red-600 mb-4')
                    ui.label(str(e)).classes('text-gray-700 mb-4')
                    ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('bg-gray-500 text-white')
    
    # Start loading the job data
    asyncio.create_task(load_job())

async def delete_job(job_id: str):
    """Handle job deletion."""
    try:
        # Show loading state
        with ui.dialog() as processing_dialog, ui.card():
            with ui.column().classes('items-center'):
                ui.spinner(size='lg')
                ui.label('Deleting job...')
        processing_dialog.open()
        
        try:
            # Call API to delete the job
            result = await asyncio.to_thread(api_client.delete_job, job_id)
            processing_dialog.close()
            
            if result:
                ui.notify('Job deleted successfully', type='positive')
                # Add a small delay to show the success message
                await asyncio.sleep(0.5)
                ui.navigate.to('/jobs')
            else:
                ui.notify('Failed to delete job. Please try again.', type='negative')
                
        except Exception as e:
            processing_dialog.close()
            ui.notify(f'Error deleting job: {str(e)}', type='negative')
            
    except Exception as e:
        ui.notify(f'Error: {str(e)}', type='negative')

def create_job_view(job: Dict[str, Any], job_id: str):
    """Create the job details view with the given job data."""
    with ui.column().classes('w-full'):
        # Header with back button and title
        with ui.row().classes('w-full items-center mb-6'):
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/jobs')).props('flat')
            ui.label('Job Details').classes('text-2xl font-bold')
        
        # Main job card
        with ui.card().classes('w-full mb-6'):
            # Job title and company
            with ui.row().classes('items-center justify-between w-full mb-4'):
                with ui.column():
                    ui.label(job.get('title', 'No Title')).classes('text-2xl font-bold')
                    ui.label(job.get('posted_by', 'Company not specified')).classes('text-lg text-gray-600')
                
                # Salary information if available
                if job.get('salary_min') or job.get('salary_max'):
                    with ui.column().classes('items-end'):
                        salary_parts = []
                        if job.get('salary_min'):
                            salary_parts.append(f"${job['salary_min']:,}")
                        if job.get('salary_max'):
                            salary_parts.append(f"${job['salary_max']:,}")
                        salary_text = ' - '.join(salary_parts)
                        if job.get('currency'):
                            salary_text += f" {job['currency']}"
                        ui.label(f"{salary_text}").classes('text-lg text-green-600 font-semibold')
            
            # Job images/flyers section
            with ui.card().classes('p-6 mb-6'):
                ui.label('Job Images').classes('text-xl font-bold mb-4')
                
                # Get all images from the job data
                image_sources = []
                
                # Add flyer if exists (handle both direct URL and object with url)
                flyer = job.get('flyer')
                if flyer:
                    if isinstance(flyer, dict):
                        flyer = flyer.get('url', '')
                    if isinstance(flyer, str) and flyer.strip():
                        image_sources.append(('Job Flyer', flyer))
                
                # Add main image if exists
                image_url = job.get('image_url')
                if image_url:
                    if isinstance(image_url, dict):
                        image_url = image_url.get('url', '')
                    if isinstance(image_url, str) and image_url.strip():
                        image_sources.append(('Job Image', image_url))
                
                # Add any additional images from images array
                images = job.get('images', [])
                if isinstance(images, list):
                    for i, img in enumerate(images, 1):
                        img_url = img.get('url') if isinstance(img, dict) else img
                        if isinstance(img_url, str) and img_url.strip():
                            image_sources.append((f'Image {i}', img_url))
                
                # Display all found images
                if image_sources:
                    with ui.row().classes('gap-4 flex-wrap'):
                        for title, url in image_sources:
                            with ui.card().classes('w-64 hover:shadow-lg transition-shadow'):
                                ui.image(job.get('flyer')).classes('w-full h-40 object-cover')
                                with ui.card_section():
                                    ui.label(title).classes('text-sm font-medium')
                else:
                    with ui.card().classes('p-4 text-center bg-gray-50'):
                        ui.icon('image', size='2rem').classes('text-gray-400 mb-2')
                        ui.label('No images available').classes('text-gray-500')
            
            # Job details
            with ui.card().classes('p-6 mb-6'):
                ui.label('Job Details').classes('text-xl font-bold mb-4')
                
                # Job metadata
                with ui.grid(columns=2).classes('w-full gap-4 mb-4'):
                    with ui.column():
                        with ui.row().classes('items-center gap-2'):
                            ui.icon('location_on', size='sm').classes('text-gray-500')
                            ui.label(job.get('location', 'Location not specified')).classes('text-gray-700')
                        
                        with ui.row().classes('items-center gap-2'):
                            ui.icon('work', size='sm').classes('text-gray-500')
                            ui.label(job.get('job_type', 'Job type not specified')).classes('text-gray-700')
                    
                    with ui.column():
                        if job.get('posted_date'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('event', size='sm').classes('text-gray-500')
                                ui.label(f"Posted: {job['posted_date']}").classes('text-gray-700')
                        
                        if job.get('deadline'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('event_available', size='sm').classes('text-gray-500')
                                ui.label(f"Deadline: {job['deadline']}").classes('text-gray-700')
                
                # Job description
                ui.label('Description').classes('text-lg font-semibold mt-4 mb-2')
                description = job.get('description', 'No description provided.')
                if isinstance(description, str):
                    ui.html(f"<div class='prose max-w-none'>{description}</div>")
                
                # Requirements if available
                requirements = job.get('requirements')
                if requirements:
                    ui.label('Requirements').classes('text-lg font-semibold mt-6 mb-2')
                    if isinstance(requirements, str):
                        ui.html(f"<div class='prose max-w-none'>{requirements}</div>")
                
                # Benefits if available
                benefits = job.get('benefits')
                if benefits:
                    ui.label('Benefits').classes('text-lg font-semibold mt-6 mb-2')
                    if isinstance(benefits, str):
                        ui.html(f"<div class='prose max-w-none'>{benefits}</div>")
            
            # Action buttons
            ui.image(job.get('flyer')).classes('w-20 h-40 object-cover')
            with ui.row().classes('w-full justify-between items-center mt-4'):
                # Back button
                ui.button('← Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).props('flat')
                
                # Right-aligned action buttons
                with ui.row().classes('gap-2'):
                    # Apply button with external link if available, otherwise show disabled button
                    apply_url = job.get('apply_url') or job.get('application_url') or job.get('apply_link')
                    if apply_url:
                        ui.button('Apply Now', on_click=lambda: ui.open(apply_url)).props('color=primary')
                    else:
                        ui.button('Apply Now').props('disabled color=primary')
                    
                    # Save/Bookmark button
                    ui.button(icon='bookmark_border').props('flat')
                    
                    # Share button
                    ui.button(icon='share').props('flat')
                    
                    # Delete button with confirmation dialog
                    with ui.dialog() as delete_dialog, ui.card():
                        ui.label('Are you sure you want to delete this job?')
                        with ui.row():
                            ui.button('Cancel', on_click=delete_dialog.close)
                            ui.button('Delete', on_click=lambda: (
                                delete_dialog.close(),
                                asyncio.create_task(delete_job(job_id))
                            )).props('color=red')
                    
                    ui.button(icon='delete', on_click=delete_dialog.open).props('color=red flat')

def display_job_image(image_url, title='Image'):
    """Simple function to display a job image"""
    with ui.card().classes('w-64 hover:shadow-lg transition-shadow'):
        ui.image(image_url).classes('w-full h-40 object-cover')
        with ui.card_section():
            ui.label(title).classes('text-sm font-medium')

def display_api_image(image):
    """Simple display for API images"""
    if isinstance(image, dict) and image.get('url'):
        display_job_image(image['url'], image.get('name', 'Image'))

def apply_to_job(job):
    """Handle job application"""
    ui.notify('Application feature coming soon!', type='info')

def save_job(job):
    """Save job to user's saved jobs"""
    ui.notify('Job saved to your favorites!', type='positive')

def share_job(job):
    """Share job via different methods"""
    with ui.dialog() as dialog, ui.card().classes('p-4'):
        ui.label('Share this job').classes('text-lg font-bold mb-4')
        
        job_url = f"https://yoursite.com/job/{job.get('id', '')}"
        
        with ui.column().classes('gap-3'):
            ui.input('Job URL', value=job_url, readonly=True).classes('w-full')
            
            with ui.row().classes('gap-2'):
                ui.button('Copy Link', on_click=lambda: copy_to_clipboard(job_url)).classes('bg-blue-500 text-white')
                ui.button('Email', on_click=lambda: share_via_email(job)).classes('bg-green-500 text-white')
                ui.button('LinkedIn', on_click=lambda: share_via_linkedin(job)).classes('bg-blue-700 text-white')
            
            ui.button('Close', on_click=dialog.close).classes('bg-gray-500 text-white mt-4')
    
    dialog.open()

def copy_to_clipboard(text):
    """Copy text to clipboard"""
    ui.run_javascript(f'navigator.clipboard.writeText("{text}")')
    ui.notify('Link copied to clipboard!', type='positive')

def share_via_email(job):
    """Share job via email"""
    subject = f"Job Opportunity: {job.get('title', 'Job')}"
    body = f"Check out this job opportunity:\n\n{job.get('title', 'Job')} at {job.get('posted_by', 'Company')}\nLocation: {job.get('location', 'N/A')}\n\nView details: https://yoursite.com/job/{job.get('id', '')}"
    mailto_url = f"mailto:?subject={subject}&body={body}"
    ui.run_javascript(f'window.open("{mailto_url}")')

def share_via_linkedin(job):
    """Share job via LinkedIn"""
    url = f"https://yoursite.com/job/{job.get('id', '')}"
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={url}"
    ui.run_javascript(f'window.open("{linkedin_url}", "_blank")')
