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
        try:
            path = filechooser.open_file(on_selection = self.selected)
            print(path)
            if path:
                save_path = self.save_file()
                self.convert(path, save_path)
        except IndexError:
            return

    def save_file(self):
        from plyer import filechooser
        try:
            save_path = (filechooser.save_file(on_selection = self.selected))
            save_path[0] += '.pdf'
            return save_path
        except IndexError:
            return

    def selected(self, selection):
        try:
            path = selection[0]
            return path
        except IndexError:
            return

    def cancel():
        pass

    def merge():
        pass

    #TODO: refactor IndexError handling

    def convert(self,path, save_path):
        image = Image.open(path[0])
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(str(save_path[0]), 'wb')
        file.write(pdf_bytes)
        image.close()
        file.close()

    def split():
        pass

if __name__ == "__main__":
    MainApp().run()
