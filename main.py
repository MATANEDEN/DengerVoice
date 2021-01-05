from order_files import order_files_by
from convert_audioformat import convert_audio_format
from RMS_algo import Preprocess_Signal
from keyword_spotting_service import Keyword_Spotting_Service
from Alert import alert_massage
from csv_testing import write_to_csv




if __name__ == '__main__':
    list_text = []
    dangerous_word = 'left'
    ogg_path = r'C:\Users\Eden\Downloads\a\part1.ogg'
    convert_audio_format(ogg_path)

    main_dir =  ogg_path.replace('ogg','wav')
    Preprocess_Signal(main_dir)

    files  = order_files_by(main_dir)
    kss = Keyword_Spotting_Service()
    for i in range(len(files)):
        list_text.append(kss.predict(files[i]))

    print(list_text)
    for  j in range(len(list_text)):
        if list_text[j]==dangerous_word:
            alert_massage()


    write_to_csv(list_text)

