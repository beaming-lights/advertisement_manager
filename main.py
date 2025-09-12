import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from nicegui import ui, app
from pages.view_event import show_event_page
from pages.edit_event import show_edit_event_page
from pages.add_event import show_add_event_page, global_job_listings
from pages.home import show_home_page
from pages.login import show_login_page
from pages.signup import show_signup_page
from pages.jobs import show_jobs_page
from pages.companies import show_companies_page
from pages.contact import show_contact_page
from pages.candidate_profile import show_candidate_profile_page, show_candidate_list_page
from pages.company_profile import show_company_profile_page, show_company_list_page
from pages.edit_candidate_profile import show_edit_candidate_profile_page
from pages.view_job import show_view_job_page
from pages.debug_api import show_debug_api_page

# Add custom CSS
ui.add_head_html('''
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>
    /* Import our custom styles */
    @import url("/static/styles.css");
    @import url("/static/jobcamp_theme.css");
    
    /* Additional modern enhancements */
    .q-card {
        border-radius: 16px !important;
        border: 1px solid #E5E7EB !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .q-card:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
    }
    
    .q-btn {
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .q-btn:hover {
        transform: translateY(-2px) !important;
    }
    
    .q-field__control {
        border-radius: 12px !important;
    }
    
    .q-input .q-field__control {
        border: 2px solid #E5E7EB !important;
    }
    
    .q-input.q-field--focused .q-field__control {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }
</style>
''')

# Configure custom colors for the job board theme
ui.colors(
    primary='#4F46E5',  # Indigo
    secondary='#06B6D4',  # Cyan
    accent='#10B981',  # Emerald
    dark='#1F2937',  # Gray-800
    positive='#10B981',  # Emerald
    negative='#EF4444',  # Red
    info='#3B82F6',  # Blue
    warning='#F59E0B'  # Amber
)

@ui.page('/')
def home_page():
    show_home_page()

@ui.page('/home')
def home_redirect():
    ui.navigate.to('/')

@ui.page('/jobs')
def jobs_page():
    show_jobs_page()

@ui.page('/view-job/{job_id}')
def view_job_page(job_id: str):
    show_view_job_page(job_id=job_id)

@ui.page('/companies')
def companies_page():
    show_companies_page()
    
@ui.page('/post-job')
def post_job_page():
    show_add_event_page()
    
@ui.page('/edit-job')
def edit_job_page():
    show_edit_event_page()

@ui.page('/edit-job/{job_id}')
def edit_specific_job_page(job_id: str):
    show_edit_event_page(job_id=job_id)

@ui.page('/contact')
def contact_page():
    show_contact_page()

@ui.page('/login')
def login_page():
    show_login_page()

@ui.page('/signin')
def signin_redirect():
    ui.navigate.to('/login')

@ui.page('/new_event')
def new_event_page():
    # Redirect to the post-job page which shows the add event form
    ui.navigate.to('/post-job')

@ui.page('/signup')
def signup_page():
    """Show the signup page."""
    show_signup_page()

@ui.page('/candidates')
def candidates_page():
    """Show the candidates list page."""
    show_candidate_list_page()

@ui.page('/candidates-profile-simple')
def candidates_profile_simple_page():
    """Redirect to candidates list page."""
    ui.navigate.to('/candidates')

@ui.page('/candidates_profile_simple')
def candidates_profile_simple_underscore_page():
    """Redirect to candidates list page."""
    ui.navigate.to('/candidates')

@ui.page('/candidates_profile')
def candidates_profile_underscore_page():
    """Redirect to candidates list page."""
    ui.navigate.to('/candidates')

@ui.page('/candidate-profile/{candidate_id}')
def candidate_profile_page(candidate_id: str):
    """Show individual candidate profile."""
    show_candidate_profile_page(candidate_id)

@ui.page('/company-profile/{company_id}')
def company_profile_page(company_id: str):
    """Show individual company profile."""
    show_company_profile_page(company_id)

@ui.page('/candidate-profile/{candidate_id}/edit')
def edit_candidate_profile_page(candidate_id: str):
    """Edit candidate profile."""
    show_edit_candidate_profile_page(candidate_id)

@ui.page('/company-list')
def company_list_page():
    """Show the companies list page."""
    show_company_list_page()

@ui.page('/debug-api')
def debug_api_page():
    """Show the API debug page."""
    show_debug_api_page()

# Configure static files
app.add_static_files('/static', 'static')

# All routes are now defined with @ui.page decorators in their respective files

if __name__ in {"__main__", "__mp_main__"}:
    print("Starting JobCamp application...")
    print(f"Python executable: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Static files directory: {os.path.join(os.getcwd(), 'static')}")
    
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
ui.run(
        title="JobCamp - Find Your Dream Job",
        port=8081,
        show=True,
        reload=True,
        dark=False,
        storage_secret="your-secret-key-here"
    )