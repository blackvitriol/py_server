from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import ObjectProperty

colors = {
    "Teal": {
        "200": "#212121",
        "500": "#212121",
        "700": "#212121",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#202020",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "A7 Server Interface"

    MDTabs:
        id: tabs


<Tab>

    MDIconButton:
        id: icon
        icon: root.icon
        icon_size: "48sp"
        theme_icon_color: "Custom"
        icon_color: "white"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

    icon = ObjectProperty()