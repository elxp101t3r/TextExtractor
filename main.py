from tkinter.filedialog import askopenfile
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
    def extract_text(self, event):
        pass
    
    
    def fileChooser(self, event):
        self.file = askopenfile(mode='r', filetypes=[('png files', '*.png')])
        self.image_file = self.file.name
        
        self.locationLabel.text = self.image_file
        self.locationLabel.pos_hint = {'center_x': .5, 'center_y': .2}
        self.extract_text_button.disabled = False
        self.choose_button.disabled = True
    
   
    
    def build(self):
        
        self.layout = MDRelativeLayout(md_bg_color=[27/255, 30/255, 36/255])
        
        self.imageText = TextInput(
            text='', pos_hint = {'center_x':0.5, 'center_y':.62},
            size_hint=(None, None), 
            height=340,
            width=480,
            font_size=25,
            foreground_color = (190, 196, 207),
            background_color=(8/255, 75/255, 209/255)
        )
        
        self.choose_button = Button(text='Select', pos_hint= {'center_x': .4,'center_y': 0.07},
        size_hint = (.2, .1),
        font_size=24,
        background_color=(0, 1, 0),
        disabled=False,
        on_press = self.fileChooser
        )
        
        self.extract_text_button = Button(text='Extract', pos_hint= {'center_x': .65,'center_y': 0.07},
        size_hint = (.2, .1),
        font_size=24,
        background_color=(0, 1, 0),
        disabled=True,
        on_press = self.extract_text
        )
        
        self.locationLabel = Label(text="",     pos_hint={'center_x': .5, 'center_y': 20},
        size_hint=(1, 1),
        font_size=20,
        color=(0,0,1)
        )
        
        self.layout.add_widget(self.imageText)
        self.layout.add_widget(self.choose_button)
        self.layout.add_widget(self.extract_text_button)
        self.layout.add_widget(self.locationLabel)
        
        return self.layout


if __name__ == "__main__":
    ExtractingTextApp().run()
    