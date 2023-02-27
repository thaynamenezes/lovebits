# Lovebits Project

## Setup

The following prerequisites are needed for running this
on the Raspberry Pi 400.

Run these commands from your terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install portaudio19-dev
```

Finally, this longer command as well:

```bash
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
```

Use Pip (Python package manager) for the following:

```bash
sudo pip install pyaudio
sudo pip install opencv-python==4.5.3.56
sudo pip install python-vlc
```

## Getting Started

To run the program, have your terminal open to the directory of the project and run the command:

```bash
python main.py
```

## Important Information

```main.py``` is where the main logic we need to work on will live.

Do NOT TOUCH ```recorder.py```, which contains all of the recording logic for both audio and video, and merging them both together.