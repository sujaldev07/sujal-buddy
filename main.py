from pynput import mouse, keyboard
import time
import random
import subprocess
from winotify import Notification

last_activity = time.time()

notified_10 = False
notified_30 = False
notified_60 = False

messages_10 = [
    "Oye Sujal, coding ruk gayi kya?",
    "Bhai, kahaan gayab ho gaye?",
    "Hello programmer sahab, wapas aa jao!"
]

messages_30 = [
    "Bhai 30 second ho gaye, wapas aa jao!",
    "Code tera wait kar raha hai!",
    "Itna bada break kyun bhai?"
]

messages_60 = [
    "Bhai zinda ho?",
    "Sujal, coding chhod di kya?",
    "Ek minute ho gaya bhai, wapas aa jao!"
]


def speak(message):
    message = message.replace(",", ", ...")
    message = message.replace(".", "... ")
    message = message.replace("?", "? ...")
    message = message.replace("!", "! ...")

    powershell_code = f'''
Add-Type -AssemblyName System.Speech
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.Rate = 0
$speaker.Volume = 100
$speaker.Speak({message!r})
$speaker.Dispose()
'''

    subprocess.Popen([
        "powershell",
        "-NoProfile",
        "-Command",
        powershell_code
    ])


def activity():
    global last_activity
    global notified_10, notified_30, notified_60

    last_activity = time.time()

    notified_10 = False
    notified_30 = False
    notified_60 = False

    print("Activity detected")


def on_move(x, y):
    activity()


def on_press(key):
    activity()


def check_inactivity():
    global notified_10, notified_30, notified_60

    elapsed = time.time() - last_activity

    if elapsed >= 60 and not notified_60:

        message = random.choice(messages_60)

        print("Inactive for 60 seconds!")
        print("Voice message:", message)

        speak(message)

        toast = Notification(
            app_id="Sujal Buddy",
            title="Sujal Buddy",
            msg=message
        )

        toast.show()

        notified_60 = True

    elif elapsed >= 30 and not notified_30:

        message = random.choice(messages_30)

        print("Inactive for 30 seconds!")
        print("Voice message:", message)

        speak(message)

        toast = Notification(
            app_id="Sujal Buddy",
            title="Sujal Buddy",
            msg=message
        )

        toast.show()

        notified_30 = True

    elif elapsed >= 10 and not notified_10:

        message = random.choice(messages_10)

        print("Inactive for 10 seconds!")
        print("Voice message:", message)

        speak(message)

        toast = Notification(
            app_id="Sujal Buddy",
            title="Sujal Buddy",
            msg=message
        )

        toast.show()

        notified_10 = True


mouse_listener = mouse.Listener(
    on_move=on_move
)

keyboard_listener = keyboard.Listener(
    on_press=on_press
)

mouse_listener.start()
keyboard_listener.start()


while True:
    check_inactivity()
    time.sleep(1)