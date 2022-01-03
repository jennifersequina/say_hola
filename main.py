
KIVY_NO_ARGS=1
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHola(App):
    def build(self):
        self._app_window = GridLayout()
        self._app_window.cols = 1
        self._app_window.size_hint = (0.6, 0.7)
        self._app_window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self._app_window.add_widget(Image(source="sayhola.png"))
        self.greeting = Label(
                        text="What's your name?",
                        font_size=34,
                        italic=True,
                        color="#FFAD7B")
        self._app_window.add_widget(self.greeting)
        self.user = TextInput(
                    multiline=False,
                    padding_y=(20,20),
                    size_hint=(0.4, 0.3),
                    halign="center")
        self._app_window.add_widget(self.user)
        self.button = Button(
                    text="GREET",
                    size_hint=(0.4, 0.3),
                    bold=True,
                    background_color="FFAD7B",
                    background_normal="")
        self.button.bind(on_press=self.callback)
        self._app_window.add_widget(self.button)

        return self._app_window

    def callback(self, instance):
        self.greeting.text = "Hola, " + self.user.text + "!"

if __name__ == "__main__":
    SayHola().run()
