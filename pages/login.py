from nicegui import ui
from components.auth_layout import create_auth_page
from components.auth_components import create_text_input, create_social_auth_buttons

def show_login_page():
    """Show the login page with the auth layout."""
    create_auth_page(
        content_callback=create_login_form,
        title='Welcome back',
        subtitle='Sign in to your account',
        image_url='https://images.unsplash.com/photo-1571902943202-507ec2618e8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    )

def create_login_form():
    """Create the login form content using auth components."""
    # Initialize form fields
    email = None
    password = None
    remember_me = None
    
    with ui.column().classes('w-full space-y-4'):
        # Email input
        email = create_text_input(
            label='Email Address',
            icon_name='email',
            on_enter=lambda e: handle_enter_key_login(e, email.value, password.value) if email and password else None
        )
        
        # Password input
        password = create_text_input(
            label='Password',
            icon_name='lock',
            is_password=True,
            show_forgot_link=True,
            on_enter=lambda e: handle_enter_key_login(e, email.value, password.value) if email and password else None
        )
        
        # Remember Me
        with ui.row().classes('items-center justify-between w-full'):
            remember_me = ui.checkbox('Keep me signed in').classes('text-sm text-gray-600')
        
        # Sign In Button
        ui.button('Sign In', 
            on_click=lambda: on_login(email.value, password.value),
            icon='login'
        ).props('unelevated') \
         .classes('w-full bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white py-2.5 text-base font-medium rounded-lg shadow-md hover:shadow-lg transition-all duration-200')
        
        # Social auth buttons
        create_social_auth_buttons(auth_type='signin')
        
        # Sign up link
        with ui.row().classes('w-full justify-center mt-4 pt-3 border-t border-gray-100'):
            ui.label("Don't have an account?").classes('text-sm text-gray-500')
            ui.link('Sign up', '/signup').classes('ml-1 text-sm font-medium text-blue-600 hover:text-blue-700 hover:underline')

def handle_enter_key_login(e, email: str, password: str):
    """Handle Enter key press in password field."""
    if e.key == 'Enter':
        on_login(email, password)

def on_login(email: str, password: str):
    """Handle login button click with elegant notifications."""
    if not email or not password:
        ui.notify('Please fill in all fields', 
                 type='warning',
                 position='top',
                 close_button='×',
                 timeout=3000)
    else:
        ui.notify(f'Welcome back! Signing in as {email}', 
                 type='positive',
                 position='top',
                 close_button='×',
                 timeout=2000)
