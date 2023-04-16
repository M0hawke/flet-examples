import flet as ft

'''
Flet HashTags in Python for Flet.

Author: C. Nichols <mohawke@gmail.com>

Requirements: You need to install Flet.
'''

class HashTags(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        
        self.page = page
        self.tags = ft.TextField(label="Add hashtags", counter_text="Tag Count: 0", on_submit=self.add_tag, 
                        on_change=self.clear_help, border=ft.InputBorder.UNDERLINE, filled=True,
                        helper_style={'color':ft.colors.RED}, counter_style={'color':ft.colors.PINK_50}) 
        self.tag_list = ft.Row(spacing=6, auto_scroll=True)
        self.build()
        
    # *** Functions.
    def delete_tag(self, e):
        '''
        Delete a tag by index.
        '''

        for index, row_item in enumerate(self.tag_list.controls):
            if e.control.data == row_item.controls[0].text:
                break
        
        self.tag_list.controls.pop(index) # Pop the tag out of the list.
        self.tags.counter_text = "Tag Count: %s" % len(self.tag_list.controls) # Update counter.
            
        self.tags.focus()      # Focus the TextField.
        self.tag_list.update() # Update tags list.
        self.page.update()     # Update page.
        
    def add_tag(self, e):
        '''
        Add a tag as an ElevatedButton and add to a ListView.
        '''
        
        t = "#%s" % self.tags.value.strip()

        tag_btn = ft.ElevatedButton(text=t, icon=ft.icons.CLOSE_OUTLINED, on_click=self.delete_tag, data=t)
        tag_item = ft.Row(controls=[tag_btn])
        has_tag = False
        for tag in self.tag_list.controls:
            # Ignore existing tags.
            if tag_item.controls[0].text == tag.controls[0].text:
                has_tag = True
        
        if not has_tag:
            self.tag_list.controls.append(tag_item)
            self.tags.counter_text = "Tag Count: %s" % len(self.tag_list.controls) # Update counter.
      
            self.tags.value = ""
        else:
            self.tags.helper_text = "Tag exists."
        
        self.tags.focus()      # Focus the TextField.
        self.tag_list.update() # Update tags list.
        self.page.update()     # Update page.
        
    def clear_help(self, e):
        self.tags.helper_text = ""
        self.page.update()     # Update page.
        
    def build(self):
        return ft.Column(controls=[self.tags, self.tag_list], expand=True)
