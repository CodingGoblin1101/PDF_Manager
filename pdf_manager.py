from pypdf import PdfReader
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

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

    def convert():
        pass

    def merge():
        pass

    def split():
        pass

if __name__ == "__main__":
    MainApp().run()