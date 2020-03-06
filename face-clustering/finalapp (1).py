from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.theming import ThemeManager
from kivymd.uix.toolbar import MDToolbar
from kivy.factory import Factory
KV = '''
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title:"This is MDtoolbar"
        md_bg_color:app.theme_cls.primary_color
        left_action_items:[['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
        MDIconButton:
            icon:"language-python"
            pos_hint:{"center_x": 0.5, "center_y": 0.5}
    ScrollView:
        do_scroll_y:"true"
        bar_color:(0,0,1,1)
        bar_width:3



         
        GridLayout:
            cols: 3
            row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)
            
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26]Cat 1[/size][size=14]cat-1.jpg[/size]"
                #on_Touch_down:
                    
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26]Cat 2[/size][size=14]cat-2.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color

            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
            
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
        
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
            
            SmartTileWithLabel:
                source: "image.jpeg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size][size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
    

'''


class MyApp(MDApp):

    def build(self):

        root= Builder.load_string(KV)
        #button_inst=Factory.imgLayout()
        theme_cls = ThemeManager()
        pass
        return root
MyApp().run()