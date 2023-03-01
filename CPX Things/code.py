# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import usb_hid
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    if cpx.button_a:
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        # kbd.send(Keycode.ENTER)  # Type capital 'A'
        while cpx.button_a:  # Wait for button to be released
            pass

    if cpx.button_b:
        kbd.press(Keycode.CONTROL, Keycode.ALT)
        kbd.send(Keycode.T)
        kbd.release_all()
        time.sleep(1)
        layout.write("cd lovebits\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        time.sleep(1)
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        layout.write("python main.py\n")
        while cpx.button_b:
            pass
