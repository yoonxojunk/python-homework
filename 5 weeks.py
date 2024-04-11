def get_welcome_message(name):
    msg1 = f"Hello {name},"
    msg2 = "Welcome to seoul."
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    box_line = '-' * (nstr + 2) 
    message = [box_line,msg1.ljust(nstr),msg2.ljust(nstr), box_line]
    return '\n'.join(message)
name = input("Input his/her name: ")

welcome_message = get_welcome_message(name)

print(welcome_message)
