from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.icon_definitions import md_icons
from kivy_design import *

class Interface(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            tab = Tab(title="This is " + name_tab, icon=name_tab)
            self.root.ids.tabs.add_widget(tab)


Interface().run()