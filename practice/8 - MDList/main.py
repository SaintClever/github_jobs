from kivymd.app import MDApp
from kivymd.uix.screen import Screen

from kivymd.uix.list import (
    MDList, ThreeLineListItem, ThreeLineAvatarListItem,
    IconLeftWidget, ImageLeftWidget
)

from kivy.uix.scrollview import ScrollView


class JobHubApp(MDApp):
    
    def build(self):
        screen = Screen()
        
        list_view = MDList()
        scroll = ScrollView()
        
        # item1 = OneLineListItem(text='item 1')
        # item2 = OneLineListItem(text='item 2')
                
        # list_view.add_widget(item1)
        # list_view.add_widget(item2)

        # scroll.add_widget(list_view)
        # screen.add_widget(scroll)
        
        
        # for loop
        for i in range(1, 21):
            # icon = IconLeftWidget(icon='android')
            image = ImageLeftWidget(source='facebook_icon.png')
            items = ThreeLineAvatarListItem(
                text=f'item {i}',
                secondary_text='Hello world',
                tertiary_text='third text'
            )
            items.add_widget(image)
            list_view.add_widget(items)
            
        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        
        return screen
        
        




JobHubApp().run()