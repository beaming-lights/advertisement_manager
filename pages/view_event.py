from nicegui import ui, app
from components.header import show_header


def show_event_page():
    show_header()
    ui.label('Welcome to the Event Page')