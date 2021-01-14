import os
import natsort

def order_files_by(main_dir):
    list_words = []
    dir_path = os.path.dirname(main_dir)
    all_files = os.listdir(os.path.dirname(main_dir))
    all_files = natsort.natsorted(all_files)


    for i in range(len(all_files)):
        if all_files[i].startswith('word'):
            list_words.append(os.path.join(dir_path, all_files[i]))


    return list_words

