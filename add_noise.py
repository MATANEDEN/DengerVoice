import soundfile as sf
import numpy as np


def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1


def add_noise(clear_signal, noise_path,amplitude):
    signal, samplerate = sf.read(clear_signal)
    wind , a = sf.read(noise_path)

    short_wind = amplitude*wind[:len(signal)]
    short_wind = short_wind[:,0]
    dirty = norm(signal+short_wind)
    sf.write(r'C:\Users\mataned\Downloads\New folder\asa_maniak.wav', dirty, samplerate)


if __name__ == '__main__':
    clear_signal = r'C:\Users\mataned\Downloads\New folder\baras.wav'
    noise_path = r'C:\Users\mataned\Downloads\New folder\wind.wav'
    amplitude = 0.1