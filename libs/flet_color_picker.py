import flet as ft
import matplotlib

'''
FletCalendar in Python.

Author: C. Nichols <mohawke@gmail.com>

Requirements: You need to install Flet and MatPlotLib
'''

# Grap the colors dictionary from Matplot
MPCOLORS = matplotlib.colors.cnames

class ColorPicker(ft.UserControl):
    
    def __init__(self, page, output_control):
        super().__init__()
        
        self.MPColors = MPCOLORS 
        self.page = page
        self.output_control = output_control
        color_grid = self.build_color_grid()
        
        # Setup the Flet AlertDialog.
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Select Color"),
            content=ft.Container(color_grid,bgcolor="#3d2d2f", border=ft.border.all(1, ft.colors.BLUE_400), border_radius=15),
            actions=[
                ft.TextButton("Done", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss="",
        )
        
        self.page.update()
        
    def build_color_grid(self):
        '''
        Create a Flet GridView to house the colors
        and populate with a series of IconButtons
        that represent each color.
        '''
        
        color_grid = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=90,
            child_aspect_ratio=1,
            spacing=5,
            run_spacing=5,
            width=350,
            height=350,
        )
        
        for color_name,color_hex in sorted(self.MPColors.items()):
            color_grid.controls.append(
                ft.IconButton(
                    icon=ft.icons.WATER_DROP,
                    icon_color=color_hex,
                    icon_size=50,
                    tooltip=color_name.title(),
                    on_click=self.picked_color,
                    data=color_hex,
                )
            )
            
        return color_grid
    
    # COLOR PICKER
    def picked_color(self, e):
        '''
        Handle the IconButton click.
        We set the result to a Flet control 
        added in main.
        '''
        hex_color = e.control.data
        self.output_control.bgcolor = hex_color
        self.page.update()
        
    def close_dlg(self, e):
        '''
        Opens the dialog.
        '''
        self.dlg_modal.open = False
        self.page.update()

    def open_dlg_modal(self, e):
        '''
        Closes the dialog.
        '''
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

"""
Usage:

    import controls.color_picker
    
    # Instantiate the color picker.
    swatch = ft.Container(bgcolor=ft.colors.BLACK, width=100, height=23, border = ft.border.all(1, ft.colors.BLACK), border_radius=ft.border_radius.all(15))
    my_color_picker = ColorPicker(page, swatch)
    
    # Add to page
    main_controls = [
        ft.Container(ft.Text("Pick A Color")),
        ft.ElevatedButton("Select Color", icon=ft.icons.COLORIZE, on_click=my_color_picker.open_dlg_modal),
        my_color_picker.output_control
    ]

"""