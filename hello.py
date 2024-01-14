from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import sqlite3

class GarageCRUDApp(App):

    def build(self):
        self.db_conn = sqlite3.connect("garage.db")
        self.create_table()
        return self.create_ui()

    def create_table(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                color TEXT,
                year INTEGER
            )
        ''')
        self.db_conn.commit()

    def create_ui(self):
        layout = BoxLayout(orientation='vertical')
        self.data_layout = GridLayout(cols=5, spacing=10)

        # Input fields
        self.model_input = TextInput(hint_text='Model')
        self.color_input = TextInput(hint_text='Color')
        self.year_input = TextInput(hint_text='Year')

        # Buttons
        add_button = Button(text='Add Car', on_press=self.add_car)
        show_button = Button(text='Show Cars', on_press=self.show_cars)

        # Add widgets to layout
        layout.add_widget(self.model_input)
        layout.add_widget(self.color_input)
        layout.add_widget(self.year_input)
        layout.add_widget(add_button)
        layout.add_widget(show_button)
        layout.add_widget(self.data_layout)

        return layout
    
    def add_car(self, instance):
        model = self.model_input.text
        color = self.color_input.text
        year = self.year_input.text

        if model and color and year:
            cursor = self.db_conn.cursor()
            cursor.execute("INSERT INTO cars (model, color, year) VALUES (?, ?, ?)", (model, color, int(year)))
            self.db_conn.commit()
            self.clear_inputs()
            print("Car added successfully.")
        else:
            print("Please fill in all fields.")

    def show_cars(self, instance):
        self.data_layout.clear_widgets()
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()

        for car in cars:
            self.data_layout.add_widget(Label(text=str(car[1])))
            self.data_layout.add_widget(Label(text=str(car[2])))
            self.data_layout.add_widget(Label(text=str(car[3])))
            edit_button = Button(text='Edit', on_press=lambda _, car_data=car: self.edit_car_popup(car_data))
            self.data_layout.add_widget(edit_button)
            delete_button = Button(text='Delete', on_press=lambda _, car_id=car[0]: self.delete_car(car_id))
            self.data_layout.add_widget(delete_button)

    def edit_car_popup(self, car_data):
        edit_popup = Popup(title='Edit Car', size_hint=(None, None), size=(400, 250))
        edit_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Input fields in the popup
        popup_model_input = TextInput(hint_text='Model', text=car_data[1], size_hint_y=None, height=40)
        popup_color_input = TextInput(hint_text='Color', text=car_data[2], size_hint_y=None, height=40)
        popup_year_input = TextInput(hint_text='Year', text=str(car_data[3]), size_hint_y=None, height=40)

        # Update button in the popup
        update_button = Button(text='Update', on_press=lambda _: self.update_car(car_data[0], popup_model_input.text, popup_color_input.text, popup_year_input.text))

        # Add widgets to the popup layout
        edit_layout.add_widget(popup_model_input)
        edit_layout.add_widget(popup_color_input)
        edit_layout.add_widget(popup_year_input)
        edit_layout.add_widget(update_button)

        edit_popup.content = edit_layout
        edit_popup.open()

    def update_car(self, car_id, model, color, year):
        if model and color and year:
            cursor = self.db_conn.cursor()
            cursor.execute("UPDATE cars SET model=?, color=?, year=? WHERE id=?", (model, color, int(year), car_id))
            self.db_conn.commit()
            print("Car updated successfully.")
            self.show_cars(None)
        else:
            print("Please fill in all fields.")

    def delete_car(self, car_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        self.db_conn.commit()
        print("Car deleted successfully.")
        self.show_cars(None)

    def clear_inputs(self):
        self.model_input.text = ''
        self.color_input.text = ''
        self.year_input.text = ''

if __name__ == '__main__':
    GarageCRUDApp().run()



    