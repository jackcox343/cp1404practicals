"""
Box layout demo
Estimate time: 30 mins
Actual time: 30 mins
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """This is the class for a boxlayout demo app"""

    def build(self):
        """This function load file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """This function handles greets"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """This function handles clearing of text"""
        print("test")
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
