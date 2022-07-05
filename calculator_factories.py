
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Tela(FloatLayout):
    pass


class Layout1(BoxLayout):
    def limpar(self):
        self.ids.caixa_entrada.text = '0'

    def valor_botao(self, valor):
        val = self.ids.caixa_entrada.text

        if val == '0':
            self.ids.caixa_entrada.text = ''
            self.ids.caixa_entrada.text = f'{valor}'
        else:
            self.ids.caixa_entrada.text = f'{val}{valor}'

    def operadores(self, operador):
        val = self.ids.caixa_entrada.text
        self.ids.caixa_entrada.text = f'{val}{operador}'

    def resultado(self):
        val = self.ids.caixa_entrada.text
        res = eval(val)
        self.ids.caixa_entrada.text = f'{res}'


class Layout2(GridLayout):
    pass


class CalculatorApp(MDApp):
    def build(self):
        self.title = 'Calculadora'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('main.kv')


CalculatorApp().run()
