#!/usr/bin/env python3
import subprocess
import sys

# save current active window
subprocess.Popen(["/bin/sh", "-c", "xdotool getactivewindow key 'ctrl+s'"])

# Get the active window's name (window in focus)
name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode("utf-8").strip()

# remove the text that comes after the filename in sublime text
if name.endswith(' - Sublime Text 2 (UNREGISTERED)'):
	fname = name[:-len(' - Sublime Text 2 (UNREGISTERED)')]

# remove tilde and replace with home path (the ~ throws off everything for some reason)
fname = fname[1:]
fname = "$HOME" + fname

# return the current open file in sublime
command = "echo "+'"'+ fname +'"'

subprocess.Popen(["/bin/sh", "-c", command])

