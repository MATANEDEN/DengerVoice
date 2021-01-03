import os
# from convert_audioformat import convert_audio_format

from RMS_algo import Preprocess_Signal





if __name__ == '__main__':

    # ogg_path = r'C:\Users\Eden\Downloads\a\part1.ogg'
    # convert_audio_format(ogg_path)

    main_dir =  ogg_path.replace('ogg','wav')
    Preprocess_Signal(main_dir)


