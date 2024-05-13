from logging import root
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Telalogin(Screen):
    def __init__(self, **kwargs):
        super(Telalogin, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.add_widget(layout)

        layout.add_widget(AsyncImage(source='https://i.pinimg.com/originals/03/05/05/030505f3035f56d855ae73838dbc77c8.jpg'))
        layout.add_widget(Label(text="SEJA BEM-VINDO!", color=(0, 0, 0.2, 1), bold=True, font_size=26))
        layout.add_widget(Label(text="Livro de Receita - Doces", color=(0, 0, 0.2, 1), bold=True, font_size=26))
        layout.add_widget(Label(text="Receitas Disponíveis", color=(0, 0, 0.2, 1), bold=True, font_size=23))
        
        botao_layout = BoxLayout(padding=10)
        layout.add_widget(botao_layout)

        self.receita_brownie = Button(text="Brownie", background_color=(1, 0, 0, 1))
        self.receita_brownie.bind(on_press=self.mudar_para_tela_brownie)
        botao_layout.add_widget(self.receita_brownie)

        self.receita_palha_italiana = Button(text="Palha Italiana", background_color=(1, 0, 0, 1))
        self.receita_palha_italiana.bind(on_press=self.mudar_para_tela_palha_italiana)
        botao_layout.add_widget(self.receita_palha_italiana)

        self.receita_pave = Button(text="Pavê", background_color=(1, 0, 0, 1))
        self.receita_pave.bind(on_press=self.mudar_para_tela_pave)
        botao_layout.add_widget(self.receita_pave)

        self.receita_pudim = Button(text="Pudim", background_color=(1, 0, 0, 1))
        self.receita_pudim.bind(on_press=self.mudar_para_tela_pudim)
        botao_layout.add_widget(self.receita_pudim)

    def mudar_para_tela_brownie(self, instance):
        app = App.get_running_app()
        app.root.current = 'tela_brownie'


    def mudar_para_tela_palha_italiana(self, instance):
        app = App.get_running_app()
        app.root.current = 'tela_palha_italiana'

    def mudar_para_tela_pave(self, instance):
        app = App.get_running_app()
        app.root.current = 'tela_pave'

    def mudar_para_tela_pudim(self, instance):
        app = App.get_running_app()
        app.root.current = 'tela_pudim'


class TelaBrownie(Screen):
    def __init__(self, **kwargs):
        super(TelaBrownie, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Detalhes do Brownie", font_size=24))
                          
        self.add_widget(layout)

class TelaPalhaItaliana(Screen):
    def __init__(self, **kwargs):
        super(TelaPalhaItaliana, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Detalhes da Palha Italiana", font_size=24))
        self.add_widget(layout)

class TelaPave(Screen):
    def __init__(self, **kwargs):
        super(TelaPave, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Detalhes do Pavê", font_size=24))
        self.add_widget(layout)

class TelaPudim(Screen):
    def __init__(self, **kwargs):
        super(TelaPudim, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Detalhes do Pudim", font_size=24))
        self.add_widget(layout)

class GerenciadordeTelas(ScreenManager):
    pass
    

class Umatela(App):
    def build(self):
        Window.clearcolor = (1,0.498,0.498,1)
        self.root = GerenciadordeTelas()
        self.root.add_widget(Telalogin(name='tela_login'))
        self.root.add_widget(TelaBrownie(name='tela_brownie'))
        self.root.add_widget(TelaPalhaItaliana(name='tela_palha_italiana'))
        self.root.add_widget(TelaPave(name='tela_pave'))
        self.root.add_widget(TelaPudim(name='tela_pudim'))
        return self.root

if __name__ == '__main__':
    Umatela().run()