import soundfile as sf


data, samplerate = sf.read(r'C:\Users\Eden\PycharmProjects\final_project\test\4_words.wav')

A=data[30*1000:85*1000]
B=data[140*1000:180*1000]
C=data[220*1000:270*1000]
D=data[340*1000:395*1000]
# E=data[int(1.38*1000000):int(1.425*1000000)]
# F=data[int(1.47*1000000):int(1.52*1000000)]
# G=data[int(1.57*1000000):int(1.62*1000000)]
# H=data[int(1.655*1000000):int(1.7*1000000)]
# I=data[int(1.74*1000000):int(1.8*1000000)]
# J=data[int(1.825*1000000):int(1.875*1000000)]
# K=data[int(1.92*1000000):int(1.97*1000000)]

print(samplerate)


sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word1_new.wav', A, samplerate)
sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word2_new.wav', B, samplerate)
sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word3_new.wav', C, samplerate)
sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word4_new.wav', D, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word24.wav', E, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word25.wav', F, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word26.wav', G, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word27.wav', H, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word28.wav', I, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word29.wav', J, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word30.wav', K, samplerate)
# sf.write(r'C:\Users\Eden\Desktop\my_new_proj\all_words\word21.wav', L, samplerate)