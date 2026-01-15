FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# if you run it from the function it will execute it.
# if you run from the main it is NOT going to execute it.
# this method helps to NOT execute from the main
if __name__ == "__main__":
    print("Hello from functions")