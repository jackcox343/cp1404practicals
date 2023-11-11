"""
Dynamic labels
Estimate: 60 mins
Actual: 60 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabel(App):
    """Dynamic labeling class"""
    def __init__(self, **kwargs):
        """This function constructs main app"""
        super().__init__(**kwargs)
        self.names = ["Jack", "John", "Alice", "Jennifer"]

    def build(self):
        """This function loads file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.add_labels(self.names)
        return self.root

    def add_labels(self, names):
        """This function adds names to labels"""
        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabel().run()
