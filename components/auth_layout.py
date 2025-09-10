from nicegui import ui

def create_auth_page(content_callback, title: str, subtitle: str, image_url: str = None):
    """
    Creates a split layout for authentication pages with no scrolling.
    
    Args:
        content_callback: Function that returns the form content
        title: Page title
        subtitle: Page subtitle
        image_url: Optional custom image URL
    """
    # Default image if none provided
    if not image_url:
        image_url = 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    
    # Set the root element to prevent any page scrolling
    ui.query('body').style('overflow: hidden')
    
    # Main container with fixed positioning and no scrolling
    with ui.element('div').classes('fixed inset-0 flex flex-col h-screen w-screen bg-gray-50'):
        with ui.row().classes('flex-1 flex-col lg:flex-row w-full h-full overflow-hidden'):
            # Left side - Image (hidden on mobile)
            with ui.column().classes('hidden lg:flex lg:w-1/2 h-full relative'):
                # Background container with image
                with ui.element('div').classes('absolute inset-0 overflow-hidden bg-gray-200'):
                    # Image with error handling and fallback
                    try:
                        img = ui.image(image_url).classes('w-full h-full object-cover')
                        img.on('error', lambda e, img=img: (
                            img.source == '' or setattr(img, 'source', '')
                        ))
                    except Exception as e:
                        print(f"Error loading image: {e}")
                    
                    # Gradient overlay
                    with ui.element('div').classes('absolute inset-0 bg-gradient-to-br from-emerald-500/80 to-teal-600/80'):
                        pass
                
                # Content overlay
                with ui.column().classes('relative z-10 flex flex-col justify-center p-16 text-white h-full'):
                    with ui.column().classes('max-w-md'):
                        ui.icon('work', size='4rem', color='white').classes('mb-6')
                        ui.label('Welcome to JobCamp').classes('text-4xl font-bold mb-4')
                        ui.label('Find your dream job today').classes('text-xl opacity-90')
                        
                        # Features list
                        with ui.column().classes('mt-8 space-y-4'):
                            features = [
                                ('search', 'Search thousands of job listings'),
                                ('star', 'Save your favorite jobs'),
                                ('notifications', 'Get job alerts'),
                                ('trending_up', 'Grow your career')
                            ]
                            
                            for icon, text in features:
                                with ui.row().classes('items-center space-x-3'):
                                    ui.icon(icon, color='white').classes('text-xl')
                                    ui.label(text).classes('text-white/90')
            
            # Right side - Form (scrollable only this section if needed)
            with ui.column().classes('w-full lg:w-1/2 h-full flex flex-col'):
                # Scrollable area for form content
                with ui.scroll_area().classes('flex-1 w-full'):
                    with ui.column().classes('w-full h-full p-6 md:p-8 lg:p-12'):
                        # Logo and back button (mobile)
                        with ui.row().classes('w-full justify-between items-center lg:hidden mb-6'):
                            with ui.link('/').classes('flex items-center space-x-2'):
                                with ui.row().classes('w-10 h-10 bg-emerald-600 rounded-lg flex items-center justify-center'):
                                    ui.icon('work', color='white')
                                ui.label('JobCamp').classes('text-xl font-bold text-emerald-600')
                            
                            with ui.link('/').classes('text-gray-500 hover:text-emerald-600'):
                                ui.icon('arrow_back').classes('text-xl')
                        
                        # Main content container with max-width for better readability
                        with ui.column().classes('max-w-md mx-auto w-full'):
                            # Header
                            with ui.column().classes('text-center lg:text-left mb-8'):
                                ui.label(title).classes('text-3xl font-extrabold text-gray-900')
                                ui.label(subtitle).classes('mt-1 text-gray-500')
                            
                            # Form content from callback
                            content_callback()
                
                # Footer (sticky at the bottom of the form section)
                with ui.column().classes('w-full p-4 bg-white border-t border-gray-100'):
                    with ui.column().classes('max-w-md mx-auto w-full'):
                        ui.label('© 2023 JobCamp. All rights reserved.').classes('text-xs text-center text-gray-500')
                        with ui.row().classes('justify-center space-x-4 mt-2'):
                            ui.link('Terms', '/terms').classes('text-xs text-emerald-600 hover:underline')
                            ui.link('Privacy', '/privacy').classes('text-xs text-emerald-600 hover:underline')
                            ui.link('Contact', '/contact').classes('text-xs text-emerald-600 hover:underline')
