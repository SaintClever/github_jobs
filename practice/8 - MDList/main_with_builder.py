from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem


list_helper = '''
Screen:
    ScrollView:
        MDList:
            id: container
            
'''



class JobHubApp(MDApp):
    
    def build(self):
        screen = Builder.load_string(list_helper)      
        return screen
        
        

    def on_start(self):
        for i in range(1, 21):
            items = OneLineListItem(text=f'item {i}')
            self.root.ids.container.add_widget(items)


JobHubApp().run()