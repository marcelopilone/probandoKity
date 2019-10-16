import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup


class MyGrid(GridLayout):

	

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Nombre: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Apellido: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Edad: "))
        self.edad = TextInput(multiline=False)
        self.inside.add_widget(self.edad)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    def show_popup():
        show = P() # Create a new instance of the P class 

        popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400)) 
        # Create the popup window

        popupWindow.open() # show the popup


    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        edad = self.edad.text
        resultadoEdad = edad.isdigit()
        if resultadoEdad == False:
        	print('No ingreso un numero')
        self.show_popup

        print("Name:", name, "Last Name:", last, "Email:", email, "Edad:", edad)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""
        self.edad.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()