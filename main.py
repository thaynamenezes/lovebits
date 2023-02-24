import time
import recorder
import os

FILE_NAME = "Lovebits_Test"
RECORD_TIME_SECONDS = 10

# dictionary (hashmap)
buttons_to_files = {
    "button1": "video_1"
}


##
#
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


##
# Here we need to find a way to get the raspberry pi 
# to play the video through VLC media player
##
def play_video(file_name):
    pass



if __name__ == "__main__":
    new_file_name = create_file_name(FILE_NAME)
    if new_file_name is None:
        print("ERROR: Acheived max capacity for videos.")
    else:
        record_video(new_file_name, RECORD_TIME_SECONDS)
