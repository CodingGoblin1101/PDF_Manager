from pypdf import PdfReader
from pypdf import PdfWriter
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
        path = filechooser.open_file(on_selection = self.selected)
        if path:
            return path

    def save_file(self):
        from plyer import filechooser
        save_path = (filechooser.save_file(on_selection = self.selected))
        if save_path:
            save_path[0] += '.pdf'
            return save_path

    def selected(self, selection):
        if selection:
            path = selection[0]
            return path

    def cancel(self):
        pass

    def merge_pdf(self):
        first_file = self.select_file()
        second_file = self.select_file()

        path_list = [first_file[0], second_file[0]]
        merger = PdfWriter()

        for data in path_list:
                merger.append(data)
        save_path = self.save_file()
        merger.write(save_path[0])
        merger.close()



    def convert(self):
        try:
            path = self.select_file()
            if path:
                image = Image.open(path[0])
                pdf_bytes = img2pdf.convert(image.filename)
                save_path = self.save_file()

                if save_path:
                    file = open(str(save_path[0]), 'wb')
                    file.write(pdf_bytes)
                    image.close()
                    file.close()
        except:
            return
            # add warning window here
    def split(self):
        pass

if __name__ == "__main__":
    MainApp().run()
