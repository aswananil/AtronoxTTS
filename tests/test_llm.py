import sys
import os

# Add the parent directory to the Python path to allow importing from `src`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm import LLM

def test_llm_hello():
    """
    Tests the LLM's response to a greeting.
    """
    llm = LLM()
    response = llm.get_response("hello")
    assert response == "Hello there! How are you?"

def test_llm_how_are_you():
    """
    Tests the LLM's response to "how are you".
    """
    llm = LLM()
    response = llm.get_response("how are you")
    assert response == "I am just a computer program, but I am doing great!"

def test_llm_unknown():
    """
    Tests the LLM's response to an unknown input.
    """
    llm = LLM()
    response = llm.get_response("what is your name?")
    assert response == "Sorry, I am a very simple bot and I don't understand that yet."
