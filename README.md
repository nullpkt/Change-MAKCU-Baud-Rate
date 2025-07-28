# Change-MAKCU-Baud-Rate
This is a little tool i threw to change the baud rate from the default 115200 to 4M. I noticed a lot of new people that keep running into issues with their baud rate, so I figured I’d share this in hopes it can help someone out on their journey :)

### How to Use
I've included a precompiled .exe for convenience so you don't need to open CMD and run the script manually and blah blah blah everytime. Just double-click and you're good to go.

### Don't trust random .exe files?
You can run the script manually or you can use pyinstaller to compile the script to an exe your self.

### Commands to run the script manually
``` cmd
# python3 ChangeBaud.py
```

### Commands to compile to exe your self
``` cmd
# pip install pyinstaller
# pyinstaller --onefile --icon=NONE ChangeBaud.py
```
