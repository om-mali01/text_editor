# text editor
text = ""
undo_stack = []
redo_stack = []

def insert(new_text):
    global undo_stack, text
    undo_stack.append(new_text)
    text = text + new_text

def undo():
    global undo_stack, redo_stack, text
    if len(undo_stack) > 0:
        redo_stack.append(undo_stack[-1])
        # print(undo_stack[len(undo_stack)-1])
        undo_stack.pop()
        undo_s = " ".join(undo_stack)
        print("text: ", undo_s)
        # print(undo_stack)

def redo():
    global undo_stack, redo_stack, text
    if len(redo_stack) > 0:
        undo_stack.append(redo_stack[-1])
        # n = len(redo_stack)
        # print(n)
        # print(redo_stack[len(redo_stack)-1]
        redo_stack.pop()
        undo_s = " ".join(undo_stack)
        print("text: ", undo_s)

while True:
    command = input("enter the command (insert, undo, redo, exit) : ")
    if command == "insert":
        new_text = input("enter the text: ")
        insert(new_text)
        # print("text ", text)
        undo_s = " ".join(undo_stack)
        print("text: ", undo_s)

    elif command == "undo":
        undo()
        # print("text: ", text)
    elif command == "redo":
        redo()
        # print("text: ", text)
    elif command == "exit":
        break
    else:
        print("please enter valid command !")
