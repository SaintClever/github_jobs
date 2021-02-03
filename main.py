# app and screen manager
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager, Screen


# widgets
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.chip import MDChip
from kivy.core.image import Image


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
    job_desc = ObjectProperty(None)
    job_locate = ObjectProperty(None)

    def show_data(self, *args):
        print(f'https://jobs.github.com/positions.json?description={self.job_desc.text}&location={self.job_locate.text}')




class JobListingsScreen(Screen):
    def display_list(self):
        job = self.manager.get_screen('main_menu').job_desc.text
        loc = self.manager.get_screen('main_menu').job_locate.text
        
        print(job, loc)




class GitHubJobsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.primary_hue = '500' # 200
        self.theme_cls.theme_style = 'Dark'  # 'Light'
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenuScreen(name='main_menu'))
        screen_manager.add_widget(JobListingsScreen(name='job_listings'))
        return screen_manager

        
GitHubJobsApp().run()