import asyncio
from typing import Dict, Any, List, Optional
from nicegui import ui
from components.header import show_header
from utils.api_client import api_client

def show_event_page(job_id: str = None):
    """Show detailed view of a single event."""
    show_header()
    
    if not job_id:
        with ui.column().classes('max-w-2xl mx-auto p-6'):
            ui.label('Event ID is required').classes('text-xl font-bold text-red-600 mb-4')
            ui.button('Back to Events', on_click=lambda: ui.navigate.to('/events')).classes('bg-gray-500 text-white')
        return
    
    # Create a container for the content
    container = ui.column().classes('w-full max-w-6xl mx-auto p-4')
    
    # Show loading state
    with container:
        ui.spinner(size='lg')
        ui.label('Loading event details...').classes('text-lg font-medium mt-2')
    
    async def load_event():
        try:
            # Get event data
            event = await asyncio.to_thread(api_client.get_job_by_id, job_id)
            if not event:
                raise Exception('Event not found')
            
            # Clear the loading state and show event details
            container.clear()
            with container:
                create_event_view(event, job_id)
            
        except Exception as e:
            container.clear()
            with container:
                ui.notify(f'Error loading event: {str(e)}', type='negative')
                with ui.column().classes('max-w-2xl mx-auto p-6'):
                    ui.label('Error loading event details').classes('text-xl font-bold text-red-600 mb-4')
                    ui.label(str(e)).classes('text-gray-700 mb-4')
                    ui.button('Back to Events', on_click=lambda: ui.navigate.to('/events')).classes('bg-gray-500 text-white')
    
    # Start loading the event data
    asyncio.create_task(load_event())

async def delete_event(event_id: str):
    """Handle event deletion."""
    try:
        # Show loading state
        with ui.dialog() as processing_dialog, ui.card():
            with ui.column().classes('items-center'):
                ui.spinner(size='lg')
                ui.label('Deleting event...')
        processing_dialog.open()
        
        try:
            # Call API to delete the event
            result = await asyncio.to_thread(api_client.delete_job, event_id)
            processing_dialog.close()
            
            if result:
                ui.notify('Event deleted successfully', type='positive')
                # Add a small delay to show the success message
                await asyncio.sleep(0.5)
                ui.navigate.to('/events')
            else:
                ui.notify('Failed to delete event. Please try again.', type='negative')
                
        except Exception as e:
            processing_dialog.close()
            ui.notify(f'Error deleting event: {str(e)}', type='negative')
            
    except Exception as e:
        ui.notify(f'Error: {str(e)}', type='negative')

def create_event_view(event: Dict[str, Any], event_id: str):
    """Create the event details view with the given event data."""
    with ui.column().classes('w-full'):
        # Header with back button and title
        with ui.row().classes('w-full items-center mb-6'):
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/events')).props('flat')
            ui.label('Event Details').classes('text-2xl font-bold')
        
        # Main event card
        with ui.card().classes('w-full mb-6'):
            # Event title and organizer
            with ui.row().classes('items-center justify-between w-full mb-4'):
                with ui.column():
                    ui.label(event.get('title', 'No Title')).classes('text-2xl font-bold')
                    ui.label(f"Organized by: {event.get('posted_by', 'Organizer not specified')}").classes('text-lg text-gray-600')
                
                # Event date and time if available
                if event.get('event_date') or event.get('event_time'):
                    with ui.column().classes('items-end'):
                        if event.get('event_date'):
                            ui.label(f"Date: {event['event_date']}").classes('text-gray-700')
                        if event.get('event_time'):
                            ui.label(f"Time: {event['event_time']}").classes('text-gray-700')
            
            # Event images section
            with ui.card().classes('p-6 mb-6'):
                ui.label('Event Images').classes('text-xl font-bold mb-4')
                
                # Get all images from the event data
                image_sources = []
                
                # Add flyer if exists (handle both direct URL and object with url)
                flyer = event.get('flyer')
                if flyer:
                    if isinstance(flyer, dict):
                        flyer = flyer.get('url', '')
                    if isinstance(flyer, str) and flyer.strip():
                        image_sources.append(('Event Flyer', flyer))
                
                # Add main image if exists
                image_url = event.get('image_url')
                if image_url:
                    if isinstance(image_url, dict):
                        image_url = image_url.get('url', '')
                    if isinstance(image_url, str) and image_url.strip():
                        image_sources.append(('Event Image', image_url))
                
                # Add any additional images from images array
                images = event.get('images', [])
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
                                ui.image(url).classes('w-full h-40 object-cover')
                                with ui.card_section():
                                    ui.label(title).classes('text-sm font-medium')
                else:
                    with ui.card().classes('p-4 text-center bg-gray-50'):
                        ui.icon('image', size='2rem').classes('text-gray-400 mb-2')
                        ui.label('No images available').classes('text-gray-500')
            
            # Event details
            with ui.card().classes('p-6 mb-6'):
                ui.label('Event Information').classes('text-xl font-bold mb-4')
                
                # Event metadata
                with ui.grid(columns=2).classes('w-full gap-4 mb-4'):
                    with ui.column():
                        if event.get('location'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('location_on', size='sm').classes('text-gray-500')
                                ui.label(event['location']).classes('text-gray-700')
                        
                        if event.get('event_type'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('category', size='sm').classes('text-gray-500')
                                ui.label(event['event_type']).classes('text-gray-700')
                    
                    with ui.column():
                        if event.get('start_date') or event.get('end_date'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('event', size='sm').classes('text-gray-500')
                                if event.get('start_date') and event.get('end_date'):
                                    ui.label(f"{event['start_date']} to {event['end_date']}").classes('text-gray-700')
                                else:
                                    ui.label(event.get('start_date', event.get('end_date', ''))).classes('text-gray-700')
                        
                        if event.get('registration_deadline'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('event_available', size='sm').classes('text-gray-500')
                                ui.label(f"Registration Deadline: {event['registration_deadline']}").classes('text-gray-700')
                
                # Event description
                ui.label('Description').classes('text-lg font-semibold mt-4 mb-2')
                description = event.get('description', 'No description provided.')
                if isinstance(description, str):
                    ui.html(f"<div class='prose max-w-none'>{description}</div>")
                
                # Additional information if available
                additional_info = event.get('additional_info')
                if additional_info:
                    ui.label('Additional Information').classes('text-lg font-semibold mt-6 mb-2')
                    if isinstance(additional_info, str):
                        ui.html(f"<div class='prose max-w-none'>{additional_info}</div>")
                
                # Speakers/Presenters if available
                speakers = event.get('speakers')
                if speakers:
                    ui.label('Speakers/Presenters').classes('text-lg font-semibold mt-6 mb-2')
                    if isinstance(speakers, str):
                        ui.html(f"<div class='prose max-w-none'>{speakers}</div>")
            
            # Action buttons
            with ui.row().classes('w-full justify-end gap-4 mt-4'):
                ui.button('Back to Events', on_click=lambda: ui.navigate.to('/events')).props('flat')
                
                # Register button with external link if available, otherwise show disabled button
                register_url = event.get('registration_url') or event.get('register_url')
                if register_url:
                    ui.button('Register Now', on_click=lambda: ui.open(register_url)).props('color=primary')
                else:
                    ui.button('Register Now').props('disabled color=primary')
                
                # Save/Bookmark button
                ui.button(icon='bookmark_border').props('flat')
                
                # Share button
                ui.button(icon='share').props('flat')
                
                # Delete button with confirmation dialog
                with ui.dialog() as delete_dialog, ui.card():
                    ui.label('Are you sure you want to delete this event?')
                    with ui.row():
                        ui.button('Cancel', on_click=delete_dialog.close)
                        ui.button('Delete', on_click=lambda: (
                            delete_dialog.close(),
                            asyncio.create_task(delete_event(event_id))
                        )).props('color=red')
                
                ui.button(icon='delete', on_click=delete_dialog.open).props('color=red flat')