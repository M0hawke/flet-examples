#!/usr/bin/env python3
import flet as ft
import math
import time
import random

'''
Simple radial gauge in Python and Flet.

Author: Charles Nichols
Date: April 16, 2023

The gauge images I created in Inkscape years ago.
'''

DESKTOP = True

def main(page: ft.Page):
    
    page.title = 'Flet Radial Seconds Gauge Example'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    
    def animate(e):
        '''
        Take a value from a text control and update the gauge.
        '''
        some_times = [30, 35, 28, 18, 60, 53, 7, 0]
        
        for current_value in some_times:
            if current_value > 0: 
                
                # Calculate the degree from seconds for positive degrees.
                curr_degree = int(360 / 60) * current_value
                pointer_value = math.radians(pointer.rotate.angle)
                
                if (current_value == 60):
                    pointer.rotate.angle = math.radians(360)
                    
                if pointer_value < 0:
                    pointer.rotate.angle = math.radians(360 - curr_degree)
                else:
                    pointer.rotate.angle = math.radians(360 + curr_degree)
                    
            else:
                pointer.rotate.angle = math.radians(360 - 0)
                
            display.value = current_value
            
            page.update()
            
            time.sleep(3)
          
    # Add gauge needle image. This is the only animation.  
    # I found 800 with decelerate worked well together.     
    pointer = ft.Image(
        src=f"/gauge/radial_gauge_pointer.png",
        fit=ft.ImageFit.CONTAIN,
        rotate=ft.transform.Rotate(6.28, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(800, ft.AnimationCurve.DECELERATE),
    )
    # Add the gauge background image.
    gauge_bg = ft.Image(
        src=f"/gauge/seconds_gauge_base.png",
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
    page.add(
        gauge_stack,
        ft.ElevatedButton("Start!", on_click=animate),
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