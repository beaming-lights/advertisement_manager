from nicegui import ui
from components.header import show_header
from components.footer import show_footer

def show_contact_page():
    """Creates the page for contacting the company."""
    show_header()

    with ui.column().classes('w-full max-w-4xl mx-auto p-4 md:p-8 relative'):
        ui.label('Contact Us').classes('text-4xl lg:text-5xl font-bold text-gray-900 text-center mb-8')
        ui.label('We\'d love to hear from you! Please fill out the form below to get in touch.').classes('text-lg text-gray-600 text-center mb-16')

        with ui.card().classes('w-full p-8'):
            with ui.column().classes('w-full gap-6'):
                ui.input(label='Your Name', placeholder='Enter your full name').classes('form-input w-full')
                ui.input(label='Your Email', placeholder='Enter your email address').classes('form-input w-full')
                ui.textarea(label='Message', placeholder='Write your message here...').classes('form-input w-full').style('min-height: 150px')
                ui.button('Send Message', on_click=lambda: ui.notify('Message sent! (Not really)', type='positive')).classes('btn btn-primary w-full py-3')

    show_footer()
