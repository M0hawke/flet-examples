#!/usr/bin/env python3
import flet as ft

from controls.flet_tags import HashTags 

DESKTOP  = True
WEB_PORT = 8000

def main(page: ft.Page):
    
    # PAGE SETTINGS :: Set to dark or light
    page.title = "Flet Calendar Dialog"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    page.dark_theme = ft.theme.Theme(color_scheme_seed=ft.colors.PINK)
    
    page.theme_mode = 'dark'
    # END PAGE SETTINGS
    
    # Instantiate the HashTags class.
    mytags = HashTags(page)
    
    # Add to page and update.
    page.add(mytags)
    
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