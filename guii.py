import Functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter to-do")
add_button =sg.Button("Add")
edit_button = sg.Button("Edit")

window= sg.Window('My TO-DO App', layout=[[label],[input_box, add_button,]])
window.read()
window.close()