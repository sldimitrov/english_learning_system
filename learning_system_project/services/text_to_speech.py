import time
import pyttsx3

class TextToSpeech:
    """
    The functionality that this class applies to the project is that it, open the dictionary
    file and read every sentence from it. The idea behind this is to train listening and
    to hear the new words more often.
    """
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        """
        The function initializes a text-to-speech engine with specified voice, rate, and volume properties.

        :param voice: The "voice" parameter is used to specify the voice that the text-to-speech engine should use.
        It can be a string representing the name of the voice, or it can be set to None to use the default voice.
        :param rate: The "rate" parameter determines the speed at which the text is spoken. It is measured in words per
        minute (wpm). A higher rate value will result in faster speech, while a lower rate value will result in slower
        speech.
        :type rate: int
        :param volume: The "volume" parameter is used to control the volume of the voice output.
        It is a float value between 0.0 and 1.0, where 0.0 represents the lowest volume (mute)
        and 1.0 represents the highest volume
        :type volume: float
        """
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        """
        The function "list_available_voices" prints the name, age, and ID of each available voice.
        It is written in case you want to change the speaker. If you want to you should call the function once
        and then copy the ID of the person you'd like to speak.
        """
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i + 1} Name : {voice.name},  Age : {voice.age}, ID : [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()
        return True


def text_to_speech():
    """
    The function `text_to_speech` reads sentences from a file, and if there are any sentences, it converts them to
    speech using the specified voice and settings. If there are no sentences in the file, it prints a message
    indicating that there are no sentences.
    """
    tts = TextToSpeech.TextToSpeech('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0',
                                    200, 1.0)
    # tts.list_available_voices()
    f = open('text_files/sentences_list.txt', 'r')
    data = f.read()
    if data:
        counter = 1
        data = data.split('\n')
        data = [x for x in data if x != '']
        print('Listen...')
        for sentence in data:
            if sentence:
                tts.text_to_speech(sentence)
                print(f'({counter}/{len(data)})')
                time.sleep(3)
                counter += 1
        print('These were all of your sentences!')
    else:
        print('There are not any sentences written yet.')
