# Sujal Buddy

A small Windows app written in Python that notices when you stop using your keyboard and mouse, and then reminds you to get back to work, with a desktop notification and a spoken message.

## What it does

- Watches keyboard and mouse activity in the background (using `pynput`)
- If there is no activity for 10, 30 and 60 seconds, it picks a random message for that level
- Shows the message as a Windows toast notification (using `winotify`)
- Speaks the message aloud using Windows speech through PowerShell
- Any keyboard or mouse activity resets the timers

The 10 / 30 / 60 second limits are test values. The plan is to change them to longer reminders (around 30 minutes) later.

## Requirements

- Windows
- Python 3
- Libraries: `pynput`, `winotify`

## How to run

1. Install the libraries:

   ```
   pip install -r requirements.txt
   ```

2. Run the app:

   ```
   python main.py
   ```

3. Stop using the keyboard and mouse for 10 seconds to see the first reminder. Press `Ctrl + C` in the terminal to stop it.

## Files

- `main.py` - the main app

## Ideas for the future

- Change the intervals to about 30 minutes
- Start automatically with Windows
- Make it into an `.exe`
- Handle the laptop waking up from sleep properly

## Author

Sujal Kumar - [github.com/sujaldev07](https://github.com/sujaldev07)
