from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Tela(BoxLayout):
    lbl_default_size = '16pt'


class MyApp(App):
    def build(self):
        self.title = "MyBuyList"
        return Tela()


if __name__ == "__main__":
    MyApp().run()
