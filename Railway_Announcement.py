from pydub import AudioSegment
import pandas as pd
from gtts import gTTS



def Speak(string, file_name):
    text = str(string)
    tts = gTTS(text, lang='en-in')
    tts.save(file_name)


def separateClipsFromAudio():
    audio = AudioSegment.from_mp3('C:\\Users\\Snehashis_Saheb\\Documents\\Railways\\railway.mp3')

    # part1 'starting music'
    part1 = audio[41100:42350]
    part1.export('part1.mp3', format='mp3')

    # part2 attention
    part2 = audio[19000:23900]
    part2.export('part2.mp3', format='mp3')

    # part4 'from'
    part4 = audio[30200:31200]
    part4.export("part4.mp3", format='mp3')

    # part6 'to'
    part6 = audio[31650:32500]
    part6.export("part6.mp3", format='mp3')

    # part8 'via'
    part8 = audio[33700:34650]
    part8.export("part8.mp3", format='mp3')

    # part10 'is arriving shortly in platfrom number'
    part10 = audio[36500:40500]
    part10.export("part10.mp3", format='mp3')


def mergeClips(lst):
    combined = AudioSegment.empty()
    for audio in lst:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateAudioFromDf():
    df = pd.read_csv('train_list.csv')
    for index, item in df.iterrows():
        # part3 train number + space + train name
        Speak(item['train_no'] + " . " + item['train_name'], 'part3.mp3')
        # part5 station_name(from)
        Speak(item['from'], 'part5.mp3')
        # part7 station_name(to)
        Speak(item['to'], 'part7.mp3')
        # part9 station_name(via)
        Speak(item['via'], 'part9.mp3')
        # part11 platform number
        Speak(item['platform'], 'part11.mp3')

        audios = [f"part{i}.mp3" for i in range(1, 12)]
        announcement = mergeClips(audios)
        announcement.export(f"Announcemnt_of_{item['train_no']}.mp3", format='mp3')


if __name__ == '__main__':
    separateClipsFromAudio()
    generateAudioFromDf()
