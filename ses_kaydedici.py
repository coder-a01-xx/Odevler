import sounddevice as sd

import numpy as np

from scipy.signal import butter,filtfilt

from scipy.io.wavfile import write


hız=44000

süre=int(input("Ses kaydı kaç saniye sürsün"))

print("İşlem sürüyor")


kaydetme= sd.rec(int(süre*hız),samplerate=hız, channels=1,dtype="float32")

sd.wait()

print("tamm")


def butter_lowpass_filter(data,cutoff,hız,order=5):

    nyq=0.5*hız

    normal_cutoff=cutoff/nyq

    b,a=butter(order,normal_cutoff,btype="low",analog=False)

    y=filtfilt(b,a,data,axis=0)

    return y


cutoff_freq=2000

#filtered_audio=butter_lowpass_filter(kaydetme,cutoff=cutoff_freq,hız=hız)
#filtered_audio=filtered_audio*5


print("Ses çalınıyor")

sd.play(kaydetme,samplerate=hız)

sd.wait()

print("Bitti")