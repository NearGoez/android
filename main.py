from kivy.app import App
from kivi.uiz.video import Video
from kivy.uiz.boxlayout import BoxLayout
from kivy.uix.button import Button

class VideoApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical')

        self.video = Video(source='r')

