from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.popup import Popup


class MainApp(MDApp):
    def build(self):
        self.title = 'My Kivy Apk'


class Screenmanager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        Home.B1.text = str(self.ids.p1.text).upper()
        Home.B2.text = str(self.ids.p2.text).upper()


class Start(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass


class Home(BoxLayout):
    s = dp(400)
    max_s = 840
    B1 = Button(
        size_hint=(None, 1),
        background_color="red",
        text="Red",
        width=s,
    )
    B2 = Button(

        size_hint=(None, 1),
        background_color="blue",
        text="Blue",
        width=s,

    )
    popup1 = Popup(title=f"{B2.text} WINS")
    popup2 = Popup(title=f" {B1.text} WINS")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background_color = "blue"

        def BTN1(self):
            self.width += 4
            print(self.text)
            if self.width > Home.max_s:
                Home.popup2.open()
            elif self.width > Home.max_s:
                Home.popup1.open()
                print(self.text)

        def BTN2(self):
            self.width += 4
            Home.B1.width -= 4
            print(Home.B1.width)

        self.add_widget(self.B1)
        self.add_widget(self.B2)
        self.B1.bind(on_release=BTN1)
        self.B2.bind(on_release=BTN2)


if __name__ == '__main__':
    MainApp().run()
