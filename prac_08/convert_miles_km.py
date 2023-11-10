"""
Convert miles program
Estimate: 60 mins
Actual: 60 mins
"""
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934


class ConvertMilesApp(App):
    """This a class for miles conversion app"""

    def build(self):
        """This function builds loaded file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """This function handles miles to km calculation"""
        value = self.get_valid_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """This function gets valid input"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        """This function handles incrementing for button press"""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


ConvertMilesApp().run()
