#!/usr/bin/env python3
import flet as ft

from flet_color_picker import ColorPicker

DESKTOP  = True
WEB_PORT = 8000

def main(page: ft.Page):
    
    # PAGE SETTINGS :: Set to dark or light
    page.title = "Flet Calendar Dialog"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    page.dark_theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    
    page.theme_mode = 'dark'
    # END PAGE SETTINGS
    
    # Instantiate the color picker.
    swatch = ft.Container(bgcolor=ft.colors.BLACK, width=100, height=23, border = ft.border.all(1, ft.colors.BLACK), border_radius=ft.border_radius.all(15))
    my_color_picker = ColorPicker(page, swatch)
    
    #  We will use an ElevatedButton to open the picker.
    page_content = [
        ft.ElevatedButton("Select Color", icon=ft.icons.COLORIZE, on_click=my_color_picker.open_dlg_modal),
        my_color_picker.output_control
    ]
        
    # Add controls to the page.
    page.add( ft.Row(page_content) )
    
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
