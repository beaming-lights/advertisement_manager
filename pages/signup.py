from nicegui import ui
from components.auth_layout import create_auth_page
from components.auth_components import create_text_input, create_social_auth_buttons

def show_signup_page():
    """Show the signup page with the auth layout."""
    create_auth_page(
        content_callback=create_signup_form,
        title='Create your account',
        subtitle='Join our community today',
        image_url='https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    )

def create_signup_form():
    """Create the signup form content using auth components."""
    # Initialize form fields
    name = None
    email = None
    password = None
    confirm_password = None
    terms_checkbox = None
    
    with ui.column().classes('w-full space-y-4'):
        # Name input
        name = create_text_input(
            label='Full Name',
            icon_name='person'
        )
        
        # Email input
        email = create_text_input(
            label='Email Address',
            icon_name='email'
        )
        
        # Password input with strength indicator
        with ui.column().classes('w-full space-y-2'):
            password = create_text_input(
                label='Password',
                icon_name='lock',
                is_password=True,
                on_enter=lambda e: handle_enter_key_signup(e, name.value, email.value, password.value, confirm_password.value, terms_checkbox.value) if all([name, email, password, confirm_password, terms_checkbox]) else None
            )
            
            # Password requirements
            with ui.column().classes('w-full space-y-1'):
                ui.label('Password must contain:').classes('text-xs text-gray-500 font-medium')
                for text in [
                    'At least 8 characters',
                    'At least one number',
                    'At least one special character'
                ]:
                    with ui.row().classes('items-center'):
                        ui.icon('check_circle', size='xs').classes('text-xs mr-1 text-gray-300')
                        ui.label(text).classes('text-xs text-gray-500')
        
        # Confirm Password
        confirm_password = create_text_input(
            label='Confirm Password',
            icon_name='lock',
            is_password=True,
            on_enter=lambda e: handle_enter_key_signup(e, name.value, email.value, password.value, confirm_password.value, terms_checkbox.value) if all([name, email, password, confirm_password, terms_checkbox]) else None
        )
        
        # Terms and Conditions
        with ui.column().classes('w-full space-y-2 mt-2'):
            with ui.row().classes('items-start'):
                terms_checkbox = ui.checkbox('').classes('mt-1')
                with ui.column().classes('ml-2'):
                    with ui.row().classes('items-baseline flex-wrap'):
                        ui.label('I agree to the').classes('text-xs text-gray-600')
                        ui.link('Terms of Service', '/terms').classes('text-xs text-blue-600 hover:underline mx-1')
                        ui.label('and').classes('text-xs text-gray-600')
                        ui.link('Privacy Policy', '/privacy').classes('text-xs text-blue-600 hover:underline ml-1')
        
        # Sign Up button
        ui.button('Create Account', 
            on_click=lambda: on_signup(name.value, email.value, password.value, confirm_password.value, terms_checkbox.value),
            icon='person_add'
        ).props('unelevated') \
         .classes('w-full bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white py-2.5 text-base font-medium rounded-lg shadow-md hover:shadow-lg transition-all duration-200 mt-2')
        
        # Social auth buttons
        create_social_auth_buttons(auth_type='signup')
        
        # Login link
        with ui.row().classes('w-full justify-center mt-4 pt-3 border-t border-gray-100'):
            ui.label('Already have an account?').classes('text-sm text-gray-500')
            ui.link('Sign in', '/login').classes('ml-1 text-sm font-medium text-blue-600 hover:text-blue-700 hover:underline')

def handle_enter_key_signup(e, name: str, email: str, password: str, confirm_password: str, accepted_terms: bool):
    """Handle Enter key press in confirm password field."""
    if e.key == 'Enter':
        on_signup(name, email, password, confirm_password, accepted_terms)

def on_signup(name: str, email: str, password: str, confirm_password: str, terms_accepted: bool):
    """Handle signup button click with elegant notifications."""
    if not all([name, email, password, confirm_password]):
        ui.notify('Please fill in all fields', 
                 type='warning',
                 position='top',
                 close_button='×',
                 timeout=3000)
    elif not terms_accepted:
        ui.notify('Please accept the terms and conditions',
                 type='warning',
                 position='top',
                 close_button='×',
                 timeout=3000)
    elif len(password) < 8:
        ui.notify('Password must be at least 8 characters',
                 type='warning',
                 position='top',
                 close_button='×',
                 timeout=3000)
    elif password != confirm_password:
        ui.notify('Passwords do not match',
                 type='warning',
                 position='top',
                 close_button='×',
                 timeout=3000)
    else:
        ui.notify(f'Account created for {email}. Welcome to JobCamp!', 
                 type='positive',
                 position='top',
                 close_button='×',
                 timeout=3000)
        ui.navigate.to('/')

# For direct testing
if __name__ in {'__main__', '__mp_main__'}:
    show_signup_page()
    ui.run()
