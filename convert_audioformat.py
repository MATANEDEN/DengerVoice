from pydub import AudioSegment



def convert_audio_format(ogg_path):

    wav_audio = AudioSegment.from_file(ogg_path, format="ogg")

    wav_audio.export(ogg_path.replace('ogg','wav'), format="wav")
