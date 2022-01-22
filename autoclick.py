import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 240.00
button = Button.left
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
click_thread.start_clicking()

def on_press(key):
    if key == exit_key:
    	click_thread.exit()
        print("bye...")
        listener.stop()    

with Listener(on_press=on_press) as listener:
    listener.join()
