from nicegui import ui, app
from pages.home import show_home_page as home_page

def show_header():
    with ui.row():
        ui.link('Advertisement Manager', '/home')
        ui.link('add event', '/add_event')
        ui.button('Home', on_click=home_page)
        ui.button('Add Event', on_click=lambda: app.open('/add_event'))
        ui.button('View Event', on_click=lambda: app.open('/view_event'))
        ui.button('Edit Event', on_click=lambda: app.open('/edit_event'))