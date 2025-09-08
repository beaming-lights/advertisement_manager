from nicegui import ui, app
from pages.home import show_home_page as home_page

def show_header():
    with ui.row():
        ui.button('Home', on_click=lambda: ui.open('/home'))
        ui.button('Add Event', on_click=lambda: ui.open('/add_event'))
        ui.button('View Event', on_click=lambda: ui.open('/view_event'))
        ui.button('Edit Event', on_click=lambda: ui.open('/edit_event'))
        ui.button('Log Out', on_click=lambda: ui.open('/'))