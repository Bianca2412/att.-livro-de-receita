from kivy.app import App
from kivy.core.window import Window
class Estudo1App(App):
    def build(self):
            Window.clearcolor=(1,1,1,1)
    pass
janela = Estudo1App()
janela.run()