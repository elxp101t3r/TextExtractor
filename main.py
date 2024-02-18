from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from PIL import Image
from pytesseract import pytesseract
from kivy.core.window import Window


Window.size= (500, 500)


class ExtractingTextApp(MDApp):
    def build(self):
        self.layout = MDRelativeLayout(md_bg_color=[248/255, 200/255, 220/255])
        
        return self.layout


if __name__ == "__main__":
    ExtractingTextApp().run()