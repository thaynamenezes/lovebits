import os
import time
from gpiozero import Button
import vlc
import recorder
from constants import *
import simpleaudio as sa


# ***CONFIGURATIONS
class Config:
    is_pressed = True
    is_running = True
    media_player = vlc.MediaPlayer()
    pins_to_buttons = {
        BUTTON_1: 5,
        BUTTON_2: 6,
        BUTTON_3: 13,
        BUTTON_4: 19,
        BUTTON_5: 26,
        BUTTON_6: 20,
        BUTTON_7: 21
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
    button_1 = None
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
    # Setup the buttons along with their callback functions
    Button.was_held = False

    #Button 1
    button_1 = Button(Config.pins_to_buttons[BUTTON_1], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_1.when_released = lambda x: button_release(BUTTON_1, button_1)
    button_1.when_held = lambda x: button_held(BUTTON_1, button_1)
    recorder.VideoRecorder.num_threads += 1
    #Button 2
    button_2 = Button(Config.pins_to_buttons[BUTTON_2], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_2.when_released = lambda x: button_release(BUTTON_2, button_2)
    button_2.when_held = lambda x: button_held(BUTTON_2, button_2)
    recorder.VideoRecorder.num_threads += 1
    #Button 3
    button_3 = Button(Config.pins_to_buttons[BUTTON_3], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_3.when_released = lambda x: button_release(BUTTON_3, button_3)
    button_3.when_held = lambda x: button_held(BUTTON_3, button_3)
    recorder.VideoRecorder.num_threads += 1
    #Button 4
    button_4 = Button(Config.pins_to_buttons[BUTTON_4], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_4.when_released = lambda x: button_release(BUTTON_4, button_4)
    button_4.when_held = lambda x: button_held(BUTTON_4, button_4)
    recorder.VideoRecorder.num_threads += 1
    #Button 5
    button_5 = Button(Config.pins_to_buttons[BUTTON_5], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_5.when_released = lambda x: button_release(BUTTON_5, button_5)
    button_5.when_held = lambda x: button_held(BUTTON_5, button_5)
    recorder.VideoRecorder.num_threads += 1
    #Button 6
    button_6 = Button(Config.pins_to_buttons[BUTTON_6], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_6.when_released = lambda x: button_release(BUTTON_6, button_6)
    button_6.when_held = lambda x: button_held(BUTTON_6, button_6)
    recorder.VideoRecorder.num_threads += 1
    #Button 7
    button_7 = Button(Config.pins_to_buttons[BUTTON_7], hold_time=BUTTON_HOLD_TIME_SECONDS)
    button_7.when_released = lambda x: button_release(BUTTON_7, button_7)
    button_7.when_held = lambda x: button_held(BUTTON_7, button_7)
    recorder.VideoRecorder.num_threads += 1


##
# Runs upon a button action/press. Two possible actions exist:
# 1. If a file for the button exists, its recorded video will play
# 2. If a file for the button does not exist, a recording for it
#    will begin and be saved to it
#
# button_name => name of button so it can be mapped to the correct file
# gpio_button => GPIOZero button object, needed to know the state of the button hold/press
##
def button_release(button_name, gpio_button):
    if gpio_button.was_held:
        gpio_button.was_held = False
        return
    
    file_name = Config.buttons_to_files[button_name]
    local_path = os.getcwd()
    # 1. File exists? Play video
    if os.path.exists(str(local_path) + "/" + file_name + ".avi"):
        play_video(file_name + ".avi")
    else:
        record_video(file_name, RECORD_TIME_SECONDS)


##
# On a button hold action, a video is recorded regardless if there
# is a video already mapped to the called button. The new video 
# overwrites the existing one.
#
# button_name => name of button so it can be mapped to the correct file
# gpio_button => GPIOZero button object, needed to know the state of the button hold/press
##
def button_held(button_name, gpio_button):
    gpio_button.was_held = True
    file_name = Config.buttons_to_files[button_name]
    local_path = os.getcwd()
    if os.path.exists(str(local_path) + "/" + file_name + ".avi"):
        os.remove(str(local_path) + "/" + file_name + ".avi")
        erase_wave_obj = sa.WaveObject.from_wave_file("sounds/erase.wav")
        play_obj = erase_wave_obj.play()
        play_obj.wait_done()
        time.sleep(2)
        Config.is_running = False
    else:
        print("No file to erase")
        Config.is_running = False



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


    #play some audio to indicate recording has begun
    record_wave_obj = sa.WaveObject.from_wave_file("sounds/record.wav")
    play_obj = record_wave_obj.play()


#    record = AudioSegment.from_wav("sounds/record.wav")
#    play(record)



    # recording begins
    recorder.start_AVrecording(file_name)
    # recording will be uninterrupted for the 
    # specified amount of time
    time.sleep(record_time)
    # After the timer is done, the recording is
    # stopped and the files are saved
    recorder.stop_AVrecording(file_name)
    done_wave_obj = sa.WaveObject.from_wave_file("sounds/done.wav")
    play_obj = done_wave_obj.play()
    play_obj.wait_done()

    
    print("Recording completed")
    
    # After a recording, we shut down the program due to potential threading issues
    
    Config.is_running = False


##
# Plays a video with the vlc media player for
# the specified file name
##
def play_video(file_name):
    play_wave_obj = sa.WaveObject.from_wave_file("sounds/play.wav")
    play_obj = play_wave_obj.play()
    media = vlc.Media(file_name)
    Config.media_player.set_fullscreen(True)
    Config.media_player.set_media(media)
    Config.media_player.play()
    time.sleep(10)
    Config.media_player.release()
    play_obj.wait_done()
    # After video is finished, shut down the program to avoid threading issues
    Config.is_running = False


##
# Function that generates the file name that is saved,
# using number values 1 to 8
##
def create_file_name(file_name):
    for i in range(1, 8):
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
    button_release(BUTTON_1)