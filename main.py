# app and screen manager
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager


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


# gitHub Jobs
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


class MenuScreen(Screen):
    job_desc = ObjectProperty(None)
    job_locate = ObjectProperty(None)

    def show_data(self):
        # print(self.job_desc.text)
        # print(self.job_locate.text)
        print(f'https://jobs.github.com/positions.json?description={self.job_desc.text}&location={self.job_locate.text}')



class GitHubJobsApp(MDApp):
           
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '500' # 200
        self.theme_cls.theme_style = 'Dark'  # 'Light'
        return MenuScreen()

        
GitHubJobsApp().run()