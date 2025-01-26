from pypdf import PdfReader
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
import img2pdf
from PIL import Image
import os

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Midnightblue'
        return Builder.load_file('pdf_manager.kv')
    
class MainScreen(Screen):
    def __init__(self, **kwargs):
	    super().__init__(**kwargs)
    # **kwargs -> belieblig viele Argumente annehmbar, als dictionary wiedergegeben
    # super(). -> ruft die __init__ Methode der Eltern auf, bedeutet Eltern nehmen gleiche Argumente entgegen

    def select_file(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.selected)

    def selected(self, selection):
        print(selection[0])
        path = selection[0]
        return path

    def convert(path):
        img_path = path
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        pdf_path = self.save_file
        ###### Problem: wie den save path hier reinkriegen? Nicht auswählbar weil über save_file function, weil diese function zwingend in
        ###### MainScreen class sein muss, Objekt aber noch nicht existiert weshalb save_file() nicht ausführbar ist.
        file = open(pdf_path, 'wb')
        file.write(pdf_bytes)
        image.close()
        file.close()

    def save_file(self):
        from plyer import filechooser
        filechooser.save_file(on_selection = self.selected)
        #print(selection[0])
        #save_path = "selection[0]"
        #return save_path
        return self

    def cancel():
        pass


    def merge():
        pass

    def split():
        pass

if __name__ == "__main__":
    MainApp().run()
