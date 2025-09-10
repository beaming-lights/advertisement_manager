from nicegui import ui

def create_auth_form(title: str, subtitle: str, form_content_callback, footer_content_callback=None):
    """
    Base authentication form component
    
    Args:
        title: Form title
        subtitle: Form subtitle
        form_content_callback: Function that returns the form fields
        footer_content_callback: Optional function for footer content
    """
    with ui.column().classes('w-full space-y-4'):
        # Header
        with ui.column().classes('w-full text-center mb-2'):
            ui.label(title).classes('text-2xl font-bold text-gray-800')
            ui.label(subtitle).classes('text-sm text-gray-500')
        
        # Form content
        form_content_callback()
        
        # Footer content if provided
        if footer_content_callback:
            footer_content_callback()

def create_text_input(label: str, icon_name: str, is_password=False, show_forgot_link=False, on_enter=None, on_change=None):
    """Create a styled text input with icon
    
    Args:
        label: Input label text
        icon_name: Name of the icon to display
        is_password: Whether this is a password field
        show_forgot_link: Whether to show 'Forgot?' link
        on_enter: Callback for Enter key press
        on_change: Callback for input value change
    """
    with ui.column().classes('w-full space-y-1'):
        with ui.row().classes('w-full justify-between items-center'):
            ui.label(label).classes('text-sm font-medium text-gray-700')
            if show_forgot_link:
                ui.link('Forgot?', '/forgot-password').classes('text-xs text-blue-600 hover:text-blue-700 hover:underline')
        
        # Create input field with proper NiceGUI syntax
        input_field = ui.input(
            placeholder=f'Enter your {label.lower()}',
            password=is_password,
            password_toggle_button=is_password
        ).props('standout dense') \
         .classes('w-full bg-gray-50 rounded-lg border-gray-200 hover:border-blue-300 focus:border-blue-500')
        
        if on_enter:
            input_field.on('keypress', on_enter)
        if on_change:
            input_field.on('update:model-value', on_change)
            
        return input_field

def create_social_auth_buttons(auth_type='signin'):
    """Create social authentication buttons"""
    with ui.column().classes('w-full'):
        # Divider
        with ui.row().classes('w-full items-center my-3'):
            ui.separator().classes('flex-1 bg-gray-200')
            ui.label('or continue with').classes('px-3 text-xs text-gray-500 bg-white')
            ui.separator().classes('flex-1 bg-gray-200')
        
        # Social buttons
        with ui.row().classes('w-full justify-center space-x-4'):
            for provider, icon, color in [
                ('Google', 'google', '#DB4437'),
                ('GitHub', 'code', '#333333')
            ]:
                ui.button(
                    text=f'Continue with {provider}',
                    icon=icon,
                    on_click=lambda p=provider: handle_social_auth(p.lower(), auth_type)
                ).props('flat outline') \
                 .classes('flex-1 h-10 rounded-lg border border-gray-200 hover:shadow-sm transition-all duration-200 text-gray-700')

def handle_social_auth(provider: str, auth_type: str):
    """Handle social authentication"""
    ui.notify(f'Redirecting to {provider.capitalize()} for {auth_type}...', type='info')
    # TODO: Implement social authentication logic
    pass
