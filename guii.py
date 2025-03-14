import Functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter to-do",key="todo")
add_button =sg.Button("Add")
list_box = sg.Listbox(values=Functions.get_todos(),key='todos',
                       enable_events=True, size=[45, 12])
edit_button = sg.Button("Edit")

window= sg.Window('My TO-DO App',
                  layout=[[label],
                          [input_box, add_button,],
                          [list_box,edit_button]],
                  font=('Helvetica', 20))
while True:
    event, values =window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos= Functions.get_todos()
            new_todo= values['todo'] + '\n'
            todos.append(new_todo)
            Functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = Functions.get_todos()
            index= todos.index(todo_to_edit)
            todos[index]= new_todo
            Functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()