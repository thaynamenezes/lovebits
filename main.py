import time
import recorder

FILE_NAME = "Thayna_Test"
RECORD_TIME_SECONDS = 15

# dictionary (hashmap)
buttons_to_files = {
    "button1": "video_1"
}

def record_video(file_name, record_time):
    # This line sets up the file names for the temp
    # files and the main file where botht the audio
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

# Here we need to find a way to get the raspberry pi 
# to play the video through VLC media player
def play_video(file_name):
    pass

if __name__ == "__main__":
    record_video(FILE_NAME, RECORD_TIME_SECONDS)
