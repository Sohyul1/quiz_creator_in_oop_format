# Import random, Fore, style, init from colorama
import random
from colorama import Fore, Style, init

# import QuizReader from quiz_reader and Question from questions
from quiz_reader_oop_format import QuizReader
from question import Question

# Initialize autoreset of colors 
init(autoreset=True)
# Initialize QuizRunner class
class QuizRunner:
    def __init__(self, reader):
        self.reader = reader
        self.score = 0


# Methhod for asking the questions
