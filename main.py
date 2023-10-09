import sounddevice as sd
import soundfile as sf
from tkinter import *

def Voice_rec():
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration*freq), samplerate=freq, channels=2)
    sd.wait()
    return sf.write('my_Audio_file.flac', recording, freq)
master = Tk()
Label(master, text=" Voice Recorder  :").grid(row=0, sticky=W, rowspan=5)
b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
mainloop()
