# Program Title: Dragpy (KIVY Ver)
# Created By: Rile_Cry
# Created On: 23 July 2019
# Current Version: 1.1.0
# Description: A smoother, much easier representation of the earlier dragypy
# program. With a visual gui to work with, the entire process can be editable.

# Imports

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel


# Classes

class Test(TabbedPanel):
    # This tab is built in the dragpy.kv file
    pass

class DragpyApp(App):
    # Call the build function
    def build(self):
        # Return our test widget
        return Test()

# Run Condition

if __name__ == '__main__':
    # Run the App
    DragpyApp().run()
