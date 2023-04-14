#!/usr/bin/env python3
import flet as ft
from controls.flet_calendar import FletCalendar

DESKTOP  = True
WEB_PORT = 8000

def main(page: ft.Page):
    
    # PAGE SETTINGS :: Set to dark or light
    page.title = "Flet Calendar Dialog"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    page.dark_theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    
    page.theme_mode = 'dark'
    # END PAGE SETTINGS
    
    # Instantiate the calendar class.
    search_cal = FletCalendar(page)
    
    def open_calendar(e):
        '''
        Opens the calendar dialog.
        '''
        search_cal.open_dlg_modal()
            
    # Add a icon button to open the dialog and a text control to see what's picked.
    page_content = ft.Row(
        [
            ft.ElevatedButton("Open Calendar", icon=ft.icons.CALENDAR_VIEW_MONTH, on_click=open_calendar),
            search_cal.output
        ],
    )

    # Add controls to page and update.
    page.add(page_content)
    page.update()
            
# MAIN
if __name__ == "__main__":
    
    try:
        
        if DESKTOP:
            ft.app(target=main)
        else:
            ft.app(target=main, port=WEB_PORT, view=ft.WEB_BROWSER)
            
    except Exception as app_error:
        print(app_error)