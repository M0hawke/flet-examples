#!/usr/bin/env python3
import flet as ft
import math

'''
Simple radial gauge in Python and Flet.

Author: Charles Nichols
Date: April 16, 2023

The gauge images I created in Inkscape years ago.
'''

DESKTOP = True

def main(page: ft.Page):
    
    page.title = 'Flet Radial Percentage Gauge Example'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    
    def animate(e):
        '''
        Take a value from a text control and update the gauge.
        '''
        current_value = user_entry.value
        
        if len(current_value) > 0: 
            current_value = int(current_value)
            curr_degree = int(current_value * 3) + 210 % 360 
            if (current_value <= 50):
                pointer.rotate.angle = math.radians(curr_degree - 360)
            else:
                pointer.rotate.angle = math.radians(abs(curr_degree - 360))
        else:
            pointer.rotate.angle = math.radians(curr_degree - 360)
            
        display.value = current_value
        
        page.update()
          
    # Add gauge needle image. This is the only animation.  
    # I found 800 with decelerate worked well together.     
    pointer = ft.Image(
        src=f"/gauge/radial_gauge_pointer.png",
        fit=ft.ImageFit.CONTAIN,
        rotate=ft.transform.Rotate(-2.6179938779914944, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(800, ft.AnimationCurve.DECELERATE),
    )
    # Add the gauge background image.
    gauge_bg = ft.Image(
        src=f"/gauge/percent_gauge_base.png",
        fit=ft.ImageFit.CONTAIN,
    )
    # Add the cap image, which hides the messy needy ;)
    gauge_cap = ft.Image(
        src=f"/gauge/percent_gauge_cap.png",
        fit=ft.ImageFit.CONTAIN,
    )
    
    display = ft.Text("0", color=ft.colors.BLACK, size=25)
    value_disp = ft.Container(content=display, width=350, height=350, alignment=ft.alignment.center)

    # Stack the images to layer the gauge components.
    gauge_stack = ft.Stack(
        [
            gauge_bg,
            pointer,
            gauge_cap,
            value_disp
        ],
        width=350,
        height=350,
    )
    
    # Add gauge and misc. controls to page.
    user_entry = ft.TextField(value='0')
    page.add(
        gauge_stack,
        user_entry,
        ft.ElevatedButton("Animate!", on_click=animate),
    )
    page.update()

# MAIN
if __name__ == "__main__":
    
    try:
        WEB_PORT = 8000
        
        if DESKTOP:
            ft.app(target=main, assets_dir='assets')
        else:
            ft.app(target=main, assets_dir='assets', port=WEB_PORT, view=ft.WEB_BROWSER)
            
    except Exception as app_error:
        print(app_error)