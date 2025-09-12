from nicegui import ui

from components.footer import show_footer
from components.header import show_header

# Import all sections
from sections.blog import show_blog_section
from sections.categories import show_categories_section
from sections.companies import show_companies_section
from sections.hero import show_hero_section
from sections.how_it_works import show_how_it_works_section
from sections.stats import show_stats_section


def show_home_page():
    """Creates the JobCamp-style home page by assembling modular sections."""
    # Main page container
    with ui.column().classes('w-full min-h-screen flex flex-col'):
        # Header section
        with ui.element('header').classes('w-full'):
            show_header()
        
        # Main content section
        with ui.column().classes('flex-1'):
            show_hero_section()
            show_categories_section()
            # show_how_it_works_section()
            # show_stats_section()
            show_blog_section()
        
        # Footer section (includes newsletter)
        with ui.element('footer').classes('w-full'):
            show_footer()
