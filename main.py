
import kivymd
from helpers import username_helper, list_helper

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarIconListItem,MDList
from kivymd.uix.list import IconLeftWidget, ImageRightWidget
from kivymd.uix.scrollview import MDScrollView

class LoginScreen(MDGridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(MDLabel(text='Username',
                                theme_text_color='Custom',
                                text_color=(1, 0, 1, 1),
                                halign="center", font_style='H4')
                        )
        self.username = MDTextField(text = 'Enter username',
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    multiline=False)
        self.add_widget(self.username)
        self.add_widget(MDLabel(text='Password',
                                theme_text_color='Custom',
                                text_color=(1, 0, 0, 1),
                                halign="center", font_style='H4')
                        )
        self.password = MDTextField(password=True, multiline=False)
        self.add_widget(self.password)

class Signup(MDApp):
    def build(self):
        screen = MDScreen()
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(MDRectangleFlatButton(text='Sign up',
                                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                                on_release= self.show_data))
        return screen

    def show_data(self, obj):
        if self.username.text == '':
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + "does not exist"
        close_button = MDFlatButton(text='Close', on_release =  self.close_dialog )
        more_button = MDFlatButton(text='More')
        self.name_dialog = MDDialog(title="Username Check", text=check_string,
                               buttons=[close_button, more_button],)
        self.name_dialog.open()

    def close_dialog(self, obj):
        self.name_dialog.dismiss()


class Calender(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue" # You can change this color check online for the compatible ones
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        btn_flat = MDRectangleFlatButton(text='Click me', pos_hint={'center_x': 0.5, 'center_y': 0.5}) #this is the position
        icon_btn = MDFloatingActionButton(icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.5}) # check compatible icons online
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        return screen






class TodoList(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # You can change this color check online for the compatible ones
        self.theme_cls.primary_hue = "400"
        # self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        list_view = MDList()
        scroll = MDScrollView()
        scroll.add_widget(list_view)
        for i in range(10):
            icon = IconLeftWidget(icon='android')
            list_view.add_widget(OneLineListItem(text="item " + str(i)))
            list_view.add_widget(TwoLineListItem(text="item " + str(i), secondary_text= "item " + str(i) + " with secondary text"))
            threeline_item = ThreeLineAvatarIconListItem(
                text="item " + str(i),
                secondary_text="item " + str(i) + " with secondary text",
                tertiary_text="item " + str(i) + " and tertiary text"
            )
            image_right = ImageRightWidget(source="minimalist-geometry-glowing-circle-square-desktop-wallpaper.jpg")
            icon = IconLeftWidget(icon='android')
            threeline_item.add_widget(image_right)
            list_view.add_widget(threeline_item)

        item1 = OneLineListItem(text='item 1')
        item2 = OneLineListItem(text='item 2')
        list_view.add_widget(item1)
        list_view.add_widget(item2)
        screen.add_widget(scroll)

        return screen






class TodoSpy(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    TodoList().run()





