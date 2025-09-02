import pyttsx3

class TextToSpeech:
    """
    A class to handle Text-to-Speech conversion using pyttsx3.
    """
    def __init__(self):
        """
        Initializes the TextToSpeech class by setting up the TTS engine.
        """
        self.engine = pyttsx3.init()

    def speak(self, text):
        """
        Speaks the given text using the TTS engine.
        """
        if text:
            print(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()

if __name__ == '__main__':
    tts = TextToSpeech()
    tts.speak("Hello, I am Atronox. How can I help you today?")
