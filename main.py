import kivy
import mysql.connector
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.accordion import Accordion, AccordionItem

class AccordionApp(App):
    def build(self):
        root = Accordion()
        for x in range(2):
            item = AccordionItem(title='Title %d' % x)
            #item.add_widget(Label(text='Very big content\n' * 10))
            root.add_widget(item)
        return root

class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="uejn_servER8",
          database="uejn_afigestion"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM personas limit 5")

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

        self.vaciar = Button(text="Resetear", font_size=40)
        self.vaciar.bind(on_press=self.vaciar_inputs)
        self.add_widget(self.vaciar)
        
        self.submit = Button(text="Enviar datos", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        myresult = mycursor.fetchall()
        for x in myresult:
          # el 7 es el nombre de la persona
          self.inside.add_widget(Label(text=x[7]))
          print(x[7])


    def invalidForm():
            pop = Popup(title='Invalid Form',
      content=Label(text='Please fill in all inputs with valid information.'),
      size_hint=(None, None), size=(400, 400))

            pop.open()

    def vaciar_inputs(self, text_inputs):
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""
        self.edad.text = ""
        self.razon_social.text = ""

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        edad = self.edad.text
        resultadoEdad = edad.isdigit()
        if resultadoEdad == False:
            #no lo puedo hacer andar desde una funcion como por ejemplo invalidForm()
            pop = Popup(title='Invalid Form',
                content=Label(text='La edad es vacia o no tiene formato numerico.'),
                size_hint=(None, None), size=(400, 400))

            pop.open()

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="uejn_servER8",
          database="uejn_afigestion"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO personas (nombre, domicilio) VALUES (%s, %s)"
        val = (name, email)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

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
    AccordionApp().run()