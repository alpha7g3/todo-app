from Functions import get_todos, write_todos


import time

now = time.strftime("%b %d ,%Y %H:%M:%S")
print("It is", now)
while True:
    user_action= input("Type add,show,edit,complete or exist:")
    user_action= user_action.strip()



    if   user_action.startswith("add"):
      todo = user_action[4:]

      todos =get_todos()

      todos.append(todo + '\n')
      write_todos(todos)



    elif user_action.startswith("show"):


          todos= get_todos()

          for index,item in enumerate(todos):
               item = item.strip('\n')
               see= f"{index+1}-{item}"
               print(see)
    elif user_action.startswith("edit") :
        try:
           number=int(user_action[5:])
           print(number)

           number= number - 1

           todos= get_todos()

           new_todo =input("enter the new todo :")
           todos[number]=new_todo + "\n"

           write_todos(todos)

        except ValueError:
            print("your command is invalid")
            continue



    elif   user_action.startswith("complete"):
        try:
            number=int (user_action[9:])

            todos= get_todos()

            index= number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo  {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("out of range ")
            continue

    elif   user_action.startswith("exist") :
     break
    else :
        print("command is not valid")
print("have a nice day")
