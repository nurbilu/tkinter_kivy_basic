from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random
from datetime import datetime

class HelloApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Button to show "Hello"
        btn_hello = Button(text="Show Hello")
        btn_hello.bind(on_press=self.show_hello)
        self.layout.add_widget(btn_hello)

        # Button to show current date
        btn_date = Button(text="Show Current Date")
        btn_date.bind(on_press=self.show_current_date)
        self.layout.add_widget(btn_date)

        # Button to change random theme color
        btn_change_color = Button(text="Change Random Theme Color")
        btn_change_color.bind(on_press=self.change_theme_color)
        self.layout.add_widget(btn_change_color)

        return self.layout

    def show_hello(self, instance):
        hello_label = Label(text="Hello")
        self.layout.add_widget(hello_label)

    def show_current_date(self, instance):
        now = datetime.now()
        date_label = Label(text=f"Current Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        self.layout.add_widget(date_label)

    def change_theme_color(self, instance):
        # Generate a random color
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        # Change the theme color
        Window.clearcolor = get_color_from_hex(random_color)

if __name__ == '__main__':
    HelloApp().run()

