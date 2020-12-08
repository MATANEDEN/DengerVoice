from pydub import AudioSegment


ogg_file = r'C:\Users\Eden\Desktop\my_new_proj\20_words.ogg'
wav_file = r'C:\Users\Eden\Desktop\my_new_proj\200_words.wav'

# wave and raw don’t use ffmpeg
wav_audio = AudioSegment.from_file(r"C:\Users\Eden\Desktop\my_new_proj\20_words.ogg", format="ogg")
raw_audio = AudioSegment.from_file(r"C:\Users\Eden\Desktop\my_new_proj\20_words.ogg", format="ogg",
                                   frame_rate=44100, channels=2, sample_width=2)

wav_audio.export(r'C:\Users\Eden\Desktop\my_new_proj\200_words.wav', format="wav")
raw_audio.export(r'C:\Users\Eden\Desktop\my_new_proj\200_words.wav', format="wav")
#