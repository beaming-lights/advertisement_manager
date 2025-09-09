from nicegui import ui, app
from pages.view_event import show_event_page
from pages.edit_event import show_edit_event_page
from pages.add_event import show_add_event_page, global_job_listings
from pages.home import show_home_page

# Add custom CSS
ui.add_head_html('''
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>
    /* Import our custom styles */
    @import url("/static/styles.css");
    
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
    show_home_page()  # This will show the jobs listing

@ui.page('/home')
def home_redirect():
    ui.open('/')

@ui.page('/jobs')
def jobs_page():
    show_home_page()  # Show the jobs listing page

@ui.page('/jobs/{job_id}')
def view_job_page(job_id: str):
    show_event_page(job_id=job_id)
    
@ui.page('/post-job')
def post_job_page():
    show_add_event_page()
    
@ui.page('/edit-job')
def edit_job_page():
    show_edit_event_page()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="JobCamp - Find Your Dream Job", favicon="🚀", dark=False)