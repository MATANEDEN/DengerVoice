from pydub import AudioSegment


ogg_file = r'C:\Users\dev2\Desktop\db\temp.ogg'
wav_file = r'C:\Users\dev2\Desktop\db\temp1.wav'

# wave and raw don’t use ffmpeg
wav_audio = AudioSegment.from_file(r"C:\Users\dev2\Desktop\db\temp.ogg", format="ogg")
raw_audio = AudioSegment.from_file(r"C:\Users\dev2\Desktop\db\temp.ogg", format="ogg",
                                   frame_rate=44100, channels=2, sample_width=2)

wav_audio.export(r'C:\Users\dev2\Desktop\db\temp1.wav', format="wav")
raw_audio.export(r'C:\Users\dev2\Desktop\db\temp1.wav', format="wav")