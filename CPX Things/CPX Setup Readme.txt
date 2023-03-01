   ____   ___   ____     ____   _   _   ___   _____   ____   __   __
  / ___| |_ _| |  _ \   / ___| | | | | |_ _| |_   _| |  _ \  \ \ / /
 | |      | |  | |_) | | |     | | | |  | |    | |   | |_) |  \ V / 
 | |___   | |  |  _ <  | |___  | |_| |  | |    | |   |  __/    | |  
  \____| |___| |_| \_\  \____|  \___/  |___|   |_|   |_|       |_|  

How to set up a CPX for use with Lovebits:

1. Install CircuitPython on a CPX:
	Follow this guide to install: https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
	The install .uf2 is included in the repo but you can also download it from here: https://circuitpython.org/board/circuitplayground_express/
	NOTE: I did these setup steps on my macbook pro, not on the rpi.

2. After the install is complete you should see code.py in the CDX's memory when you access it as a USB device

3. Replace it with the code.py file in the repository.

4. It is ready! Disconnect your CPX from your computer. When plugged into the rpi via usb, pressing the CPX B button will enter the necessary key commands to:
	- open the command line
	- navigate to the lovebits directory
	- type "python main.py" followed by the enter key ~20 times
	- TODO: minimize the terminal
	- This will queue "python main.py" commands which will be immediately exectued after the previous instance of the script ends or crashes.
	
