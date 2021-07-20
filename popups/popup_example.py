from dearpygui.core import *
from dearpygui.simple import *

with window("Tutorial"):

    add_button("Add Printer")

    with popup("Add Printer", "Popup ID", mousebutton=mvMouseButton_Left):
        add_text("A popup")
        add_input_text("enter data", label="")

start_dearpygui()