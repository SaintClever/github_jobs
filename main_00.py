# app and screen manager
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (400, 700)

# widgets
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.chip import MDChip
from kivy.core.image import Image
from kivymd.uix.list import ThreeLineAvatarListItem, MDList, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel


# properties
from kivy.properties import ObjectProperty


# request
import requests


# gitHub Jobs json
url = 'https://jobs.github.com/positions'
json_data = 'https://jobs.github.com/positions.json'
response = requests.get(url=json_data)
response.raise_for_status()
data = response.json()

# print(
#     data['type'],
#     data['url'],
#     data['company'],
#     data['company_url'],
#     data['location'],
#     data['title'],
#     data['description']
# )




class MainMenuScreen(Screen):

    def show_data(self):
        job_desc = ObjectProperty(None)
        job_locate =  ObjectProperty(None)
        
        self.job_location = [self.job_desc.text, self.job_locate.text]
        # print(job_location)

        return self.job_location



class JobListingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        des_n_loc = MainMenuScreen()
        print(des_n_loc.show_data())
        description = des_n_loc.show_data()[0]
        location = des_n_loc.show_data()[1]

        
        json_data = f'https://jobs.github.com/positions.json?description={description}&location={location}'
        print(json_data)

        response = requests.get(url=json_data)
        response.raise_for_status()
        data = response.json()
    
        md_list = MDList()
        scroll = ScrollView() 
        scroll.add_widget(md_list)
        
        
        for i in range(0, len(data)):
            
            company_logo = data[i]['company_logo']
            company = data[i]['company']
            title = data[i]['title']
            location = data[i]['location']
            
            icon_left_widget = IconLeftWidget(icon=f'language-{description}')
            
            list_item = ThreeLineAvatarListItem(
                text=company,
                secondary_text=title,
                tertiary_text=location,
            )
            
            list_item.add_widget(icon_left_widget)
            md_list.add_widget(list_item)
            
        self.add_widget(scroll)
                


    # def display_list(self):
    #     self.job = self.manager.get_screen('main_menu').job_desc.text
    #     self.loc = self.manager.get_screen('main_menu').job_locate.text
    #     print(self.job, self.loc)
        
    #     self.json_data = f'https://jobs.github.com/positions.json?description={self.job}&location={self.loc}'
    
    

class GitHubJobsApp(MDApp):
    def build(self):
        
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '500' # 200
        self.theme_cls.theme_style = 'Light'  # 'Light'
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenuScreen(name='main_menu'))
        screen_manager.add_widget(JobListingsScreen(name='job_listings'))
        
        return screen_manager

GitHubJobsApp().run()