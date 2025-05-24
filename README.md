# PRODIGY_CS_04
Simple Keylogger Program

What is it

This is a basic keylogger program written in Python using the pynput library. It captures every keystroke made on the keyboard and records them in a text file named keylog.txt along with a timestamp for each key press.

How it works

The program listens for keyboard events and logs each key pressed to keylog.txt. Special keys like Space, Enter, Tab, and Backspace are recorded with descriptive labels (e.g., [SPACE]). The logging starts when the program is run and stops when the Esc key is pressed. Each session appends to the log file, with a header indicating the start time of the session.
