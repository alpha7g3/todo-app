FILEPATH = "todos.txt"

def get_todos(filepath= FILEPATH):
    """ Read a text file and return the
         list of the to-do item
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath= FILEPATH):
    """
    write the to-do items list in the text files.
    """
    with open(filepath, 'w') as files:
        files.writelines(todos_arg)


