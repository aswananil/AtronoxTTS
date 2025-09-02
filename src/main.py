from stt import SpeechToText
from tts import TextToSpeech
from llm import LLM

class Atronox:
    """
    The main class for the Atronox conversational agent.
    """
    def __init__(self):
        """
        Initializes the Atronox agent by setting up the STT, TTS, and LLM components.
        """
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.llm = LLM()

    def run(self):
        """
        Runs the main loop of the Atronox agent.
        """
        self.tts.speak("Atronox is online.")
        while True:
            # 1. Listen for audio
            print("\nListening for user input...")
            audio_data = self.stt.listen()

            if audio_data:
                # 2. Transcribe audio to text
                text = self.stt.transcribe(audio_data)

                if text:
                    # 3. Get response from LLM
                    response = self.llm.get_response(text)

                    # 4. Speak the response
                    self.tts.speak(response)

if __name__ == "__main__":
    atronox = Atronox()
    atronox.run()
