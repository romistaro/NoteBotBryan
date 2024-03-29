import pyaudio
import wave
from pydub import AudioSegment
import threading

from transcription.stt import stt

# Set up parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096  # Buffer size
RECORD_SECONDS = 3
FILENAMES = ['f1.wav', 'f2.wav']

audio = pyaudio.PyAudio()
should_loop=False
def start_loop():
    file_index = 0
    while should_loop:
        threading.Thread(target=record_and_transcribe, args=(file_index,)).start()
        file_index = 1 - file_index
        threading.Event().wait(RECORD_SECONDS)
# Function to handle the recording and transcription
def record_and_transcribe(file_index):
    # Record
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()

    # Save the chunk to a file
    filename = FILENAMES[file_index]
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    # Transcribe
    stt(filename)



def start_mic():
    global should_loop
    should_loop=True
    threading.Thread(target=start_loop).start()





def stop_mic():
    global should_loop
    should_loop=False


if __name__ == "__main__":
    start_loop()