import keyboard
import time
import threading

key = "alt"
dot_time = 0.1

pressed_time = 0
char_timer = None                   
char_timer_running = False
space_timer = None                   
space_timer_running = False
key_pressed = False
cur_str = ""

def dot_or_dash(t):
    # Returns ".", "-", or " " depending on time length
    global dot_time

    if t < 2 * dot_time:
        return "."
    return "-"

def get_char(str):
    return "a"

def on_space_timer_end():
    keyboard.write(" ")

def on_char_timer_end():
    global cur_str
    for i in range(len(cur_str)):
        keyboard.send("backspace")
    keyboard.write(get_char(cur_str))
    cur_str = ""

def on_key_release(event):
    global pressed_time, char_timer, char_timer_running, space_timer, space_timer_running, key_pressed, cur_str
    key_pressed = False

    char_timer = threading.Timer(dot_time * 4, on_char_timer_end)
    char_timer.start()
    char_timer_running = True
    space_timer = threading.Timer(dot_time * 7, on_space_timer_end)
    space_timer.start()
    space_timer_running = True

    new_char = dot_or_dash(time.time() - pressed_time)
    keyboard.write(new_char)
    cur_str += new_char
    print(cur_str)
    
def on_key_press(event):
    global pressed_time, char_timer, char_timer_running, space_timer, space_timer_running, key_pressed
    if not key_pressed:
        if char_timer_running:
            char_timer.cancel()
        if space_timer_running:
            space_timer.cancel()
        pressed_time = time.time()
        key_pressed = True

def main():
    keyboard.on_release_key(key, on_key_release)
    keyboard.on_press_key(key, on_key_press)
    keyboard.wait("esc")

if __name__ == "__main__":
    main()