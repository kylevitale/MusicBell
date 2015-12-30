# MusicBell
A script to play music at specific times for Mac OS X. Intended to play music
before a (school) class ends and begins.

This is also an exercise in learning git and github workflows, and python.

# Requirements
1. Mac OS X Mavericks, 10.10+, other versions possibly work, too.
2. Music files must be in /usr/local/musicbell and be named 'class_ending.aif'
and 'class_starting.aif'.
3. Terminal Notifier for the Mac OS X notifications.

# Setup
Create the musicbell directory in /usr/local/ and copy the script there. Copy
the launch agent plist into /Library/LaunchAgents and load it. Install Terminal
Notifier.
