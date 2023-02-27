import os
import time
import RPi.GPIO as GPIO
import vlc
import recorder
from constants import *


# ***CONFIGURATIONS
class Config:
    is_running = True
    media_player = vlc.MediaPlayer()
    pins_to_buttons = {
        BUTTON_1: 5,
        BUTTON_2: 6,
        BUTTON_3: 13,
        BUTTON_4: 19,
        BUTTON_5: 26,
        BUTTON_6: 16,
        BUTTON_7: 20
    }
    buttons_to_files = {
        BUTTON_1: FILE_NAME + "_1",
        BUTTON_2: FILE_NAME + "_2",
        BUTTON_3: FILE_NAME + "_3",
        BUTTON_4: FILE_NAME + "_4",
        BUTTON_5: FILE_NAME + "_5",
        BUTTON_6: FILE_NAME + "_6",
        BUTTON_7: FILE_NAME + "_7",
    }
# ***END CONFIGURATIONS


##
# Main function to run the program
##
def run():
    print("Booting up Lovebits...")
    init_program()   
    print("Awaiting input...")
    while Config.is_running:
        True
    print("Program halted. Shutting down.")

##
# Gets called at program startup, initializing 
# all configurations
##
def init_program():
    # Setup the button pins as inputs with a pull-up resistor
    GPIO.setmode(GPIO.BCM)
    # Button 1
    GPIO.setup(Config.pins_to_buttons[BUTTON_1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(Config.pins_to_buttons[BUTTON_1], GPIO.FALLING, callback=lambda x: button_command(BUTTON_1))
    # Button 2
    GPIO.setup(Config.pins_to_buttons[BUTTON_2], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(Config.pins_to_buttons[BUTTON_2], GPIO.FALLING, callback=lambda x: button_command(BUTTON_2))


##
# Runs upon a button action/press. Two possible actions exist:
# 1. If a file for the button exists, its recorded video will play
# 2. If a file for the button does not exist, a recording for it
#    will begin and be saved to it
##
def button_command(button_name):
    file_name = Config.buttons_to_files[button_name]
    local_path = os.getcwd()
    # 1. File exists? Play video
    if os.path.exists(str(local_path) + "/" + file_name + ".avi"):
        play_video(file_name + ".avi")
    else:
        record_video(file_name, RECORD_TIME_SECONDS)


##
# Records video for the specified file name and recording time.
##
def record_video(file_name, record_time):
    # Validate recording time is acceptable
    if record_time < 10:
        print("Invalid recording time provided. Please provide a time equal or longer than 10 seconds.")
    
    # This line sets up the file names for the temp
    # files and the main file where both the audio
    # and image will be saved
    recorder.file_manager(file_name)

    # recording begins
    recorder.start_AVrecording(file_name)
    # recording will be uninterrupted for the 
    # specified amount of time
    time.sleep(record_time)
    # After the timer is done, the recording is
    # stopped and the files are saved
    recorder.stop_AVrecording(file_name)
    print("Recording completed")
    
    # After a recording, we shut down the program due to potential threading issues
    Config.is_running = False



##
# Plays a video with the vlc media player for
# the specified file name
##
def play_video(file_name):
    media = vlc.Media(file_name)
    Config.media_player.set_media(media)
    Config.media_player.play()
    time.sleep(10)
    Config.media_player.release()


##
# Function that generates the file name that is saved,
# using number values 1 to 8
##
def create_file_name(file_name):
    for i in range(1, 9):
        new_file_name = "{file_name}_{i}".format(file_name=file_name, i=i)
        local_path = os.getcwd()
        if os.path.exists(str(local_path) + "/" + new_file_name + ".avi"):
            continue
        else:
            return new_file_name
    return None


if __name__ == "__main__":
    init_program()
    # hardcoded for testing
    #record_video("something", 10)
    button_command(BUTTON_1)