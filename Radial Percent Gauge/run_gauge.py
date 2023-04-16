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
          
    # Add gauge needle image. This is the only animation.       
    pointer = ft.Image(
        src=f"/gauge/radial_gauge_pointer2.png",
        fit=ft.ImageFit.CONTAIN,
        rotate=ft.transform.Rotate(-2.6179938779914944, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.DECELERATE),
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
    
    # Build up the containers
    gauge_continer = ft.Container(
        pointer,
        width=350,
        height=350,
        alignment=ft.alignment.center
    )
    
    gauge_pointer_cap = ft.Container(
        gauge_cap,
        width=350,
        height=350,
        alignment=ft.alignment.center
    )
    # Stack one upon the other to layer the gauge.
    gauge_stack = ft.Stack(
        [
            gauge_bg,
            gauge_continer,
            gauge_pointer_cap
        ],
        width=350,
        height=350,
    )
    
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
    
        page.update()
    
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
            ft.app(target=main, port=WEB_PORT, view=ft.WEB_BROWSER)
            
    except Exception as app_error:
        print(app_error)