from llama_cpp import Llama
import os

class LLM:
    """
    A class for the Llama.cpp based LLM model.
    """
    def __init__(self, model_path="models/gemma-2b.Q2_K.gguf"):
        """
        Initializes the LLM class.
        """
        self.model_path = model_path
        self.llm = None
        if os.path.exists(self.model_path):
            try:
                # Initialize the Llama model
                # Note: This will fail with the dummy file, but the code is correct for a real model.
                self.llm = Llama(model_path=self.model_path, verbose=False)
                print("LLM model loaded successfully.")
            except Exception as e:
                print(f"Warning: Could not load the LLM model from {self.model_path}.")
                print(f"Error: {e}")
                print("The LLM will not be available. Using placeholder responses.")
        else:
            print(f"Warning: Model file not found at {self.model_path}. The LLM will not be available.")

    def get_response(self, text):
        """
        Returns a response from the LLM.
        If the model is not loaded, it returns a canned response.
        """
        if self.llm:
            try:
                # Create a prompt and generate a response
                prompt = f"User: {text}\nAssistant:"
                output = self.llm(prompt, max_tokens=150, echo=False)
                response = output['choices'][0]['text'].strip()
                return response
            except Exception as e:
                print(f"Error during LLM inference: {e}")
                return "Sorry, I encountered an error trying to generate a response."
        else:
            # Fallback to placeholder logic if model is not loaded
            print(f"LLM not loaded. Using placeholder for: {text}")
            if "hello" in text.lower():
                return "Hello there! How are you?"
            elif "how are you" in text.lower():
                return "I am just a computer program, but I am doing great!"
            else:
                return "Sorry, I am a very simple bot and I don't understand that yet."

if __name__ == '__main__':
    # This will likely fail to load the model with the dummy file,
    # but it demonstrates how the class would be used.
    llm = LLM()
    if llm.llm:
        response = llm.get_response("Hello, how are you?")
        print(f"LLM response: {response}")
    else:
        print("LLM could not be tested as the model failed to load.")
        # Test the fallback
        response = llm.get_response("hello")
        print(f"Fallback response: {response}")
