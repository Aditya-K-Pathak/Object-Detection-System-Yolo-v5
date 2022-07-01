from gtts import gTTS
import time
import os


def speak(text):
        language = 'en'

        obj = gTTS(text=text, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # speech
        obj.save("speech.mp3")

        # Playing the converted file
        os.system("speech.mp3")
        time.sleep(2)
