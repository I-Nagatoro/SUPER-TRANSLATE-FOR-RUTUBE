import moviepy.editor as mp
import speech_recognition as sr
import translators as ts
from gtts import gTTS
from moviepy.editor import *
import os
video = mp.VideoFileClip("C:\\vid\\8.mp4")

print('Вытаскиваю аудио из видео')
audio_file = video.audio
audio_file.write_audiofile("audio.wav")
r = sr.Recognizer()

print('Загружаю аудио')
with sr.AudioFile("audio.wav") as source:
    data = r.record(source)

print('Преобразовываю речь в текст')
text = r.recognize_google(data, language="ru-RU")

print('Делаю текстовый документ')
my_file = open("ru_text.txt", "w+")
my_file.write(text)
my_file.close()

print('Перевожу текст')
text=ts.translate_text(text,to_language="en")
my_file = open("en_text.txt", "w+")
my_file.write(text)

print('Озвучка')
audio = gTTS(text=text, lang="en", slow=False)
audio.save("example.mp3")

print('Свожу видео и аудио')
audio_clip=AudioFileClip("example.mp3")
final_video=video.set_audio(audio_clip)
final_video.write_videofile("a.mp4")

print("Запускаю видео")
os.system("start a.mp4")