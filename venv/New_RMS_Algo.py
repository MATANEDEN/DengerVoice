import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import sys
import os
import soundfile as sf





# old_stdout = sys.stdout
# log_file = open(os.path.join(r'C:\Users\Eden\PycharmProjects\final_project', 'logfile.log'), 'w')
# sys.stdout = log_file


def norm(data, simple=False):
    min_v = min(data)
    max_v = max(data)
    if simple is False:
        offset = min_v + max_v
        data = data + (offset / 2)
        data = np.array([((x - min_v) / (max_v - min_v)) for x in data]) * 2.0 - 1
        return data * ((max_v / min_v) * -1)
    else:
        return np.array([((x - min_v) / (max_v - min_v)) for x in data])


def flat_edge(arr, keyframes, intro=True):
    if intro:
        a = keyframes[0]
        b = int(keyframes[1] // 2)
    else:
        a = int(keyframes[-2] + ((len(arr) - keyframes[-2]) // 2))
        b = keyframes[-1]

    for i in range(a, b):
        arr[i] = 0
    return arr


def gates(signal, segments, speed=50):
    ones = np.ones_like(signal)
    for s in segments:
        ones[s[0]:s[1]] = norm(np.cosh(np.linspace(-speed, speed, s[1] - s[0])), True)
    return ones


def segments(keyframes, First=True):
    return [(keyframes[i], keyframes[i + 1]) for i in range(int(not First), len(keyframes) - 1, 2)]


def threshold_keyframes(rms, threshold):
    keyframes = [0]
    lastkeyframewasUp = False

    for i in range(len(rms)):
        if rms[i] < threshold:
            if lastkeyframewasUp == True:
                keyframes.append(i)
                lastkeyframewasUp = False
        else:
            if lastkeyframewasUp == False:
                keyframes.append(i)
                lastkeyframewasUp = True

    keyframes.append(len(signal))

    if keyframes[1] == 0:
        del keyframes[0]
    return keyframes


# read file

samplerate, signal = wavfile.read(r"C:\Users\Eden\Desktop\temp\take1.wav")
# signal = signal[:0]
signal = norm(np.array(signal, dtype=np.float64))

########-RMS-#########
rms = np.zeros_like(signal)
buffer_size = 1000
yellow_list=[]

for i in range(0, len(signal), buffer_size):
    s = signal[i:i + buffer_size]
    if max(s) >= 0.07:
        yellow_list.append(i)
    rms[i:i + buffer_size] = np.sqrt(np.mean(s ** 2))





list_words = []
for i in range(len(yellow_list)-1):
    if(yellow_list[i+1]-yellow_list[i])>30000:
        # print(yellow_list[i]/44100)
        list_words.append(yellow_list[i])
        list_words.append(yellow_list[i+1])


list_words.append(yellow_list[-1])
list_words.insert(0,yellow_list[0])

s = 0
for i in range(0,len(list_words),2):
    start = list_words[i]
    stop = list_words[i+1]

    len_of_audio=50000 #samples
    Calc = stop  - start
    if Calc<len_of_audio:

       off_set =int((len_of_audio-Calc)/2)
       start = start-off_set
       stop = stop+off_set

    Data = signal[start : stop]
    sf.write(os.path.join(r'C:\Users\Eden\Desktop\temp','word'+str(s)+'.wav'), Data, samplerate)
    s = s+1




cutoff = 20
normal_cutoff = cutoff / (44100 / 2)
b, a = butter(2, normal_cutoff, btype="low", analog=False)
rms = filtfilt(b, a, rms)

# calculate gate
threshold = 0.07
flip_order = True

keyframes = threshold_keyframes(rms, threshold)
g = gates(signal, segments(keyframes, flip_order), 50)

### flate edges #####
g = flat_edge(g, keyframes, True)
g = flat_edge(g, keyframes, False)


## gate signal
gated = signal * g

######## Draw ##########
plt.plot(range(len(signal)), signal, "black")
plt.plot(range(len(signal)), gated, "pink")

plt.plot(range(len(signal)), g, "yellow", label="Above or Below the threshold line")
plt.plot(range(len(signal)), rms, "red", label="Root Mean Squre")

plt.xlabel('Samples')
plt.ylabel('RMS')

plt.axhline(y=threshold, color="green", label='Threshold')

plt.legend()
plt.show()
