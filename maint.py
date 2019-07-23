# Program Title: Dragpy (KIVY Ver)
# Created By: Rile_Cry
# Created On: 23 July 2019
# Current Version: 1.1.1
# Description: A smoother, much easier representation of the earlier dragypy
# program. With a visual gui to work with, the entire process can be editable.

# Imports

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel

# Classes

class Test(TabbedPanel):
    # This tab is built in the dragpy.kv file
    # Then edited with the following code

    def update(self, dt) -> None:
        texty = ObjectProperty()
        texty2 = ObjectProperty()

        self.texty2.text = self.texty.text

class DragpyApp(App):
    # Call the build function
    def build(self) -> 'Widget':
        # Return our test widget
        Testo = Test()
        Clock.schedule_interval(Testo.update, 1/60)
        return Testo

# Run Condition

if __name__ == '__main__':
    # Run the App
    DragpyApp().run()
