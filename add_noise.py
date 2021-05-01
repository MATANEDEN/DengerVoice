import soundfile as sf
import numpy as np
import  os

def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x - min_v) / (max_v - min_v)) for x in data]) * 2.0 - 1


def get_one_channel(signal,wind):
    if len(wind.shape)>1:
        wind=wind[:,0]
    if len(signal.shape)>1:
        signal = signal[:,0]
    return wind,signal


def get_maximum_length(signal,wind):
    if len(signal)>= len(wind):
        max_length = len(wind)
    else:
        max_length = len(signal)

    return max_length


def add_noise(clear_signal, noise_path, amplitude):
    signal, samplerate = sf.read(clear_signal)
    wind, a = sf.read(noise_path)

    wind,signal  = get_one_channel(signal,wind)

    maximum_len = get_maximum_length(signal,wind)
    signal = signal[:maximum_len]
    wind = wind[:maximum_len]
    dirty = norm(signal + wind)
    sf.write(os.path.join(os.path.dirname(clear_signal) , 'new.wav'), dirty, samplerate)


if __name__ == '__main__':
    clear_signal = r'C:\Users\dev2\Downloads\exp\m.wav'
    noise_path = r'C:\Users\dev2\Downloads\exp\city_sound.wav'
    amplitude = 0.1
    add_noise(clear_signal, noise_path, amplitude)