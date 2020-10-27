import soundfile as sf


data, samplerate = sf.read(r'C:\Users\dev2\Desktop\my_project\python_dsp\test\shooting.wav')

C=data[59*samplerate:64*samplerate]
print(samplerate)
print(C)

sf.write(r'C:\Users\dev2\Desktop\my_project\python_dsp\test\shooting_orig.wav', C, samplerate)
