import speech_recognition as sr

class SpeechToText:
    """
    A class to handle Speech-to-Text conversion using the Whisper engine.
    """
    def __init__(self):
        """
        Initializes the SpeechToText class by setting up the recognizer
        and microphone.
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """
        Listens for audio from the microphone and returns the audio data.
        """
        with self.microphone as source:
            print("Listening...")
            # Adjust for ambient noise to improve accuracy
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                # Listen for speech and capture the audio
                audio = self.recognizer.listen(source)
                return audio
            except sr.WaitTimeoutError:
                print("No speech detected within the timeout period.")
                return None


    def transcribe(self, audio):
        """
        Transcribes the given audio data to text using the Whisper engine.
        """
        if audio is None:
            return None
        try:
            print("Transcribing...")
            # Use the Whisper engine to recognize the speech
            text = self.recognizer.recognize_whisper(audio)
            return text
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Whisper; {e}")
            return None

if __name__ == '__main__':
    stt = SpeechToText()
    print("Say something!")
    audio_data = stt.listen()
    if audio_data:
        text = stt.transcribe(audio_data)
        if text:
            print(f"Transcribed text: {text}")
