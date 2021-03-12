from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, ImageLeftWidget
import json

class MyItem(TwoLineAvatarIconListItem):
    def __init__(self, name, state, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = name
        self.secondary_text = state
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{state}.png")
        self.add_widget(self.image)

class Person(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        self.persons_list = self.load_json();
        for person in self.persons_list:
            list.add_widget(MyItem(name=person['name'], state=person['state']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)

    def load_json(self):
        with open('persons.json', encoding='utf-8') as f:
            return json.load(f)    