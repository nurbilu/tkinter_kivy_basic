from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class GarageApp(App):
    def build(self):
        self.garage = {}  # Dictionary to store cars in the garage
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Text input for entering car details
        self.car_input = TextInput(hint_text='Enter Car Details (e.g., Make Model)', multiline=False)
        self.layout.add_widget(self.car_input)

        # Button to add/update a car to/in the garage
        btn_add_update_car = Button(text='Add/Update Car', on_press=self.add_update_car)
        self.layout.add_widget(btn_add_update_car)

        # Button to view all cars in the garage
        btn_view_cars = Button(text='View Cars', on_press=self.view_cars)
        self.layout.add_widget(btn_view_cars)

        # Button to reset the displayed list of cars
        btn_reset_cars = Button(text='Reset Cars', on_press=self.reset_cars)
        self.layout.add_widget(btn_reset_cars)

        # Text input for deleting a car
        self.delete_input = TextInput(hint_text='Enter Car Details to Delete', multiline=False)
        self.layout.add_widget(self.delete_input)

        # Button to delete a car from the garage
        btn_delete_car = Button(text='Delete Car', on_press=self.delete_car)
        self.layout.add_widget(btn_delete_car)

        return self.layout

    def add_update_car(self, instance):
        car_details = self.car_input.text
        if car_details:
            # Check if the car is already in the garage
            if car_details in self.garage:
                # If the car is already in the garage, update its details
                self.garage[car_details] = True
            else:
                # If the car is not in the garage, add it
                self.garage[car_details] = True

            self.car_input.text = ''  # Clear the text input after adding/updating a car

    def view_cars(self, instance):
        self.layout.add_widget(Label(text='Cars in the Garage:'))
        for car in self.garage.keys():
            self.layout.add_widget(Label(text=car))

    def reset_cars(self, instance):
        # Remove all displayed labels (reset the view)
        for widget in self.layout.children[:]:
            if isinstance(widget, Label) and widget.text.startswith('Cars in the Garage:'):
                self.layout.remove_widget(widget)

    def delete_car(self, instance):
        car_details = self.delete_input.text
        if car_details in self.garage:
            del self.garage[car_details]
            self.delete_input.text = ''  # Clear the text input after deleting a car


if __name__ == '__main__':
    GarageApp().run()
